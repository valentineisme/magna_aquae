# coding: utf-8

from django.db import models
from rio import Rio


class Ponto_Monitoramento(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    rio = models.ForeignKey(Rio)

    def __unicode__(self):
        # return str(self.id) + ' - (' + str(self.latitude) + ', ' + str(self.longitude) + ')'
        return '(' + str(self.latitude) + ', ' + str(self.longitude) + ')'