from django.contrib import admin
from .models import *


class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created']

    class Meta:
        model = Achievement


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Picture)


# Register your models here.
