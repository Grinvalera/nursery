# Generated by Django 3.0.2 on 2020-02-01 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kennel', '0002_leftpictureside'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leftpictureside',
            name='small_left_picture',
        ),
    ]
