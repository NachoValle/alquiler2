from django.db import models

# Create your models here.
from django.db import models
from agencia.models import Agencia



CAR_GRUPO = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('FA', 'FA'),
        ('FB', 'FB'),
        ('FC', 'FC'),
        ('FD', 'FD'),
        ('FE', 'FE'),
        ('FF', 'FD'),
    )


# Create your models here.
class Grupo(models.Model):
    ciudad = models.CharField(max_length=20,  verbose_name='Ciudad')
    ciudad2 = models.CharField(max_length=20,verbose_name='Ciudad2')
    grupo = models.CharField(max_length=2, choices=CAR_GRUPO, verbose_name='Grupo')
    descripcion = models.CharField(max_length=100,  verbose_name='Descripción')
    dia1 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='1 dia')
    dia2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='2 dias')
    dia3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='3 dias')
    dia4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='4 dias')
    dia5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='5 dias')
    dia6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='6 dias')
    dia7 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='7 dias')
    dia8 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='8 dias')
    dia9 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='9 dias')
    dia10 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='10 dias')
    dia11 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='11 dias')
    dia12 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='12 dias')
    dia13 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='13 dias')
    dia14 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='14 dias')
    dia15 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='15 dias')
    dia16 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='16 dias')
    dia17 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='17 dias')
    dia18 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='18 dias')
    dia19 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='19 dias')
    dia20 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='20 dias')
    dia21 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='21 dias')
    dia22 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='22 dias')
    dia23 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='23 dias')
    dia24 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='24 dias')
    dia25 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='25 dias')
    dia26 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='26 dias')
    dia27 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='27 dias')
    dia28 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='28 dias')
    dia29 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='29 dias')
    dia30 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='30 dias')
    dia31 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='31 dias')

    m_dia1 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_1 dia')
    m_dia2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_2 dias')
    m_dia3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_3 dias')
    m_dia4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_4 dias')
    m_dia5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_5 dias')
    m_dia6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_6 dias')
    m_dia7 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_7 dias')
    m_dia8 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_8 dias')
    m_dia9 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_9 dias')
    m_dia10 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_10 dias')
    m_dia11 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_11 dias')
    m_dia12 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_12 dias')
    m_dia13 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_13 dias')
    m_dia14 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_14 dias')
    m_dia15 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_15 dias')
    m_dia16 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_16 dias')
    m_dia17 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_17 dias')
    m_dia18 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_18 dias')
    m_dia19 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_19 dias')
    m_dia20 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_20 dias')
    m_dia21 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_21 dias')
    m_dia22 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_22 dias')
    m_dia23 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_23 dias')
    m_dia24 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_24 dias')
    m_dia25 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_25 dias')
    m_dia26 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_26 dias')
    m_dia27 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_27 dias')
    m_dia28 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_28 dias')
    m_dia29 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_29 dias')
    m_dia30 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_30 dias')
    m_dia31 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='m_31 dias')

    a_dia1 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_1 dia')
    a_dia2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_2 dias')
    a_dia3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_3 dias')
    a_dia4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_4 dias')
    a_dia5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_5 dias')
    a_dia6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_6 dias')
    a_dia7 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_7 dias')
    a_dia8 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_8 dias')
    a_dia9 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_9 dias')
    a_dia10 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_10 dias')
    a_dia11 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_11 dias')
    a_dia12 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_12 dias')
    a_dia13 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_13 dias')
    a_dia14 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_14 dias')
    a_dia15 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_15 dias')
    a_dia16 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_16 dias')
    a_dia17 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_17 dias')
    a_dia18 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_18 dias')
    a_dia19 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_19 dias')
    a_dia20 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_20 dias')
    a_dia21 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_21 dias')
    a_dia22 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_22 dias')
    a_dia23 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_23 dias')
    a_dia24 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_24 dias')
    a_dia25 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_25 dias')
    a_dia26 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_26 dias')
    a_dia27 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_27 dias')
    a_dia28 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_28 dias')
    a_dia29 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_29 dias')
    a_dia30 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_30 dias')
    a_dia31 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='a_31 dias')

    k1 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='1 d/km')
    k2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='2 d/km')
    k3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='3 d/km')
    k4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='4 d/km')
    k5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='5 d/km')
    k6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='6 d/km')
    k7 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='7 d/km')
    k8 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='8 d/km')
    k9 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='9 d/km')
    k10 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='10 d/km')
    k11 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='11 d/km')
    k12 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='12 d/km')
    k13 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='13 d/km')
    k14 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='14 d/km')
    k15 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='15 d/km')
    k16 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='16 d/km')
    k17 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='17 d/km')
    k18 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='18 d/km')
    k19 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='19 d/km')
    k20 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='20 d/km')
    k21 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='21 d/km')
    k22 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='22 d/km')
    k23 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='23 d/km')
    k24 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='24 d/km')
    k25 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='25 d/km')
    k26 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='26 d/km')
    k27 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='27 d/km')
    k28 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='28 d/km')
    k29 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='29 d/km')
    k30 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='30 d/km')
    k31 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='31 d/km')

    km1 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='1 d_M/km')
    km2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='2 d_M/km')
    km3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='3 d_M/km')
    km4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='4 d_M/km')
    km5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='5 d_M/km')
    km6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='6 d_M/km')
    km7 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='7 d_M/km')
    km8 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='8 d_M/km')
    km9 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='9 d_M/km')
    km10 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='10 d_M/km')
    km11 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='11 d_M/km')
    km12 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='12 d_M/km')
    km13 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='13 d_M/km')
    km14 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='14 d_M/km')
    km15 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='15 d_M/km')
    km16 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='16 d_M/km')
    km17 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='17 d_M/km')
    km18 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='18 d_M/km')
    km19 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='19 d_M/km')
    km20 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='20 d_M/km')
    km21 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='21 d_M/km')
    km22 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='22 d_M/km')
    km23 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='23 d_M/km')
    km24 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='24 d_M/km')
    km25 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='25 d_M/km')
    km26 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='26 d_M/km')
    km27 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='27 d_M/km')
    km28 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='28 d_M/km')
    km29 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='29 d_M/km')
    km30 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='30 d_M/km')
    km31 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='31 d_M/km')

    ka1 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='1 d_A/km')
    ka2 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='2 d_A/km')
    ka3 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='3 d_A/km')
    ka4 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='4 d_A/km')
    ka5 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='5 d_A/km')
    ka6 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='6 d_A/km')
    ka7 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='7 d_A/km')
    ka8 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='8 d_A/km')
    ka9 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='9 d_A/km')
    ka10 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='10 d_A/km')
    ka11 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='11 d_A/km')
    ka12 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='12 d_A/km')
    ka13 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='13 d_A/km')
    ka14 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='14 d_A/km')
    ka15 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='15 d_A/km')
    ka16 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='16 d_A/km')
    ka17 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='17 d_A/km')
    ka18 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='18 d_A/km')
    ka19 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='19 d_A/km')
    ka20 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='20 d_A/km')
    ka21 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='21 d_A/km')
    ka22 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='22 d_A/km')
    ka23 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='23 d_A/km')
    ka24 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='24 d_A/km')
    ka25 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='25 d_A/km')
    ka26 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='26 d_A/km')
    ka27 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='27 d_A/km')
    ka28 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='28 d_A/km')
    ka29 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='29 d_A/km')
    ka30 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='30 d_A/km')
    ka31 = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True,verbose_name='31 d_A/km')
    def save(self):
        city = self.ciudad
        city = city.replace(" ", "")
        self.ciudad2 = city

        
        
        super(Grupo,self).save()

    def __str__(self):
        return self.grupo

    