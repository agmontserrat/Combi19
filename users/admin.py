from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ('id', 'last_login')

    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)