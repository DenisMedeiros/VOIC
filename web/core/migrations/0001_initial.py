# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(choices=[('0', 'Estava com fome'), ('1', 'Estava com sono'), ('2', 'Queria ir ao banheiro'), ('3', 'Estava com dor')], default='0', max_length=1)),
                ('data_hora', models.DateTimeField(auto_now=True)),
                ('gerou_notificacao', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Crianca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('idade', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=100)),
            ],
        ),
    ]
