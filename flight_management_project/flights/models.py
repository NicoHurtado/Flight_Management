from django.db import models
from django.db import models


class Aeropuerto(models.Model):
    codigo_aeropuerto = models.CharField(max_length=3)
    nombre_aeropuerto = models.CharField(max_length=100)
    nombre_ciudad = models.CharField(max_length=100)
    id_ciudad = models.CharField(max_length=20)
    nombre_pais = models.CharField(max_length=100)
    id_pais = models.CharField(max_length=20)

    def __str__(self):
        return self.codigo_aeropuerto


class Aerolinea(models.Model):
    codigo_aerolinea = models.CharField(max_length=3)
    nombre_aerolinea = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo_aerolinea


class Ticket(models.Model):
    id_vuelo = models.CharField(max_length=20)
    aerolinea = models.CharField(max_length=100)
    codigo_iata_salida = models.CharField(max_length=3)
    codigo_iata_llegada = models.CharField(max_length=3)
    id_pais_salida = models.CharField(max_length=20)
    id_pais_llegada = models.CharField(max_length=20)
    id_ciudad_salida = models.CharField(max_length=20)
    id_ciudad_llegada = models.CharField(max_length=20)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    categoria_vuelo = models.CharField(max_length=100)

    def __str__(self):
        return f"Ticket {self.id}"
# Create your models here.
