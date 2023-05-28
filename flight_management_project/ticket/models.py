from django.db import models

# Create your models here.
class tiquete(models.Model):
    id_cliente = models.CharField(max_length=20) # El ID del cliente que compró el tiquete
    id_vuelo = models.CharField(max_length=20) #se van a desplegat todos los vuelos registrados en la base de datos con sus datos para que la persona escoja el que quiere abajo en una tabla
    grupo = models.CharField(max_length=1)
    asiento = models.CharField(max_length=10)
    categoria_pasajero = models.CharField(max_length=20)
    equipaje_mano = models.CharField(max_length=50)
    equipaje_bodega = models.CharField(max_length=50)

    def __str__(self):
        return f'Ticket #{self.id}'