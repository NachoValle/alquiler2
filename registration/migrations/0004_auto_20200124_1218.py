# Generated by Django 3.0 on 2020-01-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200123_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='superus',
        ),
        migrations.AddField(
            model_name='profile',
            name='p_vehiculos',
            field=models.BooleanField(default=False, verbose_name='Permiso Crear Vehiculos'),
        ),
    ]
