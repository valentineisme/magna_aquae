# coding: utf-8

from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from django.views.generic.base import View
from rbcapp.models import Bacia_Hidrografica, Imagem, Ponto_Monitoramento, Coleta, Rio


class Imagem_Listar(View):
    def get(self, request):
        bhs = Bacia_Hidrografica.objects.all()
        imgs = Imagem.objects.all()
        imagens = []
        for imagem in imgs:
            rio = Ponto_Monitoramento.objects.get(id=imagem.ponto_monitoramento_id)
            im = {}
            im['id'] = imagem.id
            im['titulo'] = imagem.titulo
            im['imagem'] = imagem.imagem
            im['data_emissao'] = imagem.data_emissao
            im['ponto_monitoramento'] = imagem.ponto_monitoramento
            im['rio'] = Rio.objects.get(id=rio.rio.id)
            imagens.append(im)
        return render(request, 'imagem/index.html', {'bhs': bhs, 'imgs': imagens})
    
    def post(self, request):
        if request.POST['rio'] == "imgs":
            imgs = Imagem.objects.all()
            json = serializers.serialize("json", imgs)
            return HttpResponse(json)
        else:
            # if Ponto_Monitoramento.objects.filter(rio=request.POST['rio']).exists():
            pontos = Ponto_Monitoramento.objects.get(rio=request.POST['rio'])
            imgs = Imagem.objects.filter(ponto_monitoramento=pontos)
            json = serializers.serialize("json", imgs)
            return HttpResponse(json)


class Imagem_Add(View):
    def get(self, request):
        coleta = Coleta.objects.filter(ponto_monitoramento=request.GET['ponto'])
        json = serializers.serialize("json", coleta)
        return HttpResponse(json)
    
    def post(self, request):
        imagem = Imagem()
        imagem.titulo = request.POST['titulo']
        imagem.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
        imagem.data_emissao = request.POST['data_emissao']
        if request.POST['coleta'] != 'selecione':
            imagem.coleta = Coleta.objects.get(id=request.POST['coleta'])
        imagem.imagem = request.FILES['imagem']
        imagem.save()
        return redirect('imagem_listar')


class Imagem_Edit(View):
    def get(self, request):
        return render(request, 'imagem/index.html')
    
    def post(self, request):
        return render(request, 'imagem/index.html')


class Imagem_Delete(View):
        
    def get(self, request, img_id=None):
        imagem = Imagem.objects.get(pk=img_id)
        if imagem.id != None:
            imagem.delete()
        return redirect('imagem_listar')
    
    def post(self, request, img_id=None):
        imagem = Imagem.objects.get(pk=img_id)
        if imagem.id != None:
            imagem.delete()
        return redirect('imagem_listar')