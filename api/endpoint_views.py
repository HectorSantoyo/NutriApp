from . import models
from datetime import date
from time import time
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest

""" El objeto campos define la estructura de los campos aceptables para
los datos relacionando el nombre del campo y una tupla que cuyo primer
elemento es el tipo de dato del que se trata y el segundo elemento es 
un booleano que indica si el campo es obligatorio. """ 

campos_citas = {
    "nombre_paciente": (str, True), 
    "apellidos": (str, True), 
    "fecha": (str, True), 
    "hora": (str, True), 
    "lugar": (str, True),
    "id": (int, True),
    }

campos_pacientes = {
    "id": (int, True),
    "nombre": (str, True), 
    "apellidos": (str, True), 
    "telefono": (int, True), 
    "email": (str, True)
    }


"""El objeto lugar contiene una tupla con los lugares permitidas en el campo lugar.""" 
lugar = ('Consultorio Jani', 'Hospital Santa Ana', 'Online')

"""El objeto estructura_base es un objeto de tipo set que contiene los campos permitidos."""
#estructura_base = set(campos_citas)


def reglas(valor, campo):
    """ Función que valida las reglas de negocio """
    if campo == "lugar" and valor not in lugar:
        return False

    #elif campo == "fecha" and valor < date.today:
        #return False
    elif (campo in ("nombre", "apellidos") and (valor == "")):
        return False
    else:
        return True         


def valida(dato, campo):
    """ Función que valida un dato con relación a su campo correspondiente."""
    tipo = campos_citas[campo][0]
    try:
        if tipo is not str:
            valor = eval(dato)
        else:
            valor = dato
        if type(valor) is tipo or (tipo is float and type(dato) is int):
            return reglas(valor, campo)
        else:
            return False
    except:
        return False


@csrf_exempt
def clave_citas(request, clave):
    '''Función de vista que define un endpoint correspondiente a una clave de n dígitos.
    Opera con los métodos GET, POST, DELETE.'''
    # Cuando la petición es GET va a obtener los datos de la cita con la clave correrspondiente.
    # Esta operación se realiza en caso de que exista un objeto con el número de id.
    if request.method == "GET":
        try:
            cita = models.Cita.objects.get(id=clave) 
            return JsonResponse({campo:getattr(cita, campo) for campo in campos_citas})
        # La excepción models.Cita.DoesNotExist se desencadena cuando la búsqueda no arroje un resultado.
        except models.Cita.DoesNotExist:
            return HttpResponseNotFound()

    # Cuando la petición es DELETE la cita es eliminada de la base de datos.
    # Esta operación se realiza en caso de que exista un objeto con el id.
    if request.method == "DELETE":
        try:
            cita = models.Cita.objects.get(id=clave)
            cita.delete()
            return JsonResponse({'estado': 'eliminado'})   
        except models.Cita.DoesNotExist:
            return HttpResponseNotFound()
            
    # Cuando la petición es POST va a dar de alta los datos de la cita con la clave correspondiente y los datos enviados.
    # Esta operación se realiza en caso de que no exista un objeto con el número de id.
    if request.method == "POST":
        try:
            cita = models.Cita.objects.get(id=clave)
            return HttpResponseBadRequest()
        except models.Cita.DoesNotExist:
            estructura_base = set(campos_citas)
            registro = request.POST.dict()
            registro["id"] = str(clave)
            objeto = models.Cita()
            estructura_registro = set(registro)
            print(estructura_registro)
            print(estructura_base)
            if estructura_registro.issubset(estructura_base):
                print("holi")
                for campo in estructura_base:
                    if valida(registro[campo], campo):
                        if campos_citas[campo][0] is not str:
                            valor = eval(registro[campo])
                        else:
                            valor = registro[campo]
                        setattr(objeto, campo, valor)
                    else:
                        return HttpResponseBadRequest()
                objeto.save()
                return JsonResponse(registro)
            else:
                print("por aqui")
                return HttpResponseBadRequest()






def reglas_pacientes(valor, campo):
    """ Función que valida las reglas de negocio """
    if (campo in ("nombre", "apellidos", "telefono", "email") and (valor == "")):
        return False
    else:
        return True         


def valida_pacientes(dato, campo):
    """ Función que valida un dato con relación a su campo correspondiente."""
    tipo = campos_pacientes[campo][0]
    try:
        if tipo is not str:
            valor = eval(dato)
        else:
            valor = dato
        if type(valor) is tipo or (tipo is float and type(dato) is int):
            return reglas_pacientes(valor, campo)
        else:
            return False
    except:
        return False




@csrf_exempt
def clave_pacientes(request, clave):
    '''Función de vista que define un endpoint correspondiente a una clave de n dígitos.
    Opera con los métodos GET, POST, DELETE.'''
    # Cuando la petición es GET va a obtener los datos de la cita con la clave correrspondiente.
    # Esta operación se realiza en caso de que exista un objeto con el número de id.
    if request.method == "GET":
        try:
            paciente = models.Paciente.objects.get(id=clave) 
            return JsonResponse({campo:getattr(paciente, campo) for campo in campos_pacientes})
        # La excepción models.Paciente.DoesNotExist se desencadena cuando la búsqueda no arroje un resultado.
        except models.Paciente.DoesNotExist:
            return HttpResponseNotFound()

    # Cuando la petición es DELETE el paciente es eliminada de la base de datos.
    # Esta operación se realiza en caso de que exista un objeto con el id.
    if request.method == "DELETE":
        try:
            paciente = models.Paciente.objects.get(id=clave)
            paciente.delete()
            return JsonResponse({'estado': 'eliminado'})   
        except models.Paciente.DoesNotExist:
            return HttpResponseNotFound()
            
    # Cuando la petición es POST va a dar de alta los datos del paciente con la clave correspondiente y los datos enviados.
    # Esta operación se realiza en caso de que no exista un objeto con el número de id.
    if request.method == "POST":
        try:
            paciente = models.Paciente.objects.get(id=clave)
            return HttpResponseBadRequest()
        except models.Paciente.DoesNotExist:
            estructura_base = set(campos_pacientes)
            registro = request.POST.dict()
            registro["id"] = str(clave)
            objeto = models.Paciente()
            estructura_registro = set(registro)
            print(estructura_registro)
            print(estructura_base)
            if estructura_registro.issubset(estructura_base):
                for campo in estructura_base:
                    print(campo)
                    if valida_pacientes(registro[campo], campo):
                        if campos_pacientes[campo][0] is not str:
                            valor = eval(registro[campo])
                        else:
                            valor = registro[campo]
                        setattr(objeto, campo, valor)
                    else:
                        return HttpResponseBadRequest()
                objeto.save()
                return JsonResponse(registro)
            else:
                print("por aqui")
                return HttpResponseBadRequest()
