#coding: utf-8

from django.db import models
from entorno import Entorno

class Casos(models.Model):
    classificacao_iap = models.CharField(max_length=45)
    classificacao_iva = models.CharField(max_length=45)
    risco = models.CharField(max_length=1)
    solucao_sugerida = models.TextField()
    entorno = models.ForeignKey(Entorno)

    def __unicode__(self):
        return self.solucao_sugerida