from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Comentario, Vehiculo, Viaje, Lugar, Ruta, Pasaje, Testeo

admin.site.site_header = 'Sitio administrativo de COMBI-19'

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['patente', 'chofer', 'capacidad','modelo']

class LugarAdmin(admin.ModelAdmin):
    list_display = ['nombre','provincia','codigo_postal']
    list_filter =['provincia']

class RutaAdmin(admin.ModelAdmin):
    list_display=['origen','destino','km','nombre']
    list_filter =['origen', 'destino']

class ViajeAdmin(admin.ModelAdmin):
    list_display=['fecha','ruta','combi','estado','precio']
    list_filter =['estado','fecha','ruta','combi','precio']


class PasajeAdmin(admin.ModelAdmin):
    list_display=['usuario','viaje','cantidad']
    list_filter =['viaje__estado', 'viaje__fecha']

class TesteoAdmin(admin.ModelAdmin):
    list_display=['usuario','temperatura', 'tos', 'dolor_cabeza', 'dolor_muscular', 'dolor_garganta', 'vomitos_diarrea','perdida_gusto_olfato','dificultad_respiratoria']
    fields=[]
    list_filter =['cantidad','viaje']

    def has_add_permission(self, request):
        return False 
    def has_change_permission(self, request, obj=None):
        return False



class ComentarioAdmin(admin.ModelAdmin):
    list_display=['usuario','comentario']
    list_filter =['ruta']
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False

# class InsumoAdmin(admin.ModelAdmin):
#     list_display = ['nombre','descripcion','precio','cantidad']

admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Viaje, ViajeAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Pasaje, PasajeAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Testeo, TesteoAdmin)