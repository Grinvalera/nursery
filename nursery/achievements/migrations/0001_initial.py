# Generated by Django 3.0.2 on 2020-01-08 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=128)),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievements.Achievement')),
            ],
            options={
                'verbose_name': 'Фотография достяжения',
                'verbose_name_plural': 'Фотографии достяжений',
            },
        ),
    ]
