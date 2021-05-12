from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from datetime import date
from users.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=225, help_text="Requerido. Añadí una dirección de email válida.")
    first_name = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    last_name = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    # dni = forms.NumberInput(help_text="Requerido. Añadí tu DNI.")
    # dni = forms.NumberInput()
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'dni', 'date_of_birth')

    def clean_date_of_birth(self):
        fecha = self.cleaned_data['date_of_birth']
        today = date.today()
        if (fecha.year + 18, fecha.month, fecha.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Debes ser mayor de 18 años para registrarte en COMBI-19')
        return fecha

    def clean_email(self):
        '''Recibe un email y lo valida.'''
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f"El email {email} ya está en uso")


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ("email", "password")
    
    # def save(self):
    #     email = self.cleaned_data['email']
    #     password = self.cleaned_data['password']
    #     user = authenticate(email=email, password=password)
    #     if user: 
    #         login(request, user)
   
    def clean(self):
        '''Define el error que debe ser mostrado'''
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Inicio de sesión inválido.")