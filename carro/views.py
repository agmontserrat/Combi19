from django.shortcuts import render

from.carro import Carrito, Carro

from tienda.models import Insumo

from django.shortcuts import redirect

# Create your views here.

def agregar_insumo(request, insumo_id):
    
    carro=Carro(request)
    
    insumo=Insumo.objects.get(id=insumo_id)
    
    carro.agregar(insumo=insumo)
    
    return redirect("tienda")


def eliminar_insumo(request, insumo_id):
    
    carro=Carro(request)
    
    insumo=Insumo.objects.get(id=insumo_id)
    
    carro.eliminar(insumo=insumo)
    
    return redirect("tienda")

def restar_insumo(request, insumo_id):
    
    carro=Carro(request)
    
    insumo=Insumo.objects.get(id=insumo_id)
    
    carro.restar_producto(insumo=insumo)
    
    return redirect("tienda")


def limpiar_carrito(request):
    
    carro=Carro(request)
    
    carro.limpiar_carro()
    
    return redirect("tienda")