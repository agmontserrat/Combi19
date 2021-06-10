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
    capacidad     = models.IntegerField()
    modelo        = models.IntegerField()
    chofer        = models.ForeignKey(Chofer, blank=True, null=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente


class Lugar(models.Model):
    nombre        = models.CharField(max_length=40, blank=True, null=True, unique=True, verbose_name='Lugar')
    provincia     = models.CharField(max_length=20, blank=True, null=True)
    codigo_postal = models.IntegerField(blank=True, null=True, unique=True)
    imagen        = models.ImageField(upload_to="ciudades", blank=True, null=True)
    class Meta:
        verbose_name_plural = "Lugares"
        

    def __str__(self):
        return f'{self.nombre}'


class Ruta(models.Model):
    origen        = models.ForeignKey(Lugar, default=None, on_delete=models.CASCADE, related_name='origen')
    destino       = models.ForeignKey(Lugar, default=None, on_delete=models.CASCADE, related_name='destino')
    nombre        = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nombre de ruta')
    km            = models.IntegerField()

    def clean(self):
        if self.origen==self.destino:
            raise ValidationError('Los campos no pueden coincidir')
    

    class Meta:
        unique_together = ('origen', 'destino')
        
    def __str__(self):
        return f'Origen: {self.origen} --> Destino: {self.destino}'

class Comentario(models.Model):
    usuario = models.ForeignKey(Account, default=None, null=True,on_delete=models.CASCADE)
    comentario = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario}: {self.comentario}"

class Viaje(models.Model):
    
    fecha         =   models.DateTimeField(blank=True, null=True)
    ruta          =   models.ForeignKey(Ruta, default=None, blank=True, null=True, on_delete=models.CASCADE)
    combi         =   models.ForeignKey(Vehiculo, blank=True, null=True, on_delete=models.CASCADE)
    estado        =   models.BooleanField(default=False)
    precio        =   models.DecimalField(default=None, blank=True, null=True, max_digits=10, decimal_places=2)
    insumo        =   models.ManyToManyField(Insumo,default=None, blank=True,)
    pasajeros     =   models.ManyToManyField(Account, default=None, blank=True,)
    comentarios   =   models.ManyToManyField(Comentario, default=None, blank=True, )
    asientos_ocupados = models.IntegerField(default=0, null=True, blank=True)
    
    class Meta:
        unique_together = ('fecha', 'combi')
        
    def __str__(self):
        return f'Fecha: {self.fecha} - Ruta: {self.ruta} - Combi:{self.combi} '

class Pasaje():
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Account, on_delete=models.CASCADE)  
    
class Testeo():
    pass