# Generated by Django 3.0 on 2020-01-29 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('negra', models.BooleanField(default=False, verbose_name='Lista Negra')),
                ('tipo', models.CharField(choices=[('nif', 'N.I.F.'), ('passport', 'Pasaporte'), ('cif', 'C.I.F.')], max_length=20, verbose_name='Tipo de documentación')),
                ('n_id', models.CharField(max_length=110, verbose_name='Nº Identificación')),
                ('f_exp_id', models.DateField(blank=True, null=True, verbose_name='Fecha expedición ID')),
                ('apellido', models.CharField(blank=True, max_length=110, null=True, verbose_name='Apellidos')),
                ('nombre', models.CharField(max_length=110, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=210, null=True, verbose_name='Dirección')),
                ('poblacion', models.CharField(blank=True, max_length=110, null=True, verbose_name='Población')),
                ('provincia', models.CharField(blank=True, max_length=110, null=True, verbose_name='Provincia')),
                ('pais', models.CharField(blank=True, max_length=110, null=True, verbose_name='País')),
                ('telefono', models.CharField(blank=True, max_length=110, null=True, verbose_name='Movil')),
                ('movil', models.CharField(blank=True, max_length=110, null=True, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=210, null=True, verbose_name='Email')),
                ('f_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento')),
                ('l_nacimiento', models.CharField(blank=True, max_length=210, null=True, verbose_name='Lugar de nacimiento')),
                ('licencia', models.CharField(blank=True, max_length=210, null=True, verbose_name='Nº de licéncia')),
                ('l_exp', models.CharField(blank=True, max_length=210, null=True, verbose_name='Lugar expedición')),
                ('f_exp', models.DateField(blank=True, null=True, verbose_name='Fecha expedicion')),
                ('f_caducidad', models.DateField(blank=True, null=True, verbose_name='Fecha caducidad')),
                ('trabajo', models.CharField(blank=True, max_length=210, null=True, verbose_name='Lugar expedición')),
                ('obs', models.CharField(blank=True, max_length=210, null=True, verbose_name='Observaciones')),
                ('banco', models.CharField(blank=True, max_length=210, null=True, verbose_name='Datos bancarios')),
                ('tarjeta', models.CharField(blank=True, max_length=210, null=True, verbose_name='Nº Tarjeta')),
                ('f_tarjeta', models.CharField(blank=True, max_length=5, null=True, verbose_name='Fecha caducidad tarjeta')),
            ],
            options={
                'ordering': ['n_id', 'apellido'],
                'unique_together': {('n_id',)},
            },
        ),
    ]
