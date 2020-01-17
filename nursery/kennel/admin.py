from django.contrib import admin
from .models import Title, PictureCarousel


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created']

    class Meta:
        model = Title


class PictureCarouselAdmin(admin.ModelAdmin):
    list_display = ['picture']

    class Meta:
        model = PictureCarousel


admin.site.register(PictureCarousel, PictureCarouselAdmin)
admin.site.register(Title, TitleAdmin)
# Register your models here.
