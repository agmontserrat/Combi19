from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from datetime import date
from users.models import Account, Chofer, Tarjeta
from users.forms import RegistrationForm

class AccountAdmin(UserAdmin):
    model = Account
    form = RegistrationForm

    list_display = ('email','first_name', 'last_name', 'is_GOLD',)
    list_filter = ('is_admin','is_GOLD', 'is_staff')
    search_fields = ('email', 'is_GOLD')
    readonly_fields = ('id', 'last_login', 'reactivar')
    
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('last_login', 'first_name', 'last_name', 'date_of_birth','dni','reactivar')}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_GOLD')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'dni', 'password1', 'password2', 'is_GOLD', 'is_active'),
        }),
    )

    
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_GOLD', 'is_staff', )

    def get_form(self, request, obj=None, **kwargs):
        form = super(AccountAdmin,self).get_form(request, obj, **kwargs)
        return form

class TarjetaAdmin(admin.ModelAdmin):
    readonly_fields=['usuario','nombre_titular','nro','cvv','fecha_vencimiento',]
    fields = ['usuario','nombre_titular','nro','fecha_vencimiento',]
    list_display=['usuario','nro']
    def has_add_permission(self, request):
        return False 
    def has_change_permission(self, request, obj=None):
        return False

class ChoferAdmin(admin.ModelAdmin):
    list_display=['user', 'telefono']

admin.site.unregister(Group)
admin.site.register(Chofer, ChoferAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(Account, AccountAdmin)