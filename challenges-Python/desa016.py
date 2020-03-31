# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ou import math
from math import trunc
numero = float(input('Digite um número: '))
print('O número digitado foi {} e a sua parte inteira é {}.'.format(numero, trunc(numero)))

'''
numero = float(input('Digite um número real: '))
print('O número digitado foi {} e a sua parte inteira é {}.'.format(numero, int(numero)))
'''
#Exercicio concluido com sucesso - OK