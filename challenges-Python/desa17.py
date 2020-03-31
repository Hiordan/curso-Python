#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

catetoo = float(input('Digite o tamanho do cateto Oposto: '))
catetoa = float(input('Digite o tamanho do caterto Adjacente: '))
hipotenusa = (catetoo ** 2 + catetoa **2) ** (1/2)
print('O tamanho da hipotenusa é {:.2f}.'.format(hipotenusa))

'''
from math import hypot
catetoo = float(input('Digite o tamanho do cateto Oposto: '))
catetoa = float(input('Digite o tamanho do caterto Adjacente: '))
hipotenusa = hypot(catetoo, catetoa)
print('O tamanho da Hipotenusa é {:.2f}.'.format(hipotenusa)
print('O tamanho da Hipotenusa é {:.2f}.'.format(sqrt(hipotenusa))))
'''
#Desafio ocnluido com sucesso - OK
