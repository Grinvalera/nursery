from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email']

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)
# Register your models here.
