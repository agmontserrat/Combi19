from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Insumo

# Register your models here.

class InsumoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','precio','cantidad']

admin.site.register(Insumo, InsumoAdmin)