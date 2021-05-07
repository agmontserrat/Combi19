from django.urls import path
from Combi19App import views
from users import views as UserViews

urlpatterns = [
    path('', views.home, name="Home"),
    path('insumos', views.insumos, name="Insumos"),
    path('pasajes', views.pasajes, name="Pasajes"),
    path('registro', views.registro, name="Registro"),
    path('index', views.index, name="Index"),
]