from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    modelo = models.IntegerField()

class Insumo(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=30)
    precio = models.IntegerField()

class Pasaje():
    pass

class Viaje(models.Model):
    fecha = models.DateField()

class Lugar(models.Model):
    nombre = models.CharField(max_length=15)
    

class Ruta(models.Model):
    origen = models.CharField(max_length=15)
    destino = models.CharField(max_length=15)
    km = models.IntegerField()
    

class Combi():
    pass

class Testeo():
    pass