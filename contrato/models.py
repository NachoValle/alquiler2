from django.db import models
from vehiculo.models import Vehiculo
from cliente.models import Cliente
from django.contrib.auth.models import User
from agencia.models import Agencia


# Create your models here.


FUEL = (        
        ('F', 'F'),
        ('7/8', '7/8'),
        ('3/4', '3/4'),
        ('5/8', '5/8'),
        ('1/2', '1/2'),
        ('3/8', '3/8'),
        ('1/4', '1/4'),
        ('1/8', '1/8'),
        ('E', 'E'),
    )

class ConceptoAlquiler(models.Model):
    concepto = models.CharField(max_length=50,  verbose_name='Concepto')
    def __str__(self):
        return self.concepto

class Contrato(models.Model):
    alquilado =  models.BooleanField(default= True,verbose_name='Alquilado')
    cancelado =  models.BooleanField(default= False,verbose_name='Cancelado')
    cortesia =  models.BooleanField(default= False,verbose_name='Cortesia')
    sustitucion =  models.BooleanField(default= False , verbose_name='Sustitución')
    adicional =  models.BooleanField(default= False , verbose_name='Sustitución')
    km_ilimitado = models.BooleanField(default= False , verbose_name='Km Ilimitados')
   
    h_contrato = models.TimeField(auto_now=True,verbose_name='Hora')
    f_contrato = models.DateField(auto_now=True,verbose_name='Fecha')
    observacion = models.CharField(max_length=50,verbose_name='Observaciones',null=True, blank=True)

    concepto1 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,verbose_name='Concepto 1', related_name='Concepto_1')
    concepto2= models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 2', related_name='Concepto_2')
    concepto3 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 3', related_name='Concepto_3')
    concepto4 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 4', related_name='Concepto_4')
    concepto5 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 5', related_name='Concepto_5')
    concepto6 = models.ForeignKey(ConceptoAlquiler,on_delete=models.PROTECT,null= True, blank= True,verbose_name='Concepto 6', related_name='Concepto_6')
    
    cantidad_c1 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C1',default=1)
    cantidad_c2 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C2',null=True, blank=True)
    cantidad_c3 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C3',null=True, blank=True)
    cantidad_c4 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C4',null=True, blank=True)
    cantidad_c5 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C5',null=True, blank=True)
    cantidad_c6 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad C6',null=True, blank=True)
    
    precio_c1 = models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Precio C1',)
    precio_c2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C2')
    precio_c3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C3')
    precio_c4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C4')
    precio_c5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C5')
    precio_c6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='Precio C6')
   
    total_c1 = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Total C1',)
    total_c2 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C2')
    total_c3 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C3')
    total_c4 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C4')
    total_c5 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C5')
    total_c6 = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True,verbose_name='Total C6')
    
    total = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Total Contrato',null=True, blank=True,)
    
    fianza = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Fianza',null=True, blank=True,)
    franquicia = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Franquicia',null=True, blank=True,)
    pago_tarjeta = models.BooleanField(default= False,verbose_name='Pago Tarjeta') 
    fianza_deposito = models.BooleanField(default= False,verbose_name="Fianza en depósito") 
    fianza_tarjeta = models.BooleanField(default= False,verbose_name='Fianza Tarjeta') 
    combustible = models.CharField(max_length=4,choices=FUEL,blank=False, default=1)

    oficina = models.CharField(max_length=50,verbose_name='Oficina',null=True, blank=True)
    c_madrid = models.PositiveIntegerField(verbose_name='Nº Madrid',null=True, blank=True)
    b_madrid = models.BooleanField(default= False,verbose_name='Contabilizar Madrid')
    c_salamanca = models.PositiveIntegerField(verbose_name='Nº Salamanca',null=True, blank=True)
    b_salamanca = models.BooleanField(default= False,verbose_name='Contabilizar Salamanca')
    c_valladolid = models.PositiveIntegerField(verbose_name='Nº Valladolid',null=True, blank=True)
    b_valladolid = models.BooleanField(default= False,verbose_name='Contabilizar Valladolid')
    c_las_palmas = models.PositiveIntegerField(verbose_name='Nº Las Palmas',null=True, blank=True)
    b_las_palmas = models.BooleanField(default= False,verbose_name='Contabilizar Las Palmas')
    c_mallorca = models.PositiveIntegerField(verbose_name='Nº  Mallorca',null=True, blank=True)
    b_mallorca = models.BooleanField(default= False,verbose_name='Contabilizar Mallorca')
    c_zamora = models.PositiveIntegerField(verbose_name='Nº Zamora',null=True, blank=True)
    b_zamora = models.BooleanField(default= False,verbose_name='Contabilizar Zamora')
    c_general = models.PositiveIntegerField(verbose_name='Nº General',null=True, blank=True)
    ciudad_recogida = models.CharField(max_length=50,verbose_name='Ciudad recogida',null=True, blank=True)
    ciudad_devolucion = models.CharField(max_length=50,verbose_name='Ciudad devoluvion',null=True, blank=True)
    h_inicio = models.TimeField(verbose_name='Hora inicio',null=True, blank=True)
    f_inicio = models.DateField(verbose_name='Fecha inicio',null=True, blank=True)
    h_fin = models.TimeField(verbose_name='Hora finalización',null=True, blank=True)
    f_fin = models.DateField(verbose_name='Fecha finalización',null=True, blank=True)
    km_libres = models.PositiveIntegerField(verbose_name='KM libres',default=0)
    km_inicio = models.PositiveIntegerField(verbose_name='KM inicio',default=0)
    km_fin = models.PositiveIntegerField(verbose_name='KM fin',default=0,blank=True,null=True)
    empleado = models.CharField(max_length=30,verbose_name='Empleado',null=True, blank=True)
    
    #-------conductor--------
    conductor = models.CharField(max_length=110,verbose_name='Conductor')
    id_conductor = models.PositiveIntegerField(verbose_name='Id Conductor',default=0)
    apellido = models.CharField(max_length=110,  verbose_name='Apellidos',blank=True,null=True)
    nombre = models.CharField(max_length=110,  verbose_name='Nombre',blank=True,null=True)
    direccion = models.CharField(max_length=210,  verbose_name='Dirección',blank=True,null=True)
    poblacion = models.CharField(max_length=110,  verbose_name='Población',blank=True,null=True)
    provincia = models.CharField(max_length=110,  verbose_name='Provincia',blank=True,null=True)
    cp = models.CharField(max_length=10,  verbose_name='C.P.',blank=True,null=True)    
    pais = models.CharField(max_length=110,  verbose_name='País',blank=True,null=True)
    telefono = models.CharField(max_length=110,  verbose_name='Movil',blank=True,null=True)
    movil = models.CharField(max_length=110,  verbose_name='Teléfono',blank=True,null=True)
    f_nacimiento = models.DateField(verbose_name= 'Fecha nacimiento',blank=True,null=True)

    licencia = models.CharField(max_length=210,  verbose_name='Nº de licéncia',blank=True,null=True)
    l_exp = models.CharField(max_length=210,  verbose_name='Lugar expedición',blank=True,null=True)
    f_exp = models.DateField(verbose_name= 'Fecha expedicion',blank=True,null=True)
    f_caducidad = models.DateField(verbose_name= 'Fecha caducidad',blank=True,null=True)
    #-------cliente--------
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
   #-------conductor Adicional--------
    adicional =  models.BooleanField(default= False , verbose_name='Adicional')
    conductor_a = models.CharField(max_length=110,verbose_name='Coductor Adicional',blank=True,null=True)
    id_conductor_ad = models.PositiveIntegerField(verbose_name='Id Conductor Adicional',blank=True,null=True)
    a_apellido = models.CharField(max_length=110,  verbose_name='Apellidos',blank=True,null=True)
    a_nombre = models.CharField(max_length=110,  verbose_name='Nombre',blank=True,null=True)
    a_direccion = models.CharField(max_length=210,  verbose_name='Dirección',blank=True,null=True)
    a_poblacion = models.CharField(max_length=110,  verbose_name='Población',blank=True,null=True)
    a_provincia = models.CharField(max_length=110,  verbose_name='Provincia',blank=True,null=True)
    a_cp = models.CharField(max_length=10,  verbose_name='C.P.',blank=True,null=True)    
    a_pais = models.CharField(max_length=110,  verbose_name='País',blank=True,null=True)
    a_telefono = models.CharField(max_length=110,  verbose_name='Movil',blank=True,null=True)
    a_movil = models.CharField(max_length=110,  verbose_name='Teléfono',blank=True,null=True)
    a_f_nacimiento = models.DateField(verbose_name= 'Fecha nacimiento',blank=True,null=True)

    a_licencia = models.CharField(max_length=210,  verbose_name='Nº de licéncia',blank=True,null=True)
    a_l_exp = models.CharField(max_length=210,  verbose_name='Lugar expedición',blank=True,null=True)
    a_f_exp = models.DateField(verbose_name= 'Fecha expedicion',blank=True,null=True)
    a_f_caducidad = models.DateField(verbose_name= 'Fecha caducidad',blank=True,null=True)
    #-------Vehiculo--------
    marca = models.CharField(max_length=30,verbose_name='Marca',default='')
    modelo = models.CharField(max_length=30, verbose_name='Modelo',default='') 
    t_combustible = models.CharField(max_length=30, verbose_name='Tipo Combustible',default='')
    color = models.CharField(max_length=20, verbose_name='Color', default='')
    id_vehiculo = models.PositiveIntegerField(verbose_name='Id Vehiculo')
    vehiculo = models.CharField(max_length=210,verbose_name='Vehículo')
    km_extra = models.CharField(max_length=20,verbose_name='Km Extra',null=True, blank=True)
    
    

   

    



