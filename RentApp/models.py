# Recordatorio, las clases deben ser en Singular
from django.db import models

class Vehiculos(models.Model):
    patente = models.CharField(max_length=11)
    marca = models.CharField(max_length=40)
    tipo = models.CharField(max_length=4)
    anio = models.IntegerField(verbose_name="Año")
    arrendado = models.BooleanField(default=False)

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    email = models.EmailField()

class Arriendos(models.Model):
    f_inicio = models.DateField()
    f_fin = models.DateField()
    idVehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE, null = True) # FK Vehiculo
    idCliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null = True) # FK Cliente