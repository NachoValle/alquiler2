# Generated by Django 3.0 on 2020-01-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='odo',
            field=models.PositiveIntegerField(null=True, verbose_name='Odometro'),
        ),
    ]
