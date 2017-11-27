# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

ACAO_CHOICES = (
    ('0', 'Estava com fome'),
    ('1', 'Estava com sono'),
    ('2', 'Queria ir ao banheiro'),
    ('3', 'Estava com dor'),
)

class Crianca(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    sexo = models.CharField(max_length=1, default='M', choices=SEXO_CHOICES, null=False, blank=False)
    idade = models.PositiveIntegerField(null=False, blank=False)

class Responsavel(models.Model):
    email = models.EmailField(null=False, blank=False)
    celular = models.CharField(max_length=100, null=False, blank=False)
    
class Acao(models.Model):
    acao = models.CharField(max_length=1, default='0', choices=ACAO_CHOICES, null=False, blank=False)
    data_hora = models.DateTimeField(auto_now=True, null=False, blank=False)
    gerou_notificacao = models.BooleanField(null=False, blank=False)

