# coding: utf-8

from django.db import models

class Substancia(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome
