# Generated by Django 3.0 on 2020-01-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agencia',
            options={'ordering': ['ciudad']},
        ),
        migrations.AlterField(
            model_name='agencia',
            name='ciudad',
            field=models.CharField(max_length=50, unique=True, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='codigo_postal',
            field=models.FloatField(verbose_name='C.P.'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='direccion',
            field=models.CharField(max_length=200, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='email',
            field=models.EmailField(max_length=200, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='image',
            field=models.ImageField(upload_to='Ciudades', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='telefono_fijo',
            field=models.CharField(max_length=20, verbose_name='Teléfono Fijo'),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='telefono_movil',
            field=models.CharField(max_length=20, verbose_name='Teléfono Móvil'),
        ),
    ]
