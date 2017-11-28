# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Crianca, Responsavel, Historico

# Register your models here.


admin.site.register(Crianca)
admin.site.register(Responsavel)
admin.site.register(Historico)
