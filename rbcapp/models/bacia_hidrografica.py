# coding: utf-8

from django.db import models


class Bacia_Hidrografica(models.Model):
    nome = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nome
