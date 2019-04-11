# coding: utf-8

from rbcapp.models import Casos, Monitoramento, Entorno
from rbcapp.forms.caso import FormCaso
from rbcapp.forms.pesquisa import FormPesquisa
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Caso_Listar(View):
    template = 'caso/index.html'

    @method_decorator(login_required)
    def get(self, request):
        casos = Casos.objects.order_by('classificacao_iap', 'classificacao_iva', 'entorno', 'risco').all()
        form = FormCaso()
        paginator = Paginator(casos, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)
        return render(request, self.template, {'dados': dados, 'form': form})

    def post(self, request):
        casos = Casos.objects.order_by('classificacao_iap', 'classificacao_iva', 'entorno', 'risco').all()
        return render(request, self.template, {'dados': casos})


class Caso_Add(View):
    template = 'caso/'

    @method_decorator(login_required)
    def get(self, request):
        self.template += 'add.html'
        form = FormCaso()
        return render(request, self.template, {'form': form})

    def post(self, request):
        template = '/caso/'
        form = FormCaso(request.POST)
        if form.is_valid():
            caso = Casos()
            caso.classificacao_iap = request.POST['iap']
            caso.classificacao_iva = request.POST['iva']
            caso.entorno = Entorno.objects.get(pk=request.POST['entorno'])
            caso.risco = request.POST['risco']
            caso.solucao_sugerida = request.POST['solucao_sugerida']
            caso.save()
        return redirect(template)


# class Caso_Edit(View):
#     template = 'caso/'
#
#     def get(self, request, caso_id=None):
#         self.template += 'edit.html/'
#         caso = Casos.objects.get(pk=caso_id)
#         form = FormCaso(initial={'iap': caso.classificacao_iap, 'iva': caso.classificacao_iva, 'risco': caso.risco,
#                                  'entorno': caso.entorno, 'solucao_sugerida': caso.solucao_sugerida})
#         return render(request, self.template, {'form': form, 'caso_id': caso.id})
#
#     def post(self, request, caso_id=None):
#         template = '/caso/'
#         caso = Casos.objects.get(pk=caso_id)
#         form = FormCaso(request.POST)
#         if form.is_valid():
#             caso.classificacao_iap = request.POST['iap']
#             caso.classificacao_iva = request.POST['iva']
#             caso.entorno = Entorno.objects.get(pk=request.POST['entorno'])
#             caso.risco = request.POST['risco']
#             caso.solucao_sugerida = request.POST['solucao_sugerida']
#             caso.save()
#         return redirect(template)


class Caso_Delete(View):
    template = '/caso/'

    def get(self, request, caso_id=None):
        caso = Casos.objects.get(pk=caso_id)
        if caso.id != None:
            caso.delete()
        return redirect(self.template)

    def post(self, request, caso_id=None):
        caso = Casos.objects.get(pk=caso_id)
        if caso.id != None:
            caso.delete()
        return redirect(self.template)


class Caso_Pesquisar(View):
    
    def get(self, request):
        form = FormPesquisa()
        return render(request, 'caso/pesquisar.html', {'form': form})

    def post(self, request):
        resultado = {}
        montioramento = ''
        monitoramento = request.POST.get('monitoramento')
        entorno = request.POST.get('entorno')

        if monitoramento is not None and entorno is not None:
            sql = '''SELECT r.id, r.solucao_sugerida, r.risco FROM rbcapp_casos r
        				INNER JOIN rbcapp_entorno e ON e.id = r.entorno_id WHERE e.id = %d
        				AND r.classificacao_iap = (SELECT classificacao_iap FROM rbcapp_monitoramento WHERE id = %d)
        	 			AND r.classificacao_iva = (SELECT classificacao_iva FROM rbcapp_monitoramento WHERE id = %d)
        	 			''' % (int(entorno), int(monitoramento), int(monitoramento))

            resultado['solucao'] = list(Casos.objects.raw(sql))
            resultado['monitoramento'] = monitoramento

        return render(request, 'caso/resultado.html', {'resultado': resultado})
