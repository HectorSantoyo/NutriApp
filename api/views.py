from datetime import date
from time import time
from . import models
from django.http import JsonResponse
import json

campos_citas = {
    "id": int, 
    "nombre_paciente": str, 
    "apellidos": str, 
    "fecha": date, 
    "hora": time, 
    "lugar": str
    }
campos_pacientes = {
    "id": int,
    "nombre": str, 
    "apellidos": str, 
    "telefono": int, 
    "email": str
    }

def carga_citas(request):
    '''Función encargada de crear objetos instaciados de models.Cita y de poblar la base de datos.'''
    # Carga los datos de un archivo JSON
    with open('citas.json', 'tr') as archivo:
        citas = json.load(archivo)
    #Crea un objeto a partir de cada elemento tipo dict de citas
    for registro in citas:
        # Crea un objeto instanciando la clase Cita
        objeto = models.Cita()
        # Asigna cada campo a su atributo correspondiente
        for campo in registro:
            setattr(objeto, campo, registro[campo])
        # Guarda a la base de datos.
        objeto.save()
    #Regresa la relaciónde alumnos dados de alta.
    return JsonResponse({'respuesta':citas})


def vista_citas(request):
    return JsonResponse({'respuesta':[{campo:getattr(cita, campo) for campo in campos_citas} for cita in models.Cita.objects.all()]})


def carga_pacientes(request):
    '''Función encargada de crear objetos instaciados de models.Paciente y de poblar la base de datos.'''
    # Carga los datos de un archivo JSON
    with open('pacientes.json', 'tr') as archivo:
        pacientes = json.load(archivo)
    #Crea un objeto a partir de cada elemento tipo dict de pacientes
    for registro in pacientes:
        # Crea un objeto instanciando la clase Cita
        objeto = models.Paciente()
        # Asigna cada campo a su atributo correspondiente
        for campo in registro:
            setattr(objeto, campo, registro[campo])
        # Guarda a la base de datos.
        objeto.save()
    #Regresa la relaciónde alumnos dados de alta.
    return JsonResponse({'respuesta':pacientes})


def vista_pacientes(request):
    return JsonResponse({'respuesta':[{campo:getattr(paciente, campo) for campo in campos_pacientes} for paciente in models.Paciente.objects.all()]})