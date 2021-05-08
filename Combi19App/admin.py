from django.contrib import admin
from .models import Vehiculo, Insumo, Viaje, Lugar, Ruta

admin.site.site_header = 'Sitio administrativo de COMBI-19'

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Insumo)
admin.site.register(Viaje)
admin.site.register(Lugar)
admin.site.register(Ruta)