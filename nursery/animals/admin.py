from django.contrib import admin
from .models import *


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'create', 'picture']

    class Meta:
        model = Description


admin.site.register(Description, DescriptionAdmin)
# Register your models here.
