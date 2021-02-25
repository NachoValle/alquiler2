"""alquiler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import  CrearContrato,ActulizarContrato, PdfContrato, ListaDeContratos, ListaDeContratosMadrid, ListaDeContratosSalamanca, ListaDeContratosValladolid, ListaDeContratosMallorca, ListaDeContratosLasPalmas, ListaDeContratosZamora, ListaDeConceptos, CrearConcepto, ActualizarConcepto


contrato_patterns = ([
    path("", ListaDeContratos.as_view(), name="listacontratos"),
    path("madrid/", ListaDeContratosMadrid.as_view(), name="contratosmadrid"),
    path("salamanca/", ListaDeContratosSalamanca.as_view(),name="contratossalamanca"),
    path("valladolid/", ListaDeContratosValladolid.as_view(),name="contratosvalladolid"),
    path("mallorca/", ListaDeContratosMallorca.as_view(), name="contratosmallorca"),
    path("laspalmas/", ListaDeContratosLasPalmas.as_view(),name="contratoslaspalmas"),
    path("zamora/", ListaDeContratosZamora.as_view(), name="contratoszamora"),
    path("ListaConceptos/", ListaDeConceptos.as_view(), name="conceptos"),
    path("NuevoConcepto/", CrearConcepto.as_view(), name="crear_concepto"),
    path("NuevoContrato/", CrearContrato.as_view(), name="crear_contrato"),
    path('ActualizarConcepto/<int:pk>/', ActualizarConcepto.as_view(), name='actualizar_concepto'),
    path('ActualizarContrato/<int:pk>/<slug:slug>/', ActulizarContrato.as_view(), name='actualizar_contrato'),
    path('<int:pk>/<slug:slug>/', PdfContrato.as_view(), name='contratopdf'),   
    
    


], 'contrato')
