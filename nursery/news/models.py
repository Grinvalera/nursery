from django.db import models


class Tiding(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    title = models.TextField(blank=False, null=False)
    created = models.DateField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# Create your models here.
