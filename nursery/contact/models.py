from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name, self.last_name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
# Create your models here.
