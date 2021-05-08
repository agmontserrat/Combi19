from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10)
    capacidad = models.IntegerField()
    modelo = models.IntegerField()

    def __str__(self):
        return self.patente

class Insumo(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="insumos", null=True)

    def __str__(self):
        return self.nombre


class Pasaje():
    pass


class Lugar(models.Model):
    nombre = models.CharField(max_length=15)
    verbose_name_plural='Lugares'

    def __str__(self):
        return self.nombre


class Ruta(models.Model):
    choices = [(lugar.nombre, lugar.nombre) for lugar in Lugar.objects.all()]
    origen = (models.CharField(max_length=15,null=False, blank=False, choices=choices))
    destino = (models.CharField(max_length=15,null=False, blank=False, choices=choices))
    km = models.IntegerField()
    def __str__(self):
        return f'Origen: {self.origen} --> Destino: {self.destino}'

class Viaje(models.Model):
    fecha = models.DateField()
    ruta = models.ForeignKey(Ruta, default=None, on_delete=models.CASCADE)
    #choicesC = [(combi.patente, combi.patente) for combi in Vehiculo.objects.all()]
    #combi = (models.CharField(max_length=15,null=False, blank=False, choices=choicesC))
    combi = models.ForeignKey(Vehiculo, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return f'Fecha: {self.fecha} - Ruta: {self.ruta} - Combi:{combi} '
    
class Combi():
    pass

class Testeo():
    pass