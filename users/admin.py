from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from users.models import Account


class AccountAdmin(UserAdmin):

    model = Account

    list_display = ('email','first_name', 'last_name', 'is_GOLD',  'is_admin', 'is_staff')
    list_filter = ('is_admin','is_GOLD', 'is_staff')
    search_fields = ('email', 'is_staff', 'is_GOLD')
    readonly_fields = ('id', 'last_login')
    
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('last_login', 'first_name', 'last_name', 'date_of_birth','dni',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'dni', 'password1', 'password2',),
        }),
    )
    
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_GOLD',)
    fieldsets = ()


admin.site.register(Account, AccountAdmin)