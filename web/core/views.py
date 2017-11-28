# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, View

from .models import *

# Create your views here.

class PaginaInicialView(View):

    def get(self, request):
        
        if Crianca.objects.all().count() == 0:
            existe = False
        else:
            existe = True
        
        context = {
            'existe': existe,
        }
        return render(request, 'pagina_inicial.html', context)
        
class CadastroView(View):
        
    def get(self, request):
        if Crianca.objects.all().count() == 0:
            
            crianca_form = CriancaForm()
            responsavel_form = ResponsavelForm()

            context = {
                'crianca_form': crianca_form,
                'responsavel_form': responsavel_form,
            }
            
            return render(request, 'cadastro.html', context)
        else:
            context = {
                'mensagem': 'Já existe um cadastro.',
                'novo_cadastro': True,
            }
            return render(request, 'mensagem.html', context)

    def post(self, request):

        # Verifique se há algum problema com o form.
        crianca_form = CriancaForm(request.POST, request.FILES)
        responsavel_form = ResponsavelForm(request.POST, request.FILES)
        
        if crianca_form.is_valid() and responsavel_form.is_valid():
            crianca = crianca_form.save(commit=False)
            responsavel = responsavel_form.save(commit=False)
            
            crianca.save()
            responsavel.save()
            
            context = {
                'mensagem': 'Cadastro realizado com sucesso.',
            }            
            
            return render(request, 'mensagem.html', context)
        else:
            return None
        
class EdicaoView(View):
    
    def get(self, request):
        
        if Crianca.objects.count() > 0:
            
            crianca = Crianca.objects.last()
            responsavel = Responsavel.objects.last()
        
            crianca_form = CriancaForm(request.POST or None, instance=crianca)
            responsavel_form = ResponsavelForm(request.POST or None, instance=responsavel)

            context = {
                'crianca_form': crianca_form,
                'responsavel_form': responsavel_form,
            }
            
            return render(request, 'cadastro.html', context)
        else:
            context = {
                'mensagem': 'Ainda não existe cadastro.'
            }
            return render(request, 'mensagem.html', context)

    def post(self, request):

        # Verifique se há algum problema com o form.
        crianca_form = CriancaForm(request.POST, request.FILES)
        responsavel_form = ResponsavelForm(request.POST, request.FILES)
        
        if crianca_form.is_valid() and responsavel_form.is_valid():
            crianca = crianca_form.save(commit=False)
            responsavel = responsavel_form.save(commit=False)
            
            crianca.save()
            responsavel.save()
            
            context = {
                'mensagem': 'Edição realizada com sucesso.',
            }            
            
            return render(request, 'mensagem.html', context)
        else:
            return None


class ExclusaoView(View):
    
    def get(self, request):
        return render(request, 'exclusao.html', locals())
        
    def post(self, request):
        if 'resposta' in self.request.POST:
            resposta = self.request.POST['resposta']
            if resposta == "sim":
                Crianca.objects.all().delete()
                Responsavel.objects.all().delete()
                Historico.objects.all().delete()
                
                context = {
                    'mensagem': 'Todos os dados foram excluídos.',
                }            
            
            return render(request, 'mensagem.html', context)
        
        return Nones
        
class HistoricoView(View):
    
    def get(self, request):
        return render(request, 'historico.html', locals())
