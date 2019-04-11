# coding: utf-8

from rbcapp.models import Rio, Ponto_Monitoramento, Coleta, Casos
from rbcapp.forms.caso import FormCaso
from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.core import serializers

class Ajax_Pesquisa(View):
    def get(self, request):
        if 'bh' in request.GET:
            id = request.GET['bh']
            rios = Rio.objects.filter(bacia_hidrografica=id)
            json = serializers.serialize("json", rios)
            return HttpResponse(json)
        elif 'rio' in request.GET:
            id = request.GET['rio']
            pontos = Ponto_Monitoramento.objects.filter(rio=id)
            json = serializers.serialize("json", pontos)
            return HttpResponse(json)
        elif 'coleta' in request.GET:
            coleta = Coleta.objects.filter(ponto_monitoramento=request.GET['ponto'])
            json = serializers.serialize("json", coleta)
            return HttpResponse(json)
        elif 'caso' in request.GET:
            caso = Casos.objects.filter(id=request.GET['caso'])
            json = serializers.serialize("json", caso)
            return HttpResponse(json)

    def post(self, request):
        pass