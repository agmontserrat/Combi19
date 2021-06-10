from django.urls import path
from users import views


urlpatterns = [
    path ('register/', views.register_view, name = "Register"),
    path ('login/', views.login_view, name= "Login"),
    path ('logout/', views.logout_view, name = "Logout"),
    path ('profile/', views.profile_view, name = "Profile"),
    path ('profile/edit', views.editprofile_view, name = "EditProfile"),
    path ('viajes/', views.misviajes_view, name = "Viajes"),
    path ('tarjetas', views.mistarjetas_view, name = "Tarjetas"),
    path ('tarjetas/agregar', views.tarjeta_view, name = "Nueva Tarjeta"),
    path ('tarjetas/editar<tarjeta_id>', views.edit_tarjeta_view, name = "Editar Tarjeta"),
    path ('tarjetas/eliminar<tarjeta_id>', views.delete_tarjeta_view, name = "Eliminar Tarjeta"),
    path ('viajes/eliminar<v_id>', views.delete_viaje, name = "Eliminar Viaje"),
]
