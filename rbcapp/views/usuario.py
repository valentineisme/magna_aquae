# coding: utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rbcapp.models.user import Usuario


class Login_Usuario(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login = request.POST['login']
        senha = request.POST['senha']
        user = authenticate(username=login, password=senha)
        if user is not None:
            from django.contrib.auth import login
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'erro'})


class Logout_Usuario(View):
    def get(self, request):
        logout(request)
        return redirect('index')

    def post(self, request):
        logout(request)
        return redirect('index')

class Acessar_Conta(View):
    template = 'acessarConta.html'
    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        if senha == senha2:
            user = User.objects.get(id=request.user.id)
            user.set_password(senha)
            user.save()
            senha = "Sua senha foi alterada com sucesso!"
            return render(request, self.template, {'senha': senha})
        else:
            erro = "As senhas são diferentes, tente novamente!"
            return render(request, self.template, {'erro': erro})

class Recuperar_Senha(View):
    template = 'recuperarSenha.html'
    def get(self, request):
        user = Usuario.objects.get(username=request.GET['username'])
        if 'resposta' in request.GET:
            resposta = request.GET['resposta']
            if resposta == user.resposta:
                return render(request, self.template, {'us': user, 'senha': 'senha'})
            else:
                return render(request, self.template, {'us': user, 'erro': 'erro'})
        return render(request, self.template, {'us': user})

    def post(self, request):
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        if senha == senha2:
            user = User.objects.get(username=request.POST['username'])
            user.set_password(senha)
            user.save()
            senha = "Sua senha foi alterada com sucesso!"
            return render(request, self.template, {'login': senha})
        else:
            erro = "As senhas são diferentes, tente novamente!"
            return render(request, self.template, {'senha': 'senha', 'senha_erro': erro})



