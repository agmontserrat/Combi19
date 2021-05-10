from django.urls import path
from users import views


urlpatterns = [
    path ('register/', views.register_view, name = "Register"),
    path ('login/', views.login_view, name= "Login"),
    path ('logout/', views.logout_view, name = "Logout")
]