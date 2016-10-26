from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=True
    )

    def _str_(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(
        max_length=250,
        null=False,
        blank=True
    )

    apellido = models.CharField(
        max_length=250,
        null=False,
        blank=True
    )

    edad = models.IntegerField(
        default=0,
        null=False,
        blank=True
    )

    familia = models.ForeignKey(
        Familia,
        null=False,
        on_delete=models.CASCADE
    )

    def _str_(self):
        return "%s %s" % (self.nombre, self.apellido)
