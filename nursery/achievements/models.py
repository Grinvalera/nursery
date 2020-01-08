from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=128)
    title = models.TextField(null=False, blank=False)
    created = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Picture(models.Model):
    index = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    image = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.index}'

    class Meta:
        verbose_name = 'Фотография достяжения'
        verbose_name_plural = 'Фотографии достяжений'

# Create your models here.
