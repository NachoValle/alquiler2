# Generated by Django 3.0 on 2020-03-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0003_agencia_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencia',
            name='condiciones',
            field=models.TextField(blank=True, null=True, verbose_name='Condiciones contrato'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Ciudades', verbose_name='Avatar'),
        ),
    ]
