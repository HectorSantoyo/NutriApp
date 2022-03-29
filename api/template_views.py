from .models import Cita, Paciente
from .forms import FormaCitas, FormaPacientes
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from requests import post
from . import models
from django.db.models import Max
from django.contrib.auth.decorators  import login_required

campos_citas = (
    "nombre_paciente", 
    "apellidos", 
    "fecha", 
    "hora",
    "lugar",
    "id"
    )

campos_pacientes = (
    'nombre',
    'apellidos', 
    'telefono', 
    'email',
    'id')
@login_required
def index(request):
    return render(request, 'base.html')



@login_required
def vista_citas_fecha(request):
    try: 
        if request.method == "GET":
            fecha = request.GET.get('date')
            lista = [[(campo, getattr(cita, campo)) for campo in campos_citas] for cita in Cita.objects.filter(fecha=fecha)]
            contexto = {'lista': lista}
            return render(request, 'listado_citas.html', contexto)
    except:
        lista = [[(campo, getattr(cita, campo)) for campo in campos_citas] for cita in Cita.objects.all()]
        contexto = {'lista': lista}
        return render(request, 'listado_citas.html', contexto)




@login_required
def vista_citas(request):
    lista = [[(campo, getattr(cita, campo)) for campo in campos_citas] for cita in Cita.objects.all()]
    contexto = {'lista': lista}
    return render(request, 'listado_citas.html', contexto) 

@login_required
def valida_citas(request):
    lista = [[getattr(cita, campo) for campo in campos_citas] for cita in Cita.objects.all()]
    contexto = {'lista': lista}
    return render(request, 'valida.html', contexto)

@login_required
def vista_pacientes(request):
    lista = [[(campo, getattr(paciente, campo)) for campo in campos_pacientes] for paciente in Paciente.objects.all()]
    contexto = {'lista': lista}
    return render(request, 'listado_pacientes.html', contexto) 

@login_required
def valida_pacientes(request):
    lista = [[getattr(paciente, campo) for campo in campos_pacientes] for paciente in Paciente.objects.all()]
    contexto = {'lista': lista}
    return render(request, 'valida.html', contexto)


@login_required
def forma_citas(request):
    if request.method == 'POST':
        forma = FormaCitas(request.POST)
        if forma.is_valid():
            datos = request.POST.dict()
            print(datos)
            id_col = Cita.objects.aggregate(Max('id'))
            id = id_col['id__max'] + 1
            datos.pop('csrfmiddlewaretoken')
            resultado = post('http://' + request.get_host() + '/api/vista_citas/{}'.format(id), data=datos)
            if resultado.status_code == 200:
                #return HttpResponse('<h1>¡Alta Exitosa!</h1>')
                lista = [[(campo, getattr(cita, campo)) for campo in campos_citas] for cita in Cita.objects.all()]
                contexto = {'lista': lista, 'alta': '¡Alta Exitosa!', 'id': id}
                return render(request, 'listado_citas.html', contexto)
            else: 
                return HttpResponse('<h1>Ocurrió un error en el alta.</h1>')
    else:
        forma = FormaCitas()
    return render(request, 'forma_citas.html', {'forma': forma})

@login_required
def forma_pacientes(request):
    if request.method == 'POST':
        forma = FormaPacientes(request.POST)
        if forma.is_valid():
            datos = request.POST.dict()
            print(datos)
            id_col = Paciente.objects.aggregate(Max('id'))
            id = id_col['id__max'] + 1
            datos.pop('csrfmiddlewaretoken')
            resultado = post('http://' + request.get_host() + '/api/vista_pacientes/{}'.format(id), data=datos)
            if resultado.status_code == 200:
                #return HttpResponse('<h1>¡Alta Exitosa!</h1>') 
                lista = [[(campo, getattr(paciente, campo)) for campo in campos_pacientes] for paciente in Paciente.objects.all()]
                contexto = {'lista': lista, 'alta': '¡Alta Exitosa!', 'id': id}
                return render(request, 'listado_pacientes.html', contexto)   
            else: 
                return HttpResponse('<h1>Ocurrió un error en el alta.</h1>')
    else:
        forma = FormaPacientes()
    return render(request, 'forma_pacientes.html', {'forma': forma})