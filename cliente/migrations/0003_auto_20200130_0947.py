# Generated by Django 3.0 on 2020-01-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20200130_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='document1',
            field=models.FileField(blank=True, null=True, upload_to='cliente/', verbose_name='Documentación 1'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='document2',
            field=models.FileField(blank=True, null=True, upload_to='cliente/', verbose_name='Documentación 2'),
        ),
    ]
