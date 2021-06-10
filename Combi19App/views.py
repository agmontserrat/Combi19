from users.models import Tarjeta
from Combi19App.models import Viaje
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .filters import ViajeFilter
from django.db.models import F

# Aca creamos nuestras vistas.
@login_required
def home (request):
    return render(request, "Combi19App/home.html")

@login_required
def pasajes (request):
    viajes = Viaje.objects.all().filter(asientos_ocupados__lt= F('combi__capacidad') )

    miFiltro = ViajeFilter(request.GET, queryset=viajes)

    viajes = miFiltro.qs

    context = {"viajes": viajes, 'miFiltro': miFiltro}
    return render(request, "Combi19App/pasajes.html", context)

@login_required
def comprar_pasaje(request, *args, **kwargs):
    viaje_id = kwargs.get("v_id")
    try: 
        viaje = Viaje.objects.get(pk = viaje_id)
    except:
        return HttpResponse("Hubo un error")

    try: 
        tarjetas_usuario = Tarjeta.objects.filter(usuario_id=request.user.id)
    except Exception as E: #No tenemos tarjetas
        return redirect("Tarjetas")
    
    if request.user.is_GOLD:
        precio = viaje.precio * 0.1
    else:
        precio = viaje.precio
        
    context = {"viaje": viaje, "tarjetas": tarjetas_usuario, "precio": precio}
    return render(request, "Combi19App/detalle_viaje.html", context)



@login_required
def contacto (request):
    return render(request, "Combi19App/contact.html")

@login_required
def about (request):
    return render(request, "Combi19App/about.html")
    
def index (request):
    if request.user.is_authenticated:
        return render(request, "Combi19App/home.html")
    return render(request, "Combi19App/index.html")

@login_required
def suscripcion (request):
    return render(request, "Combi19App/pricing.html")