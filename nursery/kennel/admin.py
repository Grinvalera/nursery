from django.contrib import admin
from .models import Title, PictureCarousel, RightPictureSide, LeftPictureSide


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created']

    class Meta:
        model = Title


class LeftPictureSideAdmin(admin.ModelAdmin):
    list_display = ['left_image']

    class Meta:
        model = LeftPictureSide


class PictureCarouselAdmin(admin.ModelAdmin):
    list_display = ['picture']

    class Meta:
        model = PictureCarousel


class RightPictureSideAdmin(admin.ModelAdmin):
    list_display = ['right_image']

    class Meta:
        model = RightPictureSide


admin.site.register(PictureCarousel, PictureCarouselAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(LeftPictureSide, LeftPictureSideAdmin)
admin.site.register(RightPictureSide, RightPictureSideAdmin)
# Register your models here.
