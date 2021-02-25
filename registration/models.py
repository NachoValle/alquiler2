from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from agencia.models import Agencia

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk = instance.pk)
    
    old_instance.avatar_user.delete()
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_user = models.ImageField(upload_to=custom_upload_to, null= True, blank= True,verbose_name='Avatar')
    oficina = models.ForeignKey(Agencia, on_delete=models.PROTECT,null= True, blank= True,)
    madrid = models.BooleanField(default=False,verbose_name='Madrid')
    salamanca = models.BooleanField(default=False,verbose_name='Salamanca')
    valladolid = models.BooleanField(default=False,verbose_name='Valladolid')
    las_palmas = models.BooleanField(default=False,verbose_name='Las Palmas')
    mallorca = models.BooleanField(default=False,verbose_name='Mallorca')
    zamora = models.BooleanField(default=False,verbose_name='Zamora')
    todas = models.BooleanField(default=False,verbose_name='Todas')
    movil = models.CharField(max_length=20, null = True, blank= True,verbose_name='Télefono Movil')
    p_user = models.BooleanField(default=False,verbose_name='Permisos Usuarios')
    p_vehiculos = models.BooleanField(default=False,verbose_name='Crear Vehiculos')
    fianza = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Fianza',null=True, blank=True,)
    f_turismo = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Franquicia Turismo',null=True, blank=True,)
    f_carga = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Franquicia Carga',null=True, blank=True,)
    km_extra_turismo = models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Km extra turismo',null=True, blank=True,)
    km_extra_carga = models.DecimalField(max_digits=10, decimal_places=4,verbose_name='Km extra carga',null=True, blank=True,)
    trato =   models.CharField(max_length=210,  verbose_name='Atendido por',blank=True,null=True)
    
    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'

@receiver(post_save, sender = User )
def ensurace_perfil_exists(sender, instance, **kwargs):
    """
    crea un perfil automaticamente al dar de alta un usuario
    """
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        print('se ha creado un usuario y se ha enlzado un perfil')

    

