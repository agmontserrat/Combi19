from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Vehiculo, Viaje, Lugar, Ruta, Pasaje

admin.site.site_header = 'Sitio administrativo de COMBI-19'

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['patente', 'chofer', 'capacidad','modelo']

class LugarAdmin(admin.ModelAdmin):
    list_display = ['nombre','provincia','codigo_postal']

class RutaAdmin(admin.ModelAdmin):
    list_display=['origen','destino','km','nombre']

class ViajeAdmin(admin.ModelAdmin):
    list_display=['fecha','ruta','combi','estado','precio']

class PasajeAdmin(admin.ModelAdmin):
    list_display=['usuario','viaje']

# class InsumoAdmin(admin.ModelAdmin):
#     list_display = ['nombre','descripcion','precio','cantidad']

admin.site.register(Vehiculo, VehiculoAdmin)
# admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Pasaje, PasajeAdmin)
admin.site.register(Ruta, RutaAdmin)