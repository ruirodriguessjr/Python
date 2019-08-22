# -*- coding: utf-8 -*-

#
# Criar um programa que lei o nome completo de uma pessoa
# exibir o nome com as letras maiusculas e minusculas
# Quantas letras tem o nome sem os espaços
# Quantas letras tem o primeiro nome
#

nome = str(input('Digite o seu nome: ')).strip()
print('Analisando...')
print('O seu nome em letras maiusculas é: {} '.format(nome.upper()))
print('O seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {}, ele tem {} letras.'.format(separa[0], len(separa[0])))
