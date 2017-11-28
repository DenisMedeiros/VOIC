"""voic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin

from core import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    
    url('^$', views.PaginaInicialView.as_view(), name='pagina_inicial'),
    url('^cadastro/$', views.CadastroView.as_view(), name='cadastro'),
    url('^edicao/$', views.EdicaoView.as_view(), name='edicao'),
    url('^exclusao/$', views.ExclusaoView.as_view(), name='exclusao'),
    url('^historico/$', views.HistoricoView.as_view(), name='historico'),
    
    url('^sexo_crianca/$', views.get_sexo_crianca, name='sexo'),
    url('^registrar_acao/$', views.registrar_acao, name='registrar_acao'),
    url('^gerar_notificacao/$', views.gerar_notificacao, name='gerar_notificacao'),
]
