# coding: utf-8

from django.db import models
from entorno import Entorno
from monitoramento import Monitoramento

class Solucao(models.Model):
    monitoramento = models.ForeignKey(Monitoramento)
    entorno = models.ForeignKey(Entorno)
    risco = models.CharField(max_length=1)
    solucao_sugerida = models.TextField()