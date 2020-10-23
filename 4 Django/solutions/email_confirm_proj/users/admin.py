from django.contrib import admin


from .models import User, EmailConfirmation
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Email Address Confirmed',
            {
                'fields': (
                    'email_address_confirmed',
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)


class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'date_created', 'date_confirmed')
admin.site.register(EmailConfirmation, EmailConfirmationAdmin)

