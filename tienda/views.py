from users.models import Tarjeta
from Combi19App.models import Viaje, Pasaje
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from Combi19App.filters import ViajeFilter
from django.db.models import F
from .models import Insumo

from Combi19App.forms import CompraPasajeForm

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


    
    if request.POST:
        form = CompraPasajeForm(request.POST)
        if form.is_valid():
            ocupados = int(form.cleaned_data.get('asientos_ocupados'))
            viaje.asientos_ocupados= F('asientos_ocupados') + ocupados
            viaje.pasajeros.add(request.user)
            viaje.save()
            viaje.refresh_from_db()
            
            p = Pasaje(viaje=viaje, usuario=request.user)
            p.save()
        return redirect("Compra Exitosa")
    
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

@login_required
def tienda (request):
    insumos = Insumo.objects.all()
    return render(request, "tienda/insumos.html", {"insumos": insumos})

@login_required
def comprar_insumos(request, *args, **kwargs):
    tarjetas_usuario = Tarjeta.objects.filter(usuario_id=request.user.id)
    if not tarjetas_usuario:
        return redirect("Tarjetas")

    carrito = request.session['carro']
    viajes = Viaje.objects.filter(pasajeros=request.user).filter(estado=Viaje.comenzado)
    context = {"viajes":viajes}

    if request.POST:
        d = dict(carrito.items())
        for each in d.values():
            insumo = Insumo.objects.get(id=each["insumo_id"])
            insumo.restar_insumo(each["cantidad"])
            insumo.save()
            return redirect("Insumo Exitoso")


    return render(request, "tienda/detalle_insumo.html", context)
