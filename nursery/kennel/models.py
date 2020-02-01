from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=64, null=True, blank=False)
    title = models.TextField()
    created = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Описание питомника'


class LeftPictureSide(models.Model):
    left_image = models.ImageField(upload_to='side_image/')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Левая боковая картинка'
        verbose_name_plural = 'Левые боковые картинки'


class RightPictureSide(models.Model):
    right_image = models.ImageField(upload_to='side_image/')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Правая боковая картинка'
        verbose_name_plural = 'Правые боковые картинки'


class PictureCarousel(models.Model):
    picture = models.ImageField(upload_to='carousel_image/')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Картинка для карусели'
        verbose_name_plural = 'Картинки для карусели'


