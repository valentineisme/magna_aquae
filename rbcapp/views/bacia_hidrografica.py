# coding: utf-8

from rbcapp.models import Bacia_Hidrografica
from rbcapp.forms.bacia_hidrografica import FormBaciaHidrografica
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Bacia_Hidrografica_Listar(View):
     
    def get(self, request):
        form = FormBaciaHidrografica()
        bh = Bacia_Hidrografica.objects.all()
        paginator = Paginator(bh, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)

        return render(request, 'bacia_hidrografica/index.html', {'dados': dados, 'form': form})
    
    def post(self, request):
        bh = Bacia_Hidrografica.objects.all()
        return render(request, 'bacia_hidrografica/index.html', {'dados': bh})


class Bacia_Hidrografica_Add(View):
    
    # template = 'bacia_hidrografica/'
    # def get(self, request):
    #     self.template += 'add.html'
    #     form = FormBaciaHidrografica()
    #     return render(request, self.template, {'form':form})
    
    def post(self, request):
        form = FormBaciaHidrografica(request.POST)
        if form.is_valid():
            bh = Bacia_Hidrografica()
            bh.nome = request.POST['nome']
            bh.save()
        return redirect('bacia_hidrografica_listar')


class Bacia_Hidrografica_Edit(View):
    def get(self, request):
        bh_id = request.GET['bacia']
        bh = Bacia_Hidrografica.objects.filter(id=bh_id)
        json = serializers.serialize("json", bh)
        return HttpResponse(json)
    
    def post(self, request):
        bh_id = request.POST['bh_id']
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        form = FormBaciaHidrografica(request.POST)
        if form.is_valid():
            bh.nome = request.POST['nome']
            bh.save()
        return redirect('bacia_hidrografica_listar')


class Bacia_Hidrografica_Delete(View):
    def get(self, request, bh_id=None):
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        if bh.id != None:
            bh.delete()
        return redirect('bacia_hidrografica_listar')
    
    def post(self, request, bh_id=None):
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        if bh.id != None:
            bh.delete()
        return redirect('bacia_hidrografica_listar')
