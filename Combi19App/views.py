from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required



# Aca creamos nuestras vistas.
@login_required
def home (request):
    return render(request, "Combi19App/home.html")

@login_required
def pasajes (request):
    return render(request, "Combi19App/pasajes.html")

@login_required
def insumos (request):
    return render(request, "Combi19App/insumos.html")


def index (request):
    if request.user.is_authenticated:
        return render(request, "Combi19App/home.html")
    return render(request, "Combi19App/index.html")

