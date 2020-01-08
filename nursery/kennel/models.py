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
# Create your models here.
