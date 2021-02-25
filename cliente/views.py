from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView

from .models import Cliente
from .forms import ClienteForm, ClienteFormUpdate

# Create your views here.
@method_decorator(login_required,name='dispatch')
class ClientesList(ListView):
    model = Cliente
 
@method_decorator(login_required,name='dispatch')
class ClientesListaNegra(ListView):
    model = Cliente
    template_name = "cliente/cliente_list_negra.html"

@method_decorator(login_required,name='dispatch')
class DetalleCliente(DetailView):
    model = Cliente
    template_name='cliente/DETALLECLIENTE.html'

@method_decorator(login_required,name='dispatch')
class CrearCliente(SuccessMessageMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    
    template_name = 'cliente/CLIENTECREAR.html'
    success_message = " Cliente Creado con Exito"
    
    def get_success_url(self):
        return reverse_lazy('cliente:detalle', args=[self.object.id, self.object.n_id,]  )


@method_decorator(login_required,name='dispatch')
class ActulizarCliente(SuccessMessageMixin,UpdateView):
    model = Cliente
    form_class = ClienteFormUpdate
    template_name = 'cliente/CLIENTEACTUALIZAR.html'
    success_message = " Cliente Actualizado con Exito"
    
    def get_success_url(self):
        return reverse_lazy('cliente:detalle', args=[self.object.id, self.object.n_id,]  )