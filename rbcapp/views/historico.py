# coding: utf-8

from rbcapp.models import Ponto_Monitoramento, Coleta, Rio, Bacia_Hidrografica, Imagem, Monitoramento
from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Historico_Listar(View):
    def get(self, request):
        coletas = Coleta.objects.all()
        pontos = []
        for coleta in coletas:
            pt = {}
            ponto = Ponto_Monitoramento.objects.get(id=coleta.ponto_monitoramento.id)
            rio = Rio.objects.get(id=ponto.rio.id)
            bacia = Bacia_Hidrografica.objects.get(id=rio.bacia_hidrografica.id)
            pt['id'] = ponto.id
            pt['ponto'] = ponto
            pt['rio'] = rio.nome
            pt['bacia'] = bacia.nome
            pontos.append(pt)
        paginator = Paginator(pontos, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, 'historico/index.html', {'pontos': dados})
    
    def post(self, requests):
        pass

class Historico_Detalhes(View):
    def get(self, request, ponto_id=None):
        ponto = Ponto_Monitoramento.objects.get(id=ponto_id)
        imgs = Imagem.objects.filter(ponto_monitoramento=ponto_id)
        imagens = []
        for img in imgs:
            im = {}
            if Monitoramento.objects.filter(imagem=img).exists():
                mon = Monitoramento.objects.get(imagem=img)
                im['iva'] = mon.classificacao_iva
                im['iap'] = mon.classificacao_iap
                im['entorno'] = mon.entorno
                im['risco'] = mon.risco
                im['solucao'] = mon.solucao_sugerida
                im['coleta'] = img.coleta
            im['titulo'] = img.titulo
            im['data_emissao'] = img.data_emissao
            im['imagem'] = img.imagem
            imagens.append(im)
        return render(request, 'historico/detalhes.html', {'ponto': ponto, 'imgs': imagens})
    
    def post(self, request):
        pass