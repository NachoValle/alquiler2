# Generated by Django 3.0 on 2020-03-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0026_contrato_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='km_extra',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True, verbose_name='Km Extra'),
        ),
    ]
