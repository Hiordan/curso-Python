# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = int(input('Digite um angulo: '))
cosseno = math.cos(math.radians(angulo))
print('O cosseno do angulo {} é {:2f}.'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('A tangente do angulo {} é {:.2f}.'.format(angulo, tangente))
seno = math.sin(math.radians(angulo))
print('O seno do angulo {} é {:.2f}.'.format(angulo, seno))
#Desafio concluído com sucesso - OK