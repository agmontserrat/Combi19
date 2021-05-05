from django.shortcuts import render, HttpResponse

# Aca creamos nuestras vistas.
def home (request):
    return render(request, "Combi19App/home.html")

def pasajes (request):
    return render(request, "Combi19App/pasajes.html")

def insumos (request):
    return render(request, "Combi19App/insumos.html")

def registro (request):
    return render(request, "Combi19App/registro.html")

def index (request):
    return render(request, "Combi19App/index.html")

