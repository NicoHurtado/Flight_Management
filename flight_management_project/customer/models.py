from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# Create your models here.
