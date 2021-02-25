from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .forms import AgenciaForms
from .models import Agencia

# Create your views here.
@method_decorator(login_required,name='dispatch')
class ActualizarAgencia(SuccessMessageMixin,UpdateView):
    model = Agencia
    form_class = AgenciaForms
    template_name='agencia/agencia-form.html'
    success_message = " Oficina Actualizada con Exito"
    def get_success_url(self):
        return reverse_lazy('agencia:actualizar', args=[self.object.id,]  )

@method_decorator(login_required,name='dispatch')
class AgenciaList(ListView):
    model = Agencia
    template_name='agencia/agencias.html'