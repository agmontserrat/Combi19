from django.urls import path
from Combi19App import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('insumos', views.insumos, name="Insumos"),
    path('pasajes', views.pasajes, name="Pasajes")
    
]