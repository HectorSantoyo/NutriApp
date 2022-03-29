from django.db import models

class Cita(models.Model):
    #numero_de_cuenta = models.PositiveIntegerField(unique=True)
    nombre_paciente = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=50)

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    email = models.EmailField(default=0)
    
