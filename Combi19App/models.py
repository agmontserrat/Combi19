from django.db import models
from django.db.models.expressions import F

# Create your models here.


class Vehiculo(models.Model):
    patente       = models.CharField(max_length=10)
    capacidad     = models.IntegerField()
    modelo        = models.IntegerField()

    def __str__(self):
        return self.patente


class Insumo(models.Model):
    nombre        = models.CharField(max_length=15)
    descripcion   = models.CharField(max_length=30)
    precio        = models.IntegerField()
    imagen        = models.ImageField(upload_to="insumos", null=True)

    def __str__(self):
        return self.nombre


class Lugar(models.Model):
    nombre        = models.CharField(max_length=15)
    codigo_postal = models.IntegerField(blank=True, null=True)
    verbose_name_plural='Lugares'

    def __str__(self):
        return self.nombre


class Ruta(models.Model):
    choices      = [(lugar.nombre, lugar.nombre) for lugar in Lugar.objects.all()]
    origen       = (models.CharField(max_length=15, null=False, blank=False, choices=choices))
    destino      = (models.CharField(max_length=15, null=False, blank=False, choices=choices))
    nombre       = models.CharField(max_length=30, blank=True, null=True)
    km           = models.IntegerField()

    def __str__(self):
        return f'Origen: {self.origen} --> Destino: {self.destino}'


class Viaje(models.Model):
    fecha         =   models.DateTimeField(blank=True, null=True)
    ruta          =   models.ForeignKey(Ruta, default=None, on_delete=models.CASCADE)
    combi         =   models.ForeignKey(Vehiculo, blank=True, null=True, on_delete=models.CASCADE)
    estado        = models.BooleanField(default=False)

    def __str__(self):
        return f'Fecha: {self.fecha} - Ruta: {self.ruta} - Combi:{self.combi} '


class Pasaje():
    viaje = models.ForeignKey(Viaje, on_delete=models.PROTECT)
    
    
class Testeo():
    pass