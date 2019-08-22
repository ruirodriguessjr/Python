# -*- coding: utf-8 -*-

nome = str(raw_input('Qual é o seu nome completo: ')).strip()
print('Seu nome tem Silva?  {}'.format('silva' in nome.lower()))