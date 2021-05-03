from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=225, help_text="Requerido. Añadí una dirección de email válida.")
    first_name = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    last_name = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2', 'dni', 'date_of_birth')

    def clean_email(self):
        '''Función que valida el email'''
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.get(email=email) #Pido que me de la fila si existe la cuenta
        except Exception as e:
            raise 
        raise forms.ValidationError(f"El email {email} ya está en uso.")
