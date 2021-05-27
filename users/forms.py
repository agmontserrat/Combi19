from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from datetime import date

from django.db.models import fields
from users.models import Account

from django import forms


class RegistrationForm(UserCreationForm):
    email          = forms.EmailField(max_length=225, help_text="Requerido. Añadí una dirección de email válida.")
    first_name     = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    last_name      = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    date_of_birth  = forms.DateField()


    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'dni', 'date_of_birth')

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        today = date.today()
        if (date_of_birth) > (today):
            raise forms.ValidationError('No naciste en el futuro! Ingresá una fecha válida.')
        if (date_of_birth.year + 18, date_of_birth.month, date_of_birth.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Debes ser mayor de 18 años para registrarte en COMBI-19.')
        
        return date_of_birth
    
    def clean_dni(self):
        dni = self.cleaned_data['dni']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(dni=dni)
        except Account.DoesNotExist:
            return dni
        raise forms.ValidationError(f"Ya existe una cuenta con el DNI {dni}. Olvidaste tu contraseña?")

    def clean_email(self):
        '''Recibe un email y lo valida.'''
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f"El email {email} ya está en uso! Probá con otro.")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    
    class Meta:
        model = Account
        fields = ("email", "password")
   
    def clean(self):
        '''Define el error que debe ser mostrado'''
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Inicio de sesión inválido.")

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ("email", "password")
    
    
