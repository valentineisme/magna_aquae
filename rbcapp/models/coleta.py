# coding: utf-8

from django.db import models
from ponto_monitoramento import Ponto_Monitoramento
from substancia import Substancia
class Coleta(models.Model):
    # id = models.AutoField(verbose_name='id', serialize=False, auto_created=True, primary_key=True)
    substancia = models.ManyToManyField(Substancia, through='Coleta_Substancia')
    ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
    data_coleta = models.DateField('Data da Coleta')

    def __unicode__(self):
        return unicode(self.data_coleta)
