#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import subprocess
import requests
import os
from datetime import datetime
import string
from evdev import InputDevice
from select import select

def enviar_notificacao():
    print "Enviando notificação."
    pass

# Configurações
INTERVALO = 1 # (em segundos)
URL_SEXO = 'http://127.0.0.1:8000/sexo_crianca/'
URL_SALVAR_ACAO = 'http://127.0.0.1:8000/registrar_acao/'
TECLADO = '/dev/input/event0'
KEYS = "X^1234567890XXXXqwertzuiopXXXXasdfghjklXXXXXyxcvbnmXXXXXXXXXXXXXXXXXXXXXXX"
DIRETORIO_AUDIOS = '/home/pi/VOIC/audios/'

dev = InputDevice(TECLADO)
ultima_acao = datetime.now()

while True:
    r,w,x = select([dev], [], [])
    for event in dev.read():
        if event.type==1 and event.value==1:
            #print "Letra:", KEYS[event.code]
            #print "Event code:", event.code
            #continue
        
            diferenca = datetime.now() - ultima_acao
            if diferenca.seconds >= INTERVALO:
                r = requests.get('http://10.9.99.44:8000/sexo_crianca/')
                dados = r.json()
  
                if dados['sexo'] == "M":
                    sexo = 'homem'
                elif dados['sexo'] == "F":
                    sexo = 'mulher'
                else:
                    subprocess.Popen(['omxplayer', os.path.join(DIRETORIO_AUDIOS, 'cadastro.mp3')])
                    continue
                    
                code = event.code
                if code in (1, 41, 59,):
                    subprocess.Popen(['omxplayer', os.path.join(DIRETORIO_AUDIOS, sexo, 'comer.mp3')])
                    r = requests.get(URL_SALVAR_ACAO, params={'data_hora': ultima_acao, 'acao': 0, 'gerou_notificacao': 0})
                elif letra == 'b':
                    subprocess.Popen(['omxplayer', os.path.join(DIRETORIO_AUDIOS, sexo, 'banheiro.mp3')])
                    r = requests.get(URL_SALVAR_ACAO, params={'data_hora': ultima_acao, 'acao': 1, 'gerou_notificacao': 0})
                elif letra == 'c':
                    subprocess.Popen(['omxplayer', os.path.join(DIRETORIO_AUDIOS, sexo, 'dormir.mp3')])   
                    r = requests.get(URL_SALVAR_ACAO, params={'data_hora': ultima_acao, 'acao': 2, 'gerou_notificacao': 0})          
                elif letra == 'd':
                    subprocess.Popen(['omxplayer', os.path.join(DIRETORIO_AUDIOS, sexo, 'dor.mp3')]) 
                    r = requests.get(URL_SALVAR_ACAO, params={'data_hora': ultima_acao, 'acao': 3, 'gerou_notificacao': 0}) 
                    
                
                r = requests.get('http://10.9.99.44:8000/gerar_notificacao/')
                dados = r.json()
                if dados['gerar_notificacao']:
                    enviar_notificacao()
                

                

