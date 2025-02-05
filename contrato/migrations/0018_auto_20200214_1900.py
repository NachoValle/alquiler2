# Generated by Django 3.0 on 2020-02-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0017_contrato_adicional'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='precio_c1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio C1'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='precio_c2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio C2'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='precio_c3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio C3'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='precio_c4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio C4'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='precio_c5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio C5'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='precio_c6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Precio C6'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cantidad_c1',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Cantidad C1'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cantidad_c2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad C2'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cantidad_c3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad C3'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cantidad_c4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad C4'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cantidad_c5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad C5'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cantidad_c6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad C6'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='total_c1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Total C1'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='total_c2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total C2'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='total_c3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total C3'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='total_c4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total C4'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='total_c5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total C5'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='total_c6',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total C6'),
        ),
    ]
