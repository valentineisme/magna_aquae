# coding: utf-8

from rbcapp.models import Rio, Bacia_Hidrografica
from rbcapp.forms.rio import FormRio
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Rio_Listar(View):
    template = 'rio/index.html'

    def get(self, request):
        form = FormRio()
        rios = Rio.objects.all()
        bhs = Bacia_Hidrografica.objects.all()
        paginator = Paginator(rios, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, self.template, {'dados': dados, 'form': form, 'bhs': bhs})

    def post(self, request):
        bh = request.POST['bh']
        rios = Rio.objects.filter(bacia_hidrografica=bh).only('nome', 'dimensao', 'bacia_hidrografica')
        json = serializers.serialize("json", rios)
        return HttpResponse(json)


class Rio_Add(View):
    template = 'rio/'

    def get(self, request):
        self.template += 'add.html'
        form = FormRio()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = FormRio(request.POST)
        if form.is_valid():
            rio = Rio()
            rio.nome = request.POST['nome']
            rio.dimensao = request.POST['dimensao']
            rio.bacia_hidrografica = Bacia_Hidrografica.objects.get(pk=request.POST['bacia_hidrografica'])
            rio.save()
        return redirect('rio_listar')

class Rio_Edit(View):
    template = 'rio/'

    def get(self, request):
        rio_id = request.GET['rio_id']
        rio = Rio.objects.filter(id=rio_id)
        json = serializers.serialize("json", rio)
        return HttpResponse(json)

    def post(self, request):
        rio_id = request.POST['rio_id']
        rio = Rio.objects.get(pk=rio_id)
        rio.nome = request.POST['nome']
        rio.dimensao = request.POST['dimensao']
        rio.save()
        return redirect('rio_listar')

class Rio_Delete(View):
    template = '/rio/'

    def get(self, request, rio_id=None):
        rio = Rio.objects.get(pk=rio_id)
        if rio.id != None:
            rio.delete()
        return redirect(self.template)

    def post(self, request, rio_id=None):
        rio = Rio.objects.get(pk=rio_id)
        if rio.id != None:
            rio.delete()
        return redirect(self.template)
