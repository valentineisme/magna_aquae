# coding: utf-8

from rbcapp.models import Ponto_Monitoramento, Rio, Bacia_Hidrografica
from rbcapp.forms.ponto import FormPonto
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Ponto_Listar(View):
    template = 'ponto/index.html'

    def get(self, request):
        rios = Rio.objects.all()
        bhs = Bacia_Hidrografica.objects.all()
        ponto = Ponto_Monitoramento.objects.all()
        paginator = Paginator(ponto, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, self.template, {'rios': rios, 'bhs': bhs, 'dados': dados})

    def post(self, request):
        id = request.POST['ponto']
        pontos = Ponto_Monitoramento.objects.filter(rio=id)
        json = serializers.serialize("json", pontos)
        return HttpResponse(json)

class Ponto_Add(View):
    template = 'ponto/'

    def get(self, request):
        pass

    def post(self, request):
        template = '/ponto/'
        form = FormPonto(request.POST)
        if form.is_valid():
            ponto = Ponto_Monitoramento()
            ponto.latitude = request.POST['latitude']
            ponto.longitude = request.POST['longitude']
            ponto.rio = Rio.objects.get(pk=request.POST['rio'])
            ponto.save()
        return redirect(template)

class Ponto_Edit(View):
    template = 'ponto/'

    def get(self, request):
        ponto_id = request.GET['ponto_id']
        ponto = Ponto_Monitoramento.objects.filter(id=ponto_id)
        json = serializers.serialize("json", ponto)
        return HttpResponse(json)

    def post(self, request):
        ponto_id = request.POST['ponto_id']
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        ponto.latitude = request.POST['latitude']
        ponto.longitude = request.POST['longitude']
        # ponto.rio = Rio.objects.get(pk=request.POST['rio'])
        ponto.save()
        return redirect('ponto_listar')

class Ponto_Delete(View):
    template = '/ponto/'

    def get(self, request, ponto_id=None):
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        if ponto.id != None:
            ponto.delete()
        return redirect(self.template)

    def post(self, request, ponto_id=None):
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        if ponto.id != None:
            ponto.delete()
        return redirect(self.template)
