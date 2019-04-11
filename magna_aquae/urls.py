"""magna_aquae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from rbcapp.views import Ajax_Pesquisa, Index, Login_Usuario, Logout_Usuario, Acessar_Conta, Recuperar_Senha, \
Bacia_Hidrografica_Listar, Bacia_Hidrografica_Add, Bacia_Hidrografica_Edit, Bacia_Hidrografica_Delete, \
Rio_Listar, Rio_Add, Rio_Edit, Rio_Delete, Ponto_Listar, Ponto_Add, Ponto_Edit, Ponto_Delete, \
Coleta_Listar, Coleta_Add, Coleta_Info, Coleta_Delete, Caso_Listar, Caso_Add, Caso_Delete, Caso_Pesquisar, \
Entorno_Listar, Entorno_Add, Entorno_Edit, Entorno_Delete, Imagem_Listar, Imagem_Add, Imagem_Edit, Imagem_Delete, \
Monitoramento_Localizacao, Monitoramento_Imagem, Monitoramento_Entorno, Monitoramento_Solucao, Historico_Listar, Historico_Detalhes
from django.contrib.auth.decorators import login_required

login_template = '/login'

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    #home
    url(r'^$', Index.as_view(), name='index'),

    #ajax
    url(r'^ajax/pesquisa/$', Ajax_Pesquisa.as_view(), name='ajax_pesqusia'),

    #usuario
    url(r'^login$', Login_Usuario.as_view(), name='login'),
    url(r'^logout/$', Logout_Usuario.as_view(), name='logout'),
    url(r'^acessarConta/$', login_required(Acessar_Conta.as_view(), login_url=login_template), name='acessar_conta'),
    url(r'^recuperarSenha/$', Recuperar_Senha.as_view(), name='recuperar_senha'),

    #Bacia Hidrografica
    url(r'^bacia-hidrografica/$', login_required(Bacia_Hidrografica_Listar.as_view(), login_url=login_template), name='bacia_hidrografica_listar'),
    url(r'^bacia-hidrografica/add/$', login_required(Bacia_Hidrografica_Add.as_view(), login_url=login_template), name='bacia_hidrografica_add'),
    url(r'^bacia-hidrografica/edit/$', login_required(Bacia_Hidrografica_Edit.as_view(), login_url=login_template), name='bacia_hidrografica_edit'),
    url(r'^bacia-hidrografica/delete/(?P<bh_id>\d+)$', login_required(Bacia_Hidrografica_Delete.as_view(), login_url=login_template), name='bacia_hidrografica_delete'),

    #Rio
    url(r'^rio/$', login_required(Rio_Listar.as_view(), login_url=login_template), name='rio_listar'),
    url(r'^rio/add/$', login_required(Rio_Add.as_view(), login_url=login_template), name='rio_add'),
    url(r'^rio/edit/$', login_required(Rio_Edit.as_view(), login_url=login_template), name='rio_edit'),
    url(r'^rio/delete/(?P<rio_id>\d+)/$', login_required(Rio_Delete.as_view(), login_url=login_template), name='rio_delete'),

    #Ponto
    url(r'^ponto/$', login_required(Ponto_Listar.as_view(), login_url=login_template), name='ponto_listar'),
    url(r'^ponto/add/$', login_required(Ponto_Add.as_view(), login_url=login_template), name='ponto_add'),
    url(r'^ponto/edit/$', login_required(Ponto_Edit.as_view(), login_url=login_template), name='ponto_edit'),
    url(r'^ponto/delete/(?P<ponto_id>\d+)/$', login_required(Ponto_Delete.as_view(), login_url=login_template), name='ponto_delete'),

    #Coleta
    url(r'^coleta/$', login_required(Coleta_Listar.as_view(), login_url=login_template), name='coleta_listar'),
    url(r'^coleta/add/$', login_required(Coleta_Add.as_view(), login_url=login_template), name='coleta_add'),
    url(r'^coleta/info/$', login_required(Coleta_Info.as_view(), login_url=login_template), name='coleta_info'),
    url(r'^coleta/delete/(?P<coleta_id>\d+)/$', login_required(Coleta_Delete.as_view(), login_url=login_template), name='coleta_delete'),
    
    #Entorno
    url(r'^entorno/$', login_required(Entorno_Listar.as_view(), login_url=login_template), name='entorno_listar'),
    url(r'^entorno/add/$', login_required(Entorno_Add.as_view(), login_url=login_template), name='entorno_add'),
    url(r'^entorno/edit/$', login_required(Entorno_Edit.as_view(), login_url=login_template), name='entorno_edit'),
    url(r'^entorno/delete/(?P<entorno_id>\d+)/$', login_required(Entorno_Delete.as_view(), login_url=login_template), name='entorno_delete'),

    #Caso
    url(r'^caso/$', login_required(Caso_Listar.as_view(), login_url=login_template), name='caso_listar'),
    url(r'^caso/add/$', login_required(Caso_Add.as_view(), login_url=login_template), name='caso_add'),
    url(r'^caso/delete/(?P<caso_id>\d+)/$', login_required(Caso_Delete.as_view(), login_url=login_template), name='caso_delete'),
    url(r'^caso/pesquisar/$', login_required(Caso_Pesquisar.as_view(), login_url=login_template), name='caso_pesquisar'),
    
    #Imagem
    url(r'^imagem/$', login_required(Imagem_Listar.as_view(), login_url=login_template), name='imagem_listar'),
    url(r'^imagem/add/$', login_required(Imagem_Add.as_view(), login_url=login_template), name='imagem_add'),
    url(r'^imagem/edit/$', login_required(Imagem_Edit.as_view(), login_url=login_template), name='imagem_edit'),
    url(r'^imagem/delete/(?P<img_id>\d+)/$', login_required(Imagem_Delete.as_view(), login_url=login_template), name='imagem_delete'),
    
    #Monitoramento
    url(r'^monitoramento/localizacao/$', login_required(Monitoramento_Localizacao.as_view(), login_url=login_template), name='monitoramento_localizacao'),
    url(r'^monitoramento/imagem/(?P<coleta>\d+)/$', login_required(Monitoramento_Imagem.as_view(), login_url=login_template), name='monitoramento_imagem'),
    url(r'^monitoramento/entorno/$', login_required(Monitoramento_Entorno.as_view(), login_url=login_template), name='monitoramento_entorno'),
    url(r'^monitoramento/solucao/$', login_required(Monitoramento_Solucao.as_view(), login_url=login_template), name='monitoramento_solucao'),
    
    #Historico
    url(r'^historico/$', login_required(Historico_Listar.as_view(), login_url=login_template), name='historico_listar'),
    url(r'^historico/(?P<ponto_id>\d+)/$', login_required(Historico_Detalhes.as_view(), login_url=login_template), name='historico_detalhes')
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
