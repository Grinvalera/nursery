# Generated by Django 3.0.2 on 2020-01-14 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_delete_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(upload_to='animals_image/'),
        ),
    ]
