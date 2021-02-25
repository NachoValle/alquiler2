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

from .forms import ConceptoForm, ContratoForm,ContratoFormUpdate
from .models import Contrato, ConceptoAlquiler
from vehiculo.models import Vehiculo
from agencia.models import Agencia

@method_decorator(login_required,name='dispatch')
class ActulizarContrato(SuccessMessageMixin,UpdateView):
    model = Contrato
    form_class = ContratoFormUpdate
    template_name = 'contrato/Contrato_actualizar.html'
    success_message = " Contrato Actualizado con Exito "
    success_url = reverse_lazy("home")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ActulizarContrato,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        if not self.object.km_libres:
            self.object.km_libres = 0
        if not self.object.km_fin:
            self.object.km_fin = 0
        if not self.object.km_inicio:
            self.object.km_inicio = 0

        context['recorridos'] = self.object.km_fin - self.object.km_inicio
        if not self.object.km_ilimitado:
                   
            if (self.object.km_fin - self.object.km_inicio) > self.object.km_libres:
                context['extra'] = (self.object.km_fin - self.object.km_inicio) - self.object.km_libres
       
        return context
    def form_valid(self, form):
        # ---- pausar salvar el formulario
        self.object = form.save(commit=False)
        if not self.object.km_fin:
            self.object.km_fin = 0


    #---- Salvar cambios y guardar contrato
        self.object.save()
        return super(ActulizarContrato, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class PdfContrato(DetailView):
    """
    regresa PDF
    """
    model = Contrato
    template_name = "contrato/contratopdf.html"
    def get_context_data(self, **kwargs):
        context = super(PdfContrato, self).get_context_data(**kwargs)
        # add extra context if needed
        agencia = Agencia.objects.all()
        for i in agencia:
            if self.object.oficina == i.ciudad:
                context['condiciones_oficina'] = i.condiciones
        for i in agencia:
            if self.object.oficina == i.ciudad:
                context['movil_oficina'] = i.telefono_movil

        return context
    def render_to_response(self, context, **kwargs):
        pdf = render_pdf(self.template_name, context)
        return HttpResponse(pdf, content_type="application/pdf")

# Conceptos Alquiler
@method_decorator(login_required, name='dispatch')
class ListaDeConceptos(ListView):
    model = ConceptoAlquiler
    template_name = 'contrato/lista_conceptos.html'

@method_decorator(login_required, name='dispatch')
class CrearConcepto(SuccessMessageMixin,CreateView):    
    template_name = 'contrato/crear_concepto.html'
    form_class = ConceptoForm
    success_message = " Concepto Creado con Exito"
    success_url = reverse_lazy("contrato:conceptos")

@method_decorator(login_required, name='dispatch')
class ActualizarConcepto(SuccessMessageMixin,UpdateView):
    model = ConceptoAlquiler    
    template_name = 'contrato/crear_concepto.html'
    form_class = ConceptoForm
    success_message = " Concepto Actualizado con Exito"
    success_url = reverse_lazy("contrato:conceptos")


# Contratos Alquiler





@method_decorator(login_required, name='dispatch')
class CrearContrato(CreateView):    
    template_name = 'contrato/crear_contrato.html'
    form_class = ContratoForm
   
    
    def get_success_url(self):
        return reverse_lazy('contrato:contratopdf', args=[self.object.id, self.object.c_general,]  )
    
    
    def form_valid(self, form):
        # ---- pausar salvar el formulario
        self.object = form.save(commit=False)
        # ---- activar alquiler
        self.object.alquilado  = True
        # ---- activar Fianza
        if self.object.fianza > 0:
             self.object.fianza_deposito = True


        # ---- sumar los conceptos si existen
        cadena = self.object.concepto1.concepto + ' ' 
        if self.object.concepto2:
            cadena = cadena + self.object.concepto2.concepto + ' '
        if self.object.concepto3:
            cadena = cadena + self.object.concepto3.concepto + ' '
        if self.object.concepto4:
            cadena = cadena + self.object.concepto4.concepto + ' '
        if self.object.concepto5:
            cadena = cadena + self.object.concepto5.concepto + ' '
        if self.object.concepto6:
            cadena = cadena + self.object.concepto6.concepto
        # ---- convertirlos a minusculas
        cadena = cadena.lower()
        # ---- buscar si existe concepto de sustitucion y activarlo
        if cadena.find('sustitucion')>=0 or cadena.find('sustitución')>=0:
            self.object.sustitucion  = True
        # ---- buscar si existe concepto de adicional y activarlo        
        if cadena.find('adicional')>=0:
            self.object.adicional  = True
             
        # ---- si no existe conductor adicional borrar datos conductor adicional
        if  self.object.adicional == False:
            self.object.conductor_a = ''
            self.object.a_nombre = ''
            self.object.a_apellido = ''
            self.object.a_direccion = ''
            self.object.a_poblacion = ''
            self.object.a_provincia = ''
            self.object.a_cp = ''
            self.object.a_pais = ''
            self.object.a_telefono = ''
            self.object.a_movil = ''           
            self.object.a_l_exp = ''            
            self.object.a_licencia = ''

        #------  buscar el ultimo contrato general y sumar uno
        print(self.object.oficina)
        lista_general=0
        contratos_general = Contrato.objects.all()
        for i in contratos_general:
            lista_general += 1      
                                       
        self.object.c_general = lista_general + 1

        #------  buscar el ultimo contrato Salamanca y sumar uno
        if self.object.oficina == 'SALAMANCA':
            c_oficina = Contrato.objects.filter(b_salamanca = True)
            lista_salamanca = 0
            if c_oficina:                
                for i in c_oficina:
                    lista_salamanca +=1                 
             
            self.object.c_salamanca = lista_salamanca + 1     
            self.object.b_salamanca = True
            

        #------  buscar el ultimo contrato MADRID y sumar uno
        if self.object.oficina == 'MADRID':
                c_oficina = Contrato.objects.filter(b_madrid = True)
                lista_madrid = 0
                if c_oficina:                    
                    for i in c_oficina:
                        lista_madrid += 1                        
               
                self.object.c_madrid = lista_madrid + 1
                self.object.b_madrid = True        

        
        #------  buscar el ultimo contrato VALLADOLID y sumar uno
        if self.object.oficina == 'VALLADOLID':
            c_oficina = Contrato.objects.filter(b_valladolid = True)
            lista_valladolid = 0 
            if c_oficina:                
                for i in c_oficina:
                    lista_valladolid += 0
                    
            self.object.c_valladolid = lista_valladolid + 1
            self.object.b_valladolid = True

        #------  buscar el ultimo contrato LAS PALMAS y sumar uno
        if self.object.oficina == 'LAS PALMAS':
            print(self.object.oficina)
            c_oficina = Contrato.objects.filter(b_las_palmas = True)
            lista_las_palmas = 0
            if c_oficina:                
                for i in c_oficina:
                    lista_las_palmas += 1
                print(lista_las_palmas)
            
            self.object.c_las_palmas = lista_las_palmas + 1
            self.object.b_las_palmas = True
            print(self.object.c_las_palmas)
            print(self.object.b_las_palmas)
          
        #------  buscar el ultimo contrato MALLORCA y sumar uno
        if self.object.oficina == 'MALLORCA':
            c_oficina = Contrato.objects.filter(b_mallorca = True)
            lista_mallorca = 0
            if c_oficina:                
                for i in c_oficina:
                    lista_mallorca += 1

            self.object.c_mallorca = lista_mallorca + 1
            self.object.b_mallorca = True

        #------  buscar el ultimo contrato ZAMORA y sumar uno
        if self.object.oficina == 'ZAMORA':
            c_oficina = Contrato.objects.filter(b_zamora = True)
            lista_zamora = 0
            if c_oficina:                
                for i in c_oficina:
                    lista_zamora += 1

            self.object.c_zamora = lista_zamora + 1  
            self.object.b_zamora = True

        #---- Salvar cambios y guardar contrato
        self.object.save()
        return super(CrearContrato, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class ListaDeContratos(ListView):
    model = Contrato

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.todas == True:
            return super(ListaDeContratos, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDeContratosMadrid(TemplateView):
    template_name = "contrato/contrato_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeContratosMadrid,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['contratos'] = Contrato.objects.filter(b_madrid=True)
        context['ciudad'] = 'Madrid'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.madrid == True:
            return super(ListaDeContratosMadrid, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDeContratosSalamanca(TemplateView):
    template_name = "contrato/contrato_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeContratosSalamanca,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['contratos'] = Contrato.objects.filter(b_salamanca=True)
        context['ciudad'] = 'Salamanca'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.salamanca == True:
            return super(ListaDeContratosSalamanca, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDeContratosValladolid(TemplateView):
    template_name = "contrato/contrato_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeContratosValladolid,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['contratos'] = Contrato.objects.filter(b_valladolid=True)
        context['ciudad'] = 'Valladolid'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.valladolid == True:
            return super(ListaDeContratosValladolid, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDeContratosMallorca(TemplateView):
    template_name = "contrato/contrato_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeContratosMallorca,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['contratos'] = Contrato.objects.filter(b_mallorca=True)
        context['ciudad'] = 'Mallorca'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.mallorca == True:
            return super(ListaDeContratosMallorca, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDeContratosLasPalmas(TemplateView):
    template_name = "contrato/contrato_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeContratosLasPalmas,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['contratos'] = Contrato.objects.filter(b_las_palmas=True)
        context['ciudad'] = 'Las Palmas de Gran Canaria'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.las_palmas == True:
            return super(ListaDeContratosLasPalmas, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))


@method_decorator(login_required, name='dispatch')
class ListaDeContratosZamora(TemplateView):
    template_name = "contrato/contrato_list_ciudad.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListaDeContratosZamora,
                        self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['contratos'] = Contrato.objects.filter(b_zamora=True)
        context['ciudad'] = 'Zamora'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.zamora == True:
            return super(ListaDeContratosZamora, self).dispatch(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'))
