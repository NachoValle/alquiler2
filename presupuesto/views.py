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

from core.utileria import render_pdf

from .models import Presupuesto
from agencia.models import Agencia
from vehiculo.models import Vehiculo
from cliente.models import Cliente
from .forms import PresupuestoForm

# Create your views here.
@method_decorator(login_required, name='dispatch')
class CrearPresupuesto(SuccessMessageMixin,CreateView): 
    model = Presupuesto   
    template_name = 'presupuesto/crear_presupuesto.html'
    form_class = PresupuestoForm
    success_message = " Presupuesto creado con Exito"
    success_url = reverse_lazy("home")

@method_decorator(login_required, name='dispatch')
class ListaDePresupuestos(ListView):
    model = Presupuesto
    template_name = 'presupuesto/presupuesto_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.todas == True:
            return super(ListaDePresupuestos, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))

@method_decorator(login_required, name='dispatch')
class ListaDePresupuestosMadrid(TemplateView):
    template_name = "presupuesto/presupuesto_list_ciudad.html"
   


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDePresupuestosMadrid,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['presupuestos'] = Presupuesto.objects.filter(oficina ="MADRID")
        context['ciudad'] = 'Madrid'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.madrid == True:
            return super(ListaDePresupuestosMadrid, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDePresupuestosSalamanca(TemplateView):
    template_name = "presupuesto/presupuesto_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDePresupuestosSalamanca,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['presupuestos'] = Presupuesto.objects.filter(oficina ="SALAMANCA")
        context['ciudad'] = 'Salamanca'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.salamanca == True:
            return super(ListaDePresupuestosSalamanca, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDePresupuestosValladolid(TemplateView):
    template_name = "presupuesto/presupuesto_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDePresupuestosValladolid,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['presupuestos'] = Presupuesto.objects.filter(oficina ="VALLADOLID")
        context['ciudad'] = 'Valladolid'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.valladolid == True:
            return super(ListaDePresupuestosValladolid, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDePresupuestosMallorca(TemplateView):
    template_name = "presupuesto/presupuesto_list_ciudad.html"  
  
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDePresupuestosMallorca,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['presupuestos'] = Presupuesto.objects.filter(oficina ="MALLORCA")
        context['ciudad'] = 'Mallorca'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.mallorca == True:
            return super(ListaDePresupuestosMallorca, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))




@method_decorator(login_required, name='dispatch')
class ListaDePresupuestosZamora(TemplateView):
    template_name = "presupuesto/presupuesto_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDePresupuestosZamora,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['presupuestos'] = Presupuesto.objects.filter(oficina ="ZAMORA")
        context['ciudad'] = 'Zamora'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.zamora == True:
            return super(ListaDePresupuestosZamora, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDePresupuestosLasPalmas(TemplateView):
    template_name = "presupuesto/presupuesto_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDePresupuestosLasPalmas,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['presupuestos'] = Presupuesto.objects.filter(oficina = "LAS PALMAS")
        context['ciudad'] = 'Las Palmas de Gran Canaria'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.las_palmas == True:
            return super(ListaDePresupuestosLasPalmas, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))