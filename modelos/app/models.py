# -*- encoding: utf-8 -*-
from django.db import models

#à
class Especie(models.Model):
    tipo = models.CharField(max_length=200)
    habitat = models.CharField(max_length=50)
    zona = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tipo

class Pato(models.Model):  
    bd = models.DateTimeField()
    nombre = models.CharField(max_length=100)
    SETXO_CHOICES = (
        (1, 'Masculino'),
        (2, 'Femenino')
    )
    sexo = models.IntegerField(choices=SETXO_CHOICES)
    curp = models.CharField(unique=True, max_length=20)
    especie = models.ForeignKey(Especie)

    def __unicode__(self):
        return self.nombre
