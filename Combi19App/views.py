from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Home")

def pasajes (request):
    return HttpResponse("Pasajes")

def insumos (request):
    return HttpResponse("Insumos")
