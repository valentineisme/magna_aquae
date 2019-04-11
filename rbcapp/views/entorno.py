# coding: utf-8

from rbcapp.forms.entorno import FormEntorno
from rbcapp.models import Entorno
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Entorno_Listar(View):
    template = 'entorno/index.html'

    def get(self, request):
        entornos = Entorno.objects.all()
        paginator = Paginator(entornos, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, self.template, {'dados': dados})

    def post(self, request):
        entornos = Entorno.objects.all()
        return render(request, self.template, {'dados': entornos})

class Entorno_Add(View):
    template = 'entorno/'

    def get(self, request):
        self.template += 'add.html'
        form = FormEntorno()
        return render(request, self.template, {'form': form})

    def post(self, request):
        template = '/entorno/'
        form = FormEntorno(request.POST)
        if form.is_valid():
            entorno = Entorno()
            entorno.variavel_entorno = request.POST['variavel_entorno']
            entorno.cor_hex = request.POST['cor']
            entorno.save()
        return redirect(template)


class Entorno_Edit(View):
    template = 'entorno/'

    def get(self, request, entorno_id=None):
        self.template += 'edit.html/'
        entorno = Entorno.objects.get(pk=entorno_id)
        form = FormEntorno(initial={'variavel_entorno': entorno.variavel_entorno})
        return render(request, self.template, {'form': form, 'entorno_id': entorno.id})

    def post(self, request, entorno_id=None):
        template = '/entorno/'
        entorno = Entorno.objects.get(pk=entorno_id)
        form = FormEntorno(request.POST)
        if form.is_valid():
            entorno.variavel_entorno = request.POST['variavel_entorno']
            entorno.save()
        return redirect(template)


class Entorno_Delete(View):
    template = '/entorno/'

    def get(self, request, entorno_id=None):
        entorno = Entorno.objects.get(pk=entorno_id)
        if entorno.id != None:
            entorno.delete()
        return redirect(self.template)

    def post(self, request, entorno_id=None):
        entorno = Entorno.objects.get(pk=entorno_id)
        if entorno.id != None:
            entorno.delete()
        return redirect(self.template)
