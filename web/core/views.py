# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, View

from .models import *

# Create your views here.

class PaginaInicialView(View):

    def get(self, request):
        context = {
            'existe': False,
        }
        return render(request, 'pagina_inicial.html', context)
        
class CadastroView(View):
        
    def get(self, request):

        if request.user.is_authenticated():
            return HttpResponseRedirect("/")

        return render(request, 'cadastro.html', locals())

    def post(self, request):

        # Verifique se há algum problema com o form.
        form = ContaForm(request.POST, request.FILES)
        erros = form.errors.as_data()

        if not form.is_valid():
            return render(request, 'cadastro_conta.html', locals())

        # Neste ponto todos os campos obrigatórios estão OK.

        conta = form.save()
        conta.save()

        # Neste ponto deve ser criada a conta no Samba, LDAP, etc.

        return render(request, 'cadastro_sucesso.html', locals())
        
class EdicaoView(View):
        
    def get(self, request):

        if request.user.is_authenticated():
            return HttpResponseRedirect("/")

        form = ContaForm()
        return render(request, 'cadastro_conta.html', locals())

    def post(self, request):

        # Verifique se há algum problema com o form.
        form = ContaForm(request.POST, request.FILES)
        erros = form.errors.as_data()

        if not form.is_valid():
            return render(request, 'cadastro_conta.html', locals())

        # Neste ponto todos os campos obrigatórios estão OK.

        conta = form.save()
        conta.save()

        # Neste ponto deve ser criada a conta no Samba, LDAP, etc.

        return render(request, 'cadastro_sucesso.html', locals())


class ExclusaoView(View):
    
    def get(self, request):
        return render(request, 'exclusao.html', locals())
        
class HistoricoView(View):
    
    def get(self, request):
        return render(request, 'historico.html', locals())
