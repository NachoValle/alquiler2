# Generated by Django 3.0 on 2020-01-14 11:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agencia', '0002_auto_20200113_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='Activado')),
                ('tipo', models.CharField(choices=[('TU', 'Turismo'), ('FU', 'Carga')], max_length=20)),
                ('placa', models.CharField(max_length=10, unique=True, verbose_name='Matrícula')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo')),
                ('combustible', models.CharField(choices=[('GAS', 'Gasolina'), ('DSL', 'Diesel'), ('HIB', 'Hibrido'), ('GPL', 'GPL')], max_length=20, verbose_name='Combustible')),
                ('color', models.CharField(choices=[('RO', 'Rojo'), ('NE', 'Negro'), ('BA', 'Blanco'), ('GC', 'Gris Claro'), ('GO', 'Gris Oscuro'), ('AZ', 'Azul'), ('AM', 'Amarillo'), ('NA', 'Naranja'), ('OT', 'Otro')], max_length=20)),
                ('bastidor', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_matricula', models.DateField(default=datetime.date.today, max_length=200, verbose_name='Año matriculación')),
                ('itv', models.DateField(default=datetime.date.today, verbose_name='I.T.V.')),
                ('image', models.ImageField(upload_to='vehiculos', verbose_name='Foto')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agencia.Agencia')),
            ],
            options={
                'ordering': ['itv'],
            },
        ),
    ]
