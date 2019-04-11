# coding: utf-8

from django.db import models
from PIL import Image
from rbcapp.models import Ponto_Monitoramento, Coleta

class Imagem(models.Model):
    titulo = models.CharField(max_length=150)
    ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
    coleta = models.ForeignKey(Coleta, blank=True, null=True)
    data_emissao = models.DateField()
    imagem = models.ImageField(upload_to="imagem/")