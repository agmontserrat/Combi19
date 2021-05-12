from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin.widgets import FilteredSelectMultiple


from users.models import Account, Chofer


class AccountAdmin(UserAdmin):

    model = Account

    list_display = ('email','first_name', 'last_name', 'is_GOLD',  'is_admin', 'is_staff')
    list_filter = ('is_admin','is_GOLD', 'is_staff')
    search_fields = ('email', 'is_staff', 'is_GOLD')
    readonly_fields = ('id', 'last_login')
    
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('last_login', 'first_name', 'last_name', 'date_of_birth','dni',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'dni', 'password1', 'password2', 'is_staff'),
        }),
    )

    
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_GOLD',)
    
    # def get_fieldsets(self, request, obj=None):
    #     if not request.user.is_superuser:
    #         return [(None, {'fields': ('your_editable_fields',)}),]
    #     else:
    #         return self.fieldsets


class ChoferAdmin (UserAdmin):
    model = Chofer

    list_display = ('email','first_name', 'last_name', 'is_staff')
    list_filter = ('is_admin', 'is_staff')
    search_fields = ('email', 'dni', 'is_active')
    readonly_fields = ('id', 'last_login')
    
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('last_login', 'first_name', 'last_name', 'date_of_birth','dni', 'contacto', 'combi')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'dni','contacto' ,'combi','password1', 'password2',),
        }),
    )

    
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    

admin.site.register(Chofer, ChoferAdmin)
admin.site.register(Account, AccountAdmin)