from django.db import models
from django.db.models.expressions import F
from django.db.models.constraints import UniqueConstraint
from django.core.exceptions import ValidationError

# Create your models here.
from users.models import Chofer

class Vehiculo(models.Model):

    patente       = models.CharField(max_length=10, unique=True)
    capacidad     = models.IntegerField()
    modelo        = models.IntegerField()
    chofer        = models.ForeignKey(Chofer, blank=True, null=True, default=None, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente


class Insumo(models.Model):
    nombre        = models.CharField(max_length=30)
    descripcion   = models.CharField(max_length=50)
    precio        = models.IntegerField()
    imagen        = models.ImageField(upload_to="insumos", null=True)
    cantidad      = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'


class Lugar(models.Model):
    nombre        = models.CharField(max_length=40, blank=True, null=True, unique=True)
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
    nombre        = models.CharField(max_length=30, blank=True, null=True)
    km            = models.IntegerField()

    def clean(self):
        if self.origen==self.destino:
            raise ValidationError('Los campos no pueden coincidir')
    

    class Meta:
        unique_together = ('origen', 'destino')
        
    def __str__(self):
        return f'Origen: {self.origen} --> Destino: {self.destino}'


class Viaje(models.Model):
    
    fecha         =   models.DateTimeField(blank=True, null=True)
    ruta          =   models.ForeignKey(Ruta, default=None, blank=True, null=True, on_delete=models.CASCADE)
    combi         =   models.ForeignKey(Vehiculo, blank=True, null=True, on_delete=models.CASCADE)
    estado        =   models.BooleanField(default=False)
    # chofer        =   models.ForeignKey(Chofer, default=None, on_delete=models.PROTECT)
    # insumo        =   models.ManyToManyField(Insumo, default="",blank=True, null=True)

    
    class Meta:
        unique_together = ('fecha', 'combi')
        

    def __str__(self):
        return f'Fecha: {self.fecha} - Ruta: {self.ruta} - Combi:{self.combi} '


class Pasaje():
    viaje = models.ForeignKey(Viaje, on_delete=models.PROTECT)
    
    
class Testeo():
    pass