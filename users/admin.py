from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from users.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'dni','last_login', 'first_name', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('id', 'last_login')
    
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('last_login', 'first_name', 'last_name', 'date_of_birth','dni',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'dni', 'password1', 'password2'),
        }),
    )
    list_filter = ('is_admin',)
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)