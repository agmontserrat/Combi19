from django.contrib import admin
from .models import Vehiculo, Insumo, Viaje, Lugar

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Insumo)
admin.site.register(Viaje)
admin.site.register(Lugar)