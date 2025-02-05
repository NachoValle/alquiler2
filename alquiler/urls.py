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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from core import views
from vehiculo.urls import vehiculo_patterns
from cliente.urls import cliente_patterns
from contrato.urls import contrato_patterns
from agencia.urls import agencia_patterns
from buscamultas.urls import bucamultas_patterns
from presupuesto.urls import presupuesto_patterns
from clase.urls import grupo_patterns

urlpatterns = [
    path('',include('core.urls')),
    path('vehiculo/',include(vehiculo_patterns)),
    path('clientes/',include(cliente_patterns)),
    path('contrato/',include(contrato_patterns)),
    path('agencia/',include(agencia_patterns)),
    path('buscamultas/',include(bucamultas_patterns)),
    path('presupuesto/',include(presupuesto_patterns)),
    path('clase/',include(grupo_patterns)),
    path('admin/', admin.site.urls),

    # paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    
    
]

#ver archivos media en pruebas
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)