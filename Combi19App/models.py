from django.db import models
from django.db.models.expressions import F
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from tienda.models import Insumo
# Create your models here.
from users.models import Account, Chofer

class Vehiculo(models.Model):

    patente       = models.CharField(max_length=10, unique=True)
    capacidad     = models.IntegerField(validators=[MinValueValidator(0)])
    modelo        = models.IntegerField()
    chofer        = models.ForeignKey(Chofer, blank=True, null=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente

class Lugar(models.Model):
    nombre        = models.CharField(max_length=40, blank=True, null=True, unique=True, verbose_name='Lugar')
    provincia     = models.CharField(max_length=20, blank=True, null=True)
    codigo_postal = models.IntegerField(blank=True, null=True, unique=True, validators=[MinValueValidator(1000)])
    imagen        = models.ImageField(upload_to="ciudades", blank=True, null=True)
    class Meta:
        verbose_name_plural = "Lugares"
        

    def __str__(self):
        return f'{self.nombre}'

class Ruta(models.Model):
    origen        = models.ForeignKey(Lugar, default=None, on_delete=models.CASCADE, related_name='origen')
    destino       = models.ForeignKey(Lugar, default=None, on_delete=models.CASCADE, related_name='destino')
    nombre        = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nombre de ruta')
    km            = models.IntegerField(validators=[MinValueValidator(0)])

    def clean(self):
        if self.origen==self.destino:
            raise ValidationError('Los campos no pueden coincidir')
    

    class Meta:
        unique_together = ('origen', 'destino')
        
    def __str__(self):
        return f'De {self.origen} a {self.destino}'

class Comentario(models.Model):
    usuario    = models.ForeignKey(Account, default=None, null=True,on_delete=models.CASCADE)
    comentario = models.CharField(max_length=300)
    ruta       = models.ForeignKey(Ruta, default=None, null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.usuario}: {self.comentario}"

class Viaje(models.Model):
    comenzado  = "com"
    finalizado = "fin"
    cancelado  = "can"
    ESTADO_CHOICES = [ (comenzado,'COMENZADO'), (finalizado, 'FINALIZADO'), (cancelado,'CANCELADO') ]
    
    
    fecha             =   models.DateTimeField(blank=True, null=True)
    ruta              =   models.ForeignKey(Ruta, default=None, blank=True, null=True, on_delete=models.CASCADE)
    combi             =   models.ForeignKey(Vehiculo, blank=True, null=True, on_delete=models.CASCADE)
    precio            =   models.DecimalField(default=None, blank=True, null=True, max_digits=10, decimal_places=2)
    insumo            =   models.ManyToManyField(Insumo,default=None, blank=True)
    pasajeros         =   models.ManyToManyField(Account, default=None, blank=True)
    asientos_ocupados =   models.IntegerField(default=0, null=True, blank=True)
    estado            =   models.CharField(max_length=3, choices=ESTADO_CHOICES, default=ESTADO_CHOICES[0])
    
    class Meta:
        unique_together = ('fecha', 'combi')
        
    def __str__(self):
        return f'Fecha: {self.fecha:%Y-%m-%d %H:%M} - Ruta: {self.ruta} - Combi: {self.combi} '

    def finalizar_viaje(self):
        self.estado = self.finalizado
    
    def cancelar_viaje(self):
        self.estado = self.cancelado

class Pasaje(models.Model):
    pendiente  = "pen"
    finalizado = "fin"
    cancelado  = "can"
    ESTADO_CHOICES = [ (pendiente,'PENDIENTE'), (finalizado, 'FINALIZADO'), (cancelado,'CANCELADO') ]
    
    viaje    = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    usuario  = models.ForeignKey(Account, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True)
    estado   = models.CharField(max_length=3, choices=ESTADO_CHOICES, default=ESTADO_CHOICES[0])

    class Meta:
        verbose_name_plural = "Pasajes"

class Testeo(models.Model):
    usuario                 = models.ForeignKey(Account, on_delete=models.CASCADE)
    viaje                   = models.ForeignKey(Viaje, on_delete=models.CASCADE, blank=True, null=True)
    temperatura             = models.FloatField()
    dolor_cabeza            = models.BooleanField()
    dolor_garganta          = models.BooleanField()
    dolor_muscular          = models.BooleanField()
    vomitos_diarrea         = models.BooleanField()
    perdida_gusto_olfato    = models.BooleanField()
    tos                     = models.BooleanField()
    dificultad_respiratoria = models.BooleanField()
    cantidad                = models.IntegerField(verbose_name='Cantidad de sintomas', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Testeos"