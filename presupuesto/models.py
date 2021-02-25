from django.db import models
from vehiculo.models import Vehiculo
from cliente.models import Cliente
from django.contrib.auth.models import User
from agencia.models import Agencia
from contrato.models import ConceptoAlquiler

# Create your models here.
class Presupuesto(models.Model):
    km_ilimitado = models.BooleanField(default= False , verbose_name='Km Ilimitados')
    h_contrato = models.TimeField(auto_now=True,verbose_name='Hora')
    f_contrato = models.DateField(auto_now=True,verbose_name='Fecha')
   
    concepto1 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,verbose_name='Concepto 1', related_name='pConcepto_1')
    concepto2= models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 2', related_name='pConcepto_2')
    concepto3 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 3', related_name='pConcepto_3')
    concepto4 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 4', related_name='pConcepto_4')
   
    cantidad_c1 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C1',default=1)
    cantidad_c2 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C2',null=True, blank=True)
    cantidad_c3 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C3',null=True, blank=True)
    cantidad_c4 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C4',null=True, blank=True)

    precio_c1 = models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Precio C1',)
    precio_c2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C2')
    precio_c3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C3')
    precio_c4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C4')

    total_c1 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Total C1',)
    total_c2 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C2')
    total_c3 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C3')
    total_c4 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C4')

    total = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Total Contrato',null=True, blank=True,)

    fianza = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Fianza',null=True, blank=True,)
    franquicia = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Franquicia',null=True, blank=True,)
    pago_tarjeta = models.BooleanField(default= False,verbose_name='Pago Tarjeta') 
     
    fianza_tarjeta = models.BooleanField(default= False,verbose_name='Fianza Tarjeta') 

    entregado = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='entregado',null=True, blank=True,)
    reservado = models.BooleanField(default= False,verbose_name='reservado')
    oficina = models.CharField(max_length=50,verbose_name='Oficina',null=True, blank=True)
    ciudad_recogida = models.CharField(max_length=50,verbose_name='Ciudad recogida',null=True, blank=True)
    ciudad_devolucion = models.CharField(max_length=50,verbose_name='Ciudad devoluvion',null=True, blank=True)
    h_inicio = models.TimeField(verbose_name='Hora inicio',null=True, blank=True)
    f_inicio = models.DateField(verbose_name='Fecha inicio',null=True, blank=True)
    h_fin = models.TimeField(verbose_name='Hora finalización',null=True, blank=True)
    f_fin = models.DateField(verbose_name='Fecha finalización',null=True, blank=True)
    km_libres = models.PositiveIntegerField(verbose_name='KM libres',default=0)

    cliente = models.CharField(max_length=110,verbose_name='Cliente')
    id_cliente = models.PositiveIntegerField(verbose_name='Id Cliente',default=0)
    c_apellido = models.CharField(max_length=110,  verbose_name='Apellidos',blank=True,null=True)
    c_nombre = models.CharField(max_length=110,  verbose_name='Nombre',blank=True,null=True)
    c_direccion = models.CharField(max_length=210,  verbose_name='Dirección',blank=True,null=True)
    c_poblacion = models.CharField(max_length=110,  verbose_name='Población',blank=True,null=True)
    c_provincia = models.CharField(max_length=110,  verbose_name='Provincia',blank=True,null=True)
    c_cp = models.CharField(max_length=10,  verbose_name='C.P.',blank=True,null=True)
    c_pais = models.CharField(max_length=110,  verbose_name='País',blank=True,null=True)
    c_telefono = models.CharField(max_length=110,  verbose_name='Movil',blank=True,null=True)
    c_movil = models.CharField(max_length=110,  verbose_name='Teléfono',blank=True,null=True)

    marca = models.CharField(max_length=30,verbose_name='Marca',default='')
    modelo = models.CharField(max_length=30, verbose_name='Modelo',default='') 
    t_combustible = models.CharField(max_length=30, verbose_name='Tipo Combustible',default='')
    color = models.CharField(max_length=20, verbose_name='Color', default='')
    id_vehiculo = models.PositiveIntegerField(verbose_name='Id Vehiculo')
    vehiculo = models.CharField(max_length=210,verbose_name='Vehículo')
    km_extra = models.CharField(max_length=20,verbose_name='Km Extra',null=True, blank=True)
    empleado = models.CharField(max_length=30,verbose_name='Empleado',null=True, blank=True)
