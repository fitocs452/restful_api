from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    fechaOrigen = models.DateField(auto_now=False, auto_now_add=False)


class Automovil(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    modelo = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(2016),
            MinValueValidator(1975)
        ]
    )
    linea = models.CharField(max_length=50)
    placa = models.CharField(max_length=50)
    polarizado = models.BooleanField()
