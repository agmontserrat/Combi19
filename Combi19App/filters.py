from django.db.models import fields
import django_filters
from django_filters import DateTimeFilter, CharFilter

from .models import *

class ViajeFilter(django_filters.FilterSet):
    start_date = DateTimeFilter(field_name="fecha", lookup_expr='gte', label='Fecha')
    
    ruta__origen__nombre = django_filters.CharFilter(lookup_expr='icontains', label='Origen')
    ruta__destino__nombre = django_filters.CharFilter(lookup_expr='icontains', label='Destino')
    class Meta:
        model = Viaje
        fields = '__all__'
        exclude = ['fecha', 'ruta','combi', 'estado', 'pasajeros', 'insumo', 'comentarios', 'precio']

