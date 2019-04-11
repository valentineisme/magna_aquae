# coding: utf-8

from rbcapp.models import Bacia_Hidrografica, Imagem, Entorno, Monitoramento, Ponto_Monitoramento, Rio, Casos, Coleta
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.db import connection
from django.core import serializers

class Monitoramento_Localizacao(View):
    def get(self, request):
        bhs = Bacia_Hidrografica.objects.all()
        return render(request, 'monitoramento/localizacao.html', {'bhs': bhs})
    
    def post(self, request):
        return redirect('monitoramento_imagem', coleta=request.POST['coleta'])


class Monitoramento_Imagem(View):
    def get(self, request, coleta=None):
        imgs = Imagem.objects.filter(coleta=coleta)
        monitoramento = Monitoramento.objects.get(coleta=coleta)
        return render(request, 'monitoramento/imagem.html', {'imgs': imgs, 'monitoramento': monitoramento})

    def post(self, request):
        pass


class Monitoramento_Entorno(View):
    def get(self, request):
        imagem = request.GET['imagem']
        img = Imagem.objects.get(id=imagem)
        entornos = Entorno.objects.all()
        monitoramento = request.GET['monitoramento']
        return render(request, 'monitoramento/entorno.html',
                      {'img': img, 'entornos': entornos, 'monitoramento': monitoramento})
    
    def post(self, request):
        entornos = Entorno.objects.all()
        monitoramento = request.POST['monitoramento']
        mon = Monitoramento.objects.get(id=monitoramento)
        img = Imagem()
        img.titulo = request.POST['titulo']
        img.ponto_monitoramento = Ponto_Monitoramento.objects.get(id=mon.ponto_monitoramento.id)
        img.data_emissao = request.POST['data_emissao']
        img.coleta = Coleta.objects.get(id=mon.coleta.id)
        img.imagem = request.FILES['imagem']
        img.save()
        return render(request, 'monitoramento/entorno.html',
                      {'img': img, 'entornos': entornos, 'monitoramento': monitoramento})
        


class Monitoramento_Solucao(View):
    def get(self, request):
        if 'entorno' in request.GET:
            entorno = request.GET['entorno']
            monitoramento = request.GET['monitoramento']
            img = request.GET['imagem']

            sql = '''SELECT r.id, r.solucao_sugerida, r.risco FROM rbcapp_casos r
            				INNER JOIN rbcapp_entorno e ON e.id = r.entorno_id WHERE e.id = %d
            				AND r.classificacao_iap = (SELECT classificacao_iap FROM rbcapp_monitoramento WHERE id = %d)
            	 			AND r.classificacao_iva = (SELECT classificacao_iva FROM rbcapp_monitoramento WHERE id = %d)
            	 			''' % (int(entorno), int(monitoramento), int(monitoramento))
            cursor = connection.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()

            mon = Monitoramento.objects.get(id=monitoramento)
            ponto = Ponto_Monitoramento.objects.get(id=mon.ponto_monitoramento.id)
            rio = Rio.objects.get(id=ponto.rio.id)
            en = Entorno.objects.get(id=entorno)

            return render(request, 'monitoramento/solucao.html',
                          {'resultados': resultado, 'rio': rio.nome, 'monitoramento': mon, 'entorno': en, 'img': img})
        
    def post(self, request):
        if 'caso_id' in request.POST:
            img = Imagem.objects.get(id=request.POST['imagem'])
            monitoramento_id = request.POST['monitoramento']
            monitoramento = Monitoramento.objects.get(pk=monitoramento_id)
            entorno = Entorno.objects.get(id=request.POST['entorno'])
            caso = Casos()

            if request.POST['caso_id'] != '':
                caso_id = Casos.objects.get(id=request.POST['caso_id'])
                caso_original = Casos.objects.get(pk=caso_id.id)
                caso.classificacao_iap = caso_original.classificacao_iap
                caso.classificacao_iva = caso_original.classificacao_iva
                caso.entorno = entorno
                caso.risco = request.POST['risco']
                caso.solucao_sugerida = request.POST['solucao_sugerida']
                caso.save()
            else:
                caso.classificacao_iap = monitoramento.classificacao_iap
                caso.classificacao_iva = monitoramento.classificacao_iva
                caso.entorno = entorno
                caso.risco = request.POST['risco']
                caso.solucao_sugerida = request.POST['solucao_sugerida']
                caso.save()

            monitoramento.solucao_sugerida = caso.solucao_sugerida
            monitoramento.risco = caso.risco
            monitoramento.entorno = entorno
            monitoramento.imagem = img
            monitoramento.save()
            return redirect('index')
        else:
            img = Imagem.objects.get(id=request.POST['imagem'])
            caso_id = Casos.objects.get(id=request.POST['caso'])
            monitoramento_id = request.POST['monitoramento']
            entorno = Entorno.objects.get(id=request.POST['entorno'])
            caso = Casos.objects.get(pk=caso_id.id)
            monitoramento = Monitoramento.objects.get(pk=monitoramento_id)
            monitoramento.solucao_sugerida = caso.solucao_sugerida
            monitoramento.risco = caso.risco
            monitoramento.entorno = entorno
            monitoramento.imagem = img
            monitoramento.save()
            return redirect('index')
