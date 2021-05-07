from django.urls import path
from Combi19App import views

urlpatterns = [
    path('home', views.home, name="Home"),
    path('insumos', views.insumos, name="Insumos"),
    path('pasajes', views.pasajes, name="Pasajes"),
    path('registro', views.registro, name="Registro"),
    path('', views.index, name="Index")
    
]