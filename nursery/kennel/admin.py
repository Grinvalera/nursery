from django.contrib import admin
from .models import Title


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created']

    class Meta:
        model = Title


admin.site.register(Title, TitleAdmin)
# Register your models here.
