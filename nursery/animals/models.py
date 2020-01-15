from django.db import models


class Description(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=False, null=False)
    picture = models.ImageField(upload_to='animals_image/')
    create = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'

# Create your models here.
