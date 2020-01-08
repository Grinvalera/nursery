from django.contrib import admin
from .models import *


class TidingAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created']

    class Meta:
        model = Tiding


admin.site.register(Tiding, TidingAdmin)
# Register your models here.
