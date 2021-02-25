from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView

from datetime import datetime, date, timedelta


from contrato.models import Contrato



# Create your views here.
@method_decorator(login_required,name='dispatch')
class BuscarMulta(TemplateView):   
    
    template_name='buscamultas/buscamultas.html'
    
@method_decorator(login_required,name='dispatch')
class listaMultados(TemplateView):   
    
    template_name='buscamultas/contrato_multa.html'

    def post(self, request, *args, **kwargs):
        #   matricula
        placa = request.POST['matricula']
        placa = placa.upper()
        #busca todos los contratos con esa matricula
        contratos = Contrato.objects.filter(vehiculo__contains = placa)
        
        contratos_fecha=[]
        # fecha
        formato_fecha = "%Y-%m-%d"
        fecha = request.POST['fecha']
        
        # HORA
        hora = request.POST['hora']
        if hora:
            hora = datetime.strptime(hora, "%H:%M").time()
        n_contratos = len(contratos)
        # si encuentra contratos
        if n_contratos > 0:
            for i in contratos:
                inicio = i.f_inicio
                fin = i.f_fin              
                # si la fecha esta en el rango de alquiler del contrato
                if str(fecha) >= str(inicio):
                    if  str(fecha) <= str(fin) :
                        contratos_fecha.append(i)
                    # si la fecha es igual a la devolucion
                    if str(fecha) == str(fin):                        
                        hora_final = i.h_fin
                        # si existe la hora y está fuera de la hora de entrega que elimine el contrato
                        if hora:
                            if hora_final< hora:                               
                                contratos_fecha.remove(i)


                            
                           
        print(contratos_fecha)
        
        
        
       


        
        return render(request,'buscamultas/contrato_multa.html', {'contratos':contratos_fecha})

    


