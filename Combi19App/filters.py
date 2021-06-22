from django.db.models import fields
import django_filters
from django_filters import DateTimeFilter, CharFilter, ModelChoiceFilter

from .models import *

class ViajeFilter(django_filters.FilterSet):
    """Filtro para Viajes"""
    start_date = DateTimeFilter(field_name="fecha", lookup_expr='gte', label='Fecha')
    # ruta__origen__nombre = CharFilter(lookup_expr='icontains', label='Origen')
    # ruta__destino__nombre = django_filters.CharFilter(lookup_expr='icontains', label='Destino')
    ruta__origen__nombre = ModelChoiceFilter(label="Origen",queryset=Lugar.objects.all())
    ruta__destino__nombre = ModelChoiceFilter(label="Destino",queryset=Lugar.objects.all().exclude(nombre=ruta__origen__nombre))
    class Meta:
        model = Viaje
        fields = '__all__'
        exclude = ['fecha', 'ruta','combi', 'estado', 'pasajeros', 'insumo', 'comentarios', 'precio', 'asientos_ocupados']

class ComentarioFilter(django_filters.FilterSet):
    """Filtro para comentarios"""
    class Meta:
        model = Comentario
        fields = '__all__'
        exclude = ['usuario', 'comentario']