# Generated by Django 3.0 on 2020-01-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0002_auto_20200113_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencia',
            name='codigo',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Codigo Oficina'),
        ),
    ]
