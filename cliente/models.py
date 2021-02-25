from django.db import models
from django.utils import timezone
from datetime import timedelta, date


ID_TYPE=(('N.I.F.','N.I.F.'),
          ('Pasaporte','Pasaporte'),
          ('C.I.F.','C.I.F.'),
    )

def custom_upload_to1(instance, filename):
    old_instance = Cliente.objects.get(pk = instance.pk)
    
    old_instance.document1.delete()
    return 'cliente/' + filename

def custom_upload_to2(instance, filename):
    old_instance = Cliente.objects.get(pk = instance.pk)
    
    old_instance.document2.delete()
    return 'cliente/' + filename



class Cliente(models.Model):
    
    negra = models.BooleanField(default=False,verbose_name='Lista Negra')
   
    tipo = models.CharField(max_length=20,choices=ID_TYPE,verbose_name='Tipo de documentación' )
    n_id = models.CharField(max_length=110,  verbose_name='Nº Identificación')
    f_exp_id = models.DateField(verbose_name= 'Fecha expedición ID', blank=True,null=True)
    
    apellido = models.CharField(max_length=110,  verbose_name='Apellidos',blank=True,null=True)
    nombre = models.CharField(max_length=110,  verbose_name='Nombre')
    direccion = models.CharField(max_length=210,  verbose_name='Dirección',blank=True,null=True)
    poblacion = models.CharField(max_length=110,  verbose_name='Población',blank=True,null=True)
    provincia = models.CharField(max_length=110,  verbose_name='Provincia',blank=True,null=True)
    cp = models.CharField(max_length=10,  verbose_name='C.P.',blank=True,null=True)
    
    pais = models.CharField(max_length=110,  verbose_name='País',blank=True,null=True)
    telefono = models.CharField(max_length=110,  verbose_name='Movil',blank=True,null=True)
    movil = models.CharField(max_length=110,  verbose_name='Teléfono',blank=True,null=True)
    email = models.EmailField(max_length=210,  verbose_name='Email',blank=True,null=True)
    f_nacimiento = models.DateField(verbose_name= 'Fecha nacimiento',blank=True,null=True)
    l_nacimiento = models.CharField(max_length=210,  verbose_name='Lugar de nacimiento',blank=True,null=True)
   
    licencia = models.CharField(max_length=210,  verbose_name='Nº de licéncia',blank=True,null=True)
    l_exp = models.CharField(max_length=210,  verbose_name='Lugar expedición',blank=True,null=True)
    f_exp = models.DateField(verbose_name= 'Fecha expedicion',blank=True,null=True)
    f_caducidad = models.DateField(verbose_name= 'Fecha caducidad',blank=True,null=True)
   
    trabajo =  models.CharField(max_length=210,  verbose_name='Trabajo',blank=True,null=True)
    obs =  models.CharField(max_length=210,  verbose_name='Observaciones',blank=True,null=True)
   
    banco = models.CharField(max_length=210,  verbose_name='Datos bancarios',blank=True,null=True)
    tarjeta = models.CharField(max_length=210,  verbose_name='Nº Tarjeta',blank=True,null=True)
    f_tarjeta = models.CharField(max_length=5, verbose_name= 'Fecha caducidad tarjeta',blank=True,null=True)
    
    document1 = models.FileField( upload_to = 'cliente/' , null=True, blank=True, verbose_name='Documentación 1')
    document2 = models.FileField( upload_to = 'cliente/' , null=True, blank=True, verbose_name='Documentación 2')

    def edad(self):
        diferencia_fechas = date.today() - self.f_nacimiento
        diferencia_fechas_dias = diferencia_fechas.days
        edad_numerica = diferencia_fechas_dias / 365.2425
        years = int(edad_numerica)
        return years

   
   
   
    def save(self):
        
        self.n_id =self.n_id.upper()
        if self.licencia:
            self.licencia =self.licencia.upper()       
        
        super(Cliente,self).save()
    
    class Meta:
        ordering = ['n_id','apellido']
        unique_together =('n_id',)
    
    def __str__(self):
        return self.n_id








    

