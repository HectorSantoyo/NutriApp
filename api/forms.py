from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django import forms
from django.forms.widgets import NumberInput, TextInput
import datetime as dt

lugares =(('Consultorio Jani', 'Consultorio Jani'), 
           ('Hospital Santa Ana', 'Hospital Santa Ana'), 
           ('Online', 'Online'))

HOUR_CHOICES = [(None, '------')] + [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 23)]


class FormaCitas(forms.Form):
    nombre_paciente = forms.CharField(max_length=50, 
                             label='Nombre paciente')
    apellidos = forms.CharField(max_length=50, 
                                      label='Apellidos')
    fecha = forms.DateField(label='Fecha', widget=NumberInput(attrs={'type':'date'}))
    print(HOUR_CHOICES)
    hora = forms.ChoiceField(label='Hora', choices=HOUR_CHOICES) 
    lugar = forms.ChoiceField(label='Lugar', choices=lugares )


class FormaPacientes(forms.Form):
    nombre = forms.CharField(max_length=50, 
                             label='Nombre paciente')
    apellidos = forms.CharField(max_length=50, 
                                      label='Apellidos')
    telefono = forms.CharField(max_length=10,  min_length=10, widget=TextInput(attrs={'type':'number', 'placeholder': '0123456789'})) 
    #telefono = forms.IntegerField(label='Telefono', widget=NumberInput(attrs={'type':'phone'}))     
    #                        label='Telefono')
    #telefono = forms.RegexField(regex=r'^[0-9]{4}$', label='Telefono', default='x')
    #r'^[0-9]+$' ^\d{9,12}$
    #telefono = forms.PhoneField(label="Telefono")
    email = forms.EmailField(label='email') 

