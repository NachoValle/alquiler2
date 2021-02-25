from vehiculo.models import Vehiculo
from cliente.models import Cliente
from contrato.models import Contrato

from rest_framework.serializers import ModelSerializer

class VehiculoSerializer(ModelSerializer):
    class Meta:
        model = Vehiculo
        fields='__all__'

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields='__all__'

class ContratoSerializer(ModelSerializer):
    class Meta:
        model = Contrato
        fields=['id','combustible','oficina','c_madrid','c_salamanca','c_valladolid','c_las_palmas','c_mallorca','c_zamora','b_madrid','b_salamanca','b_valladolid','b_las_palmas','b_mallorca','b_zamora','c_general',
                'ciudad_recogida','ciudad_devolucion','h_fin','f_fin','km_ilimitado','km_libres','km_inicio','conductor','cliente','adicional','conductor_a','vehiculo','fianza','fianza_tarjeta','franquicia',]