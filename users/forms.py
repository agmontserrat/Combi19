from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from datetime import date
from django.http import request
from users.models import Account, Tarjeta

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
        fields = ("email", "first_name", "last_name", "date_of_birth", "dni")

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email = email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f"El email {email} ya está en uso.")
        
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        today = date.today()
        if not date_of_birth:
            raise forms.ValidationError("No hay fecha")
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

    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.first_name= self.cleaned_data['first_name']
        account.last_name= self.cleaned_data['last_name']  
        account.date_of_birth = self.cleaned_data['date_of_birth']      
        account.dni = self.cleaned_data['dni']
        account.email = self.cleaned_data['email']
        if commit:
            account.save()
        return account

class AddCardForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ("nro", "nombre_titular", "cvv", "fecha_vencimiento")

    def clean_nro(self):
        nro = str(self.cleaned_data['nro'])
        if len(nro) != 16:
            raise forms.ValidationError("Las tarjetas necesitan un número de 16 digitos.")
        return nro
    
    def clean_nombre_titular(self):
        nombre_titular = self.cleaned_data['nombre_titular']
        if any(char.isdigit() for char in nombre_titular):
            raise forms.ValidationError("El nombre no puede contener dígitos.")
        return nombre_titular

    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data['fecha_vencimiento']
        return fecha

    def save(self, commit=True):
        tarjeta = Tarjeta()
        tarjeta.usuario = self.instance
        tarjeta.nombre_titular= self.cleaned_data['nombre_titular']  
        tarjeta.nro= self.cleaned_data['nro']  
        tarjeta.fecha_vencimiento = self.cleaned_data['fecha_vencimiento']  
        tarjeta.cvv = self.cleaned_data['cvv']
        if commit:
            tarjeta.save()
        return tarjeta
    
class EditCardForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ("nro", "nombre_titular", "cvv", "fecha_vencimiento")

    def clean_nro(self):
        nro = str(self.cleaned_data['nro'])
        if len(nro) != 16:
            raise forms.ValidationError("Las tarjetas necesitan un número de 16 digitos.")
        return nro
    
    def clean_nombre_titular(self):
        nombre_titular = self.cleaned_data['nombre_titular']
        if any(char.isdigit() for char in nombre_titular):
            raise forms.ValidationError("El nombre no puede contener dígitos.")
        return nombre_titular

    def clean_fecha_vencimiento(self):
        fecha = self.cleaned_data['fecha_vencimiento']
        return fecha

    def save(self, user=None, commit=True):
        tarjeta = super(EditCardForm, self).save(commit=False)
        tarjeta.usuario = user
        tarjeta.nombre_titular= self.cleaned_data['nombre_titular']  
        tarjeta.nro= self.cleaned_data['nro']  
        tarjeta.fecha_vencimiento = self.cleaned_data['fecha_vencimiento']  
        tarjeta.cvv = self.cleaned_data['cvv']
        if commit:
            tarjeta.save()
        return tarjeta