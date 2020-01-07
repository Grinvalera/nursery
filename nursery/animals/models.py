from django.db import models


class Description(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=False, null=False)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'


class Picture(models.Model):
    product = models.ForeignKey(Description, on_delete=models.CASCADE)
    picture = models.CharField(max_length=128)
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.picture}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

# Create your models here.
