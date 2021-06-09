from django import template
from decimal import Decimal
register = template.Library()

@register.filter(name='porcentaje')
def porcentaje(value, arg):
    precio = int(value)
    porcentaje =  int(value) * arg
    return (precio - porcentaje)

@register.filter(name='restar')
def restar(value, arg):
    return value - arg