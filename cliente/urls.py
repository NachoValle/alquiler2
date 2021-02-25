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
from .views import ClientesList, ClientesListaNegra, DetalleCliente, CrearCliente, ActulizarCliente



cliente_patterns = ([
    path("",ClientesList.as_view(), name="listaclientes"),
    path("ListaNegra/",ClientesListaNegra.as_view(), name="listanegra"),
    path('<int:pk>/<slug:slug>/', DetalleCliente.as_view(), name='detalle'),
    path('Crear/', CrearCliente.as_view(), name='crear'),
    path('Actualizar/<int:pk>', ActulizarCliente.as_view(), name='actualizar'),
    

    ],'cliente')