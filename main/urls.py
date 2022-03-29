"""NutriApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path 
from . import views

urlpatterns = [
    path('', views.index, name="inicio"), 
    path('vista', views.vista),
    re_path(r'^claves/(?P<clave>[0-9]{4}$)', views.clave),
    path('claves/<int:numero>', views.numero),
    path('claves/<str:nombre>', views.saluda),
    path('json', views.respuesta_json),
    path('contenido', views.contenido),
    path('error', views.error),
    path('listas', views.listas),
]
