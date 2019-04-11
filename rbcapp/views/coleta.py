# coding: utf-8

from rbcapp.models import Coleta, Substancia, Ponto_Monitoramento, Monitoramento, Rio, Bacia_Hidrografica, \
    Coleta_Substancia
from rbcapp.forms.coleta import FormColeta
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.db import connection
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Coleta_Listar(View):
    template = 'coleta/index.html'

    def get(self, request):
        rios = Rio.objects.all()
        bhs = Bacia_Hidrografica.objects.all()
        subs = Substancia.objects.all()
        coletas = Coleta.objects.all()
        col = []
        for coleta in coletas:
            sbs = {}
            ponto = Ponto_Monitoramento.objects.get(id=coleta.ponto_monitoramento.id)
            sbs['ponto_monitoramento'] = ponto
            sbs['data_coleta'] = coleta.data_coleta
            sbs['id'] = coleta.id
            rio = Rio.objects.get(id=ponto.rio.id)
            sbs['rio'] = rio.nome
            col.append(sbs)

        paginator = Paginator(col, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)

        return render(request, self.template, {'dados': dados, 'rios': rios, 'bhs': bhs, 'substancias': subs})

    def post(self, request):
        rio = request.POST['rio']
        pts = Ponto_Monitoramento.objects.filter(rio=rio)
        coletas = Coleta.objects.filter(ponto_monitoramento=pts)
        json = serializers.serialize('json', coletas)
        return HttpResponse(json)

class Coleta_Info(View):
    def get(self, request):
        import json
        coleta = Coleta.objects.filter(id=request.GET['id'])
        sql = '''select nome, valor_coletado
              from rbcapp_coleta, rbcapp_coleta_substancia, rbcapp_substancia
              where rbcapp_coleta_substancia.coleta_id='%s' and
              rbcapp_coleta_substancia.substancia_id=rbcapp_substancia.id and
              rbcapp_coleta.id='%s';
        '''%(coleta[0].id, coleta[0].id)
        cursor = connection.cursor()
        cursor.execute(sql)
        teste = cursor.fetchall()
        return JsonResponse(json.dumps(teste), safe=False)


class Coleta_Add(View):
    template = 'coleta/'

    def get(self, request):
        self.template += 'add.html'
        form = FormColeta()
        return render(request, self.template,
                      {'form': form, 'bhs': Bacia_Hidrografica.objects.all(), 'substancias': Substancia.objects.all()})

    def post(self, request):
        substancias = request.POST.getlist('substancia')
        valores_coletados = request.POST.getlist('valor_coletado')

        coleta = Coleta()
        coleta.data_coleta = request.POST['data_coleta']
        coleta.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
        coleta.save()

        for i in range(len(substancias)):
            coleta_substancia = Coleta_Substancia()
            coleta_substancia.coleta = Coleta.objects.get(pk=coleta.id)
            coleta_substancia.substancia = Substancia.objects.get(pk=substancias[i])
            coleta_substancia.valor_coletado = float(valores_coletados[i])
            coleta_substancia.save()

        monitoramento = Monitoramento()
        monitoramento.data_monitoramento = request.POST['data_coleta']
        monitoramento.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
        monitoramento.coleta = coleta
        monitoramento.save()

        calculo = Monitoramento.objects.get(pk=monitoramento.id)
        calculo.classificacao_iva = calculo.get_classificacao_iva()
        calculo.classificacao_iap = calculo.get_classificacao_iap()
        calculo.save()

        if "mon" in request.POST:
            return redirect('monitoramento_imagem', coleta= coleta.id)

        return redirect('coleta_listar')

class Coleta_Delete(View):
    def get(self, request, coleta_id=None):
        coleta = Coleta.objects.get(pk=coleta_id)
        if coleta.id != None:
            coleta.delete()
        return redirect('coleta_listar')

    def post(self, request, coleta_id=None):
        coleta = Coleta.objects.get(pk=coleta_id)
        if coleta.id != None:
            coleta.delete()
        return redirect('coleta_listar')