# Generated by Django 3.0 on 2020-02-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0021_auto_20200217_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='vehiculo',
            field=models.CharField(max_length=210, verbose_name='Vehículo'),
        ),
    ]
