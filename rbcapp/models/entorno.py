# coding: utf-8

from django.db import models


class Entorno(models.Model):
    variavel_entorno = models.CharField(max_length=45)
    cor = models.CharField(max_length=16)

    def __unicode__(self):
        return self.variavel_entorno
