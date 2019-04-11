# coding: utf-8

from django.db import models
from coleta import Coleta
from substancia import Substancia

class Coleta_Substancia(models.Model):
    coleta = models.ForeignKey(Coleta)
    substancia = models.ForeignKey(Substancia)
    valor_coletado = models.FloatField()