# coding: utf-8

from django.db import models
from bacia_hidrografica import Bacia_Hidrografica


class Rio(models.Model):
    nome = models.CharField(max_length=150)
    dimensao = models.FloatField()
    bacia_hidrografica = models.ForeignKey(Bacia_Hidrografica)

    def __unicode__(self):
        return self.nome
