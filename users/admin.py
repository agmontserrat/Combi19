from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from datetime import date
from users.models import Account, Chofer
from users.forms import RegistrationForm

class AccountAdmin(UserAdmin):
    model = Account
    form = RegistrationForm

    list_display = ('email','first_name', 'last_name', 'is_GOLD',)
    list_filter = ('is_admin','is_GOLD', 'is_staff')
    search_fields = ('email', 'is_GOLD')
    readonly_fields = ('id', 'last_login')
    
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('last_login', 'first_name', 'last_name', 'date_of_birth','dni',)}),
        ('Permissions', {'fields': ('is_active','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'dni', 'password1', 'password2'),
        }),
    )

    
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_GOLD',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(AccountAdmin,self).get_form(request, obj, **kwargs)
        return form

    

admin.site.unregister(Group)
admin.site.register(Chofer)
admin.site.register(Account, AccountAdmin)