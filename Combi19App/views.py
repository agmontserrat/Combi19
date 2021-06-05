from Combi19App.models import Insumo, Viaje
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .filters import ViajeFilter


# Aca creamos nuestras vistas.
@login_required
def home (request):
    return render(request, "Combi19App/home.html")

@login_required
def pasajes (request):
    viajes = Viaje.objects.all()

    miFiltro = ViajeFilter(request.GET, queryset=viajes)

    viajes = miFiltro.qs

    context = {"viajes": viajes, 'miFiltro': miFiltro}
    return render(request, "Combi19App/pasajes.html", context)

@login_required
def insumos (request):
    insumos = Insumo.objects.all()
    return render(request, "Combi19App/insumos.html", {"insumos": insumos})

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