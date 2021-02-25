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

from .views import  CrearPresupuesto, ListaDePresupuestos, ListaDePresupuestosLasPalmas, ListaDePresupuestosMadrid, ListaDePresupuestosMallorca, ListaDePresupuestosSalamanca, ListaDePresupuestosValladolid, ListaDePresupuestosZamora


presupuesto_patterns = ([
   
    path("NuevoPresupuesto/", CrearPresupuesto.as_view(), name="crear_presupuesto"),
    path("", ListaDePresupuestos.as_view(), name="listapresupuestos"),
    path("LasPalmas/", ListaDePresupuestosLasPalmas.as_view(),name="laspalmas"),  
    path("Madrid/", ListaDePresupuestosMadrid.as_view(),name="madrid"),  
    path("Mallorca/", ListaDePresupuestosMallorca.as_view(),name="mallorca"),  
    path("Salamanca/", ListaDePresupuestosSalamanca.as_view(),name="salamanca"),  
    path("Valladolid/", ListaDePresupuestosValladolid.as_view(),name="valladolid"),  
    path("Zamora/", ListaDePresupuestosZamora.as_view(),name="zamora"),  
    
    


], 'presupuesto')
