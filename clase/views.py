from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import Grupo
from .forms import GrupoForm

@method_decorator(login_required, name='dispatch')
class CrearGrupo(SuccessMessageMixin,CreateView):    
    template_name = 'clase/crear_grupo.html'
    form_class = GrupoForm
    success_message = " Grupo Creado con Exito" 
        
    success_url = "/clase/{ciudad2}"

@method_decorator(login_required, name='dispatch')
class ListaDeGruposLasPalmas(TemplateView):
    template_name = "clase/grupo_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeGruposLasPalmas,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['grupos'] = Grupo.objects.filter(ciudad="LAS PALMAS")
        context['ciudad'] = 'Las Palmas de Gran Canaria'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.las_palmas == True:
            return super(ListaDeGruposLasPalmas, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('agencia:agencia'))
