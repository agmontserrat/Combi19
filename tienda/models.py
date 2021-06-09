from django.db import models

# Create your models here.
class Insumo(models.Model):
    nombre        = models.CharField(max_length=30)
    descripcion   = models.CharField(max_length=50)
    precio        = models.IntegerField()
    imagen        = models.ImageField(upload_to="insumos", null=True)
    cantidad      = models.IntegerField(blank=True, null=True)
    created       = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated       = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'
