from django.urls import path
from Combi19App import views
from users import views as UserViews

urlpatterns = [
    path('home', views.home, name="Home"),
    path('nosotros', views.about, name ="About"),
    path('insumos', views.insumos, name="Insumos"),
    path('pasajes', views.pasajes, name="Pasajes"),
    path('contacto', views.contacto, name="Contacto"),
    path('', views.index, name="Index")
    
]