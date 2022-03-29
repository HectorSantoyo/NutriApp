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
from . import views, endpoint_views, template_views

urlpatterns = [
    #path('vista_citas', views.vista_citas),
    path('', template_views.index),
    path('carga_citas', views.carga_citas),
    path('vista_pacientes', template_views.vista_pacientes),
    path('valida_pacientes', template_views.valida_pacientes),
    path('carga_pacientes', views.carga_pacientes),
    path('vista_citas/<int:clave>', endpoint_views.clave_citas),
    path('vista_pacientes/<int:clave>', endpoint_views.clave_pacientes),
    path('vista_citas/', template_views.vista_citas),
    path('vista_citas_fecha/', template_views.vista_citas_fecha, name="test"),
    path('valida_citas/', template_views.valida_citas),
    path('alta_citas/', template_views.forma_citas),
    path('alta_pacientes/', template_views.forma_pacientes)
    ]
    