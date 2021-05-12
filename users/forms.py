from users.admin import AccountAdmin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from datetime import date
from users.models import Account

from django import VERSION, forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

class RegistrationForm(UserCreationForm):
    email          = forms.EmailField(max_length=225, help_text="Requerido. Añadí una dirección de email válida.")
    first_name     = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    last_name      = forms.CharField(max_length=30, help_text="Requerido. Añadí tu nombre.")
    date_of_birth  = forms.DateField()
    # dni = forms.NumberInput(help_text="Requerido. Añadí tu DNI.")
    # dni = forms.NumberInput()
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', 'dni', 'date_of_birth')

    def clean_date_of_birth(self):
        fecha = self.cleaned_data['date_of_birth']
        today = date.today()
        if (fecha) > (today):
            raise forms.ValidationError('No naciste en el futuro! Ingresá una fecha válida.')
        if (fecha.year + 18, fecha.month, fecha.day) > (today.year, today.month, today.day):
            raise forms.ValidationError('Debes ser mayor de 18 años para registrarte en COMBI-19.')
        
        return fecha
    
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
    # remember_me = forms.BooleanField()
  
    
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

# Create ModelForm based on the Group model.
# class GroupAdminForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         exclude = []

#     # Add the users field.
#     users = forms.ModelMultipleChoiceField(
#         queryset=Account.objects.all(),
#         required=False,
#         # Use the pretty 'filter_horizontal widget'.
#         widget=FilteredSelectMultiple('users', False),
#         label=_('Users'),
#     )

#     def __init__(self, *args, **kwargs):
#         # Do the normal form initialisation.
#         super(GroupAdminForm, self).__init__(*args, **kwargs)
#         # If it is an existing group (saved objects have a pk).
#         if self.instance.pk:
#             # Populate the users field with the current Group users.
#             self.fields['users'].initial = self.instance.user_set.all()

#     def save_m2m(self):
#         # Add the users to the Group.
#         # Deprecated in Django 1.10: Direct assignment to a reverse foreign key
#         #                            or many-to-many relation
#         if VERSION < (1, 9):
#             self.instance.user_set = self.cleaned_data['users']
#         else:
#             self.instance.user_set.set(self.cleaned_data['users'])

#     def save(self, *args, **kwargs):
#         # Default save
#         instance = super(GroupAdminForm, self).save()
#         # Save many-to-many data
#         self.save_m2m()
#         return instance