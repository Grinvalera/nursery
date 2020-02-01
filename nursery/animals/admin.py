from django.contrib import admin
from .models import *


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['name', 'create', 'picture']

    class Meta:
        model = Description


class OurAnimalAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = OurAnimal


admin.site.register(OurAnimal, OurAnimalAdmin)
admin.site.register(Description, DescriptionAdmin)
# Register your models here.
