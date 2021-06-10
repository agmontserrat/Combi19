from django.urls import path
from .import views

app_name="carro"

urlpatterns = [
    # path('', views.home, name="Home"),
    # path('', views.about, name ="About"),
    # path('', views.tienda, name="Insumos"),
    # path('', views.pasajes, name="Pasajes"),
    # path('', views.contacto, name="Contacto"),
    # path('', views.suscripcion, name="Suscripcion"),
    # path('', views.comprar_pasaje, name = "Comprar Pasaje"),
    path('agregar/<int:insumo_id>', views.agregar_insumo, name="agregar"),
    path('eliminar/<int:insumo_id>', views.eliminar_insumo, name="eliminar"),
    path('restar/<int:insumo_id>', views.restar_insumo, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),

]