# Generated by Django 3.0.2 on 2020-02-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kennel', '0003_remove_leftpictureside_small_left_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='leftpictureside',
            name='picture',
            field=models.ImageField(default=0, upload_to='small_side_picture/'),
            preserve_default=False,
        ),
    ]
