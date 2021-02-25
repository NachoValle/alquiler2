from django.shortcuts import render
from django.views.generic.base import TemplateView
import json
from django.http import HttpResponse
from .serializers import VehiculoSerializer, ClienteSerializer, ContratoSerializer
from rest_framework.views import APIView
from vehiculo.models import Vehiculo
from cliente.models import Cliente
from contrato.models import Contrato


class HomeView(TemplateView):
    template_name = "core/home.html"

#Serializer de Vehiculos
class VehiculoAPI(APIView):
    serializer = VehiculoSerializer
    

    def get(self, request, format=None):
        lista = Vehiculo.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')

#Serializer de Vehiculos
class ClienteAPI(APIView):
    serializer = ClienteSerializer
    

    def get(self, request, format=None):
        lista = Cliente.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')
  
#Serializer de Contratos
class ContratoAPI(APIView):
    serializer = ContratoSerializer
    

    def get(self, request, format=None):
        lista = Contrato.objects.all()
        response = self.serializer(lista, many=True)

        return HttpResponse(json.dumps(response.data), content_type='application/json')
   