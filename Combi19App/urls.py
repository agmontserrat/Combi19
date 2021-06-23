from django.urls import path
from Combi19App import views
from users import views as UserViews

urlpatterns = [
    path('home', views.home, name="Home"),
    path('nosotros', views.about, name ="About"),
    path('pasajes', views.pasajes, name="Pasajes"),
    path('contacto', views.contacto, name="Contacto"),

    path('suscripcion', views.suscripcion, name="Suscripcion"),
    path('suscripcion/gold', views.suscripcion_gold_exito, name="GOLD"),
    path('suscripcion/cancelargold', views.suscripcion_gold_chau, name="NO-GOLD"),

    path('exito', views.compra_exitosa, name="Compra Exitosa"),

    path('reseñas', views.reseñas, name="Reseñas"),
    path ('reseñas/eliminar<c_id>', views.delete_comentario, name = "Eliminar Comentario"),
    path ('reseñas/editar<c_id>', views.modificar_comentario, name = "Editar Comentario"),

    path('tienda/exito', views.insumo_exitoso, name="Insumo Exitoso"),
    path ('pasajes/comprar<v_id>', views.comprar_pasaje, name = "Comprar Pasaje"),
    path('', views.index, name="Index")
    
]