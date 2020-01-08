from django.contrib import admin
from .models import *


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'create']

    class Meta:
        model = Description


admin.site.register(Description, DescriptionAdmin)
admin.site.register(Picture)
# Register your models here.
