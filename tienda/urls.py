from django.urls import path
from .import views
from users import views as UserViews

urlpatterns = [
    path('home', views.home, name="Home"),
    path('nosotros', views.about, name ="About"),
    path('tienda', views.tienda, name="Insumos"),
    path('pasajes', views.pasajes, name="Pasajes"),
    path('contacto', views.contacto, name="Contacto"),
    path('suscripcion', views.suscripcion, name="Suscripcion"),
    path ('pasajes/comprar<v_id>', views.comprar_pasaje, name = "Comprar Pasaje"),
    path ('tienda/comprar', views.comprar_insumos, name = "Comprar Insumo"),
    path('', views.index, name="Index")
    
]