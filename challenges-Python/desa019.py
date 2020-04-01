#m professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome dos alunos e escrevendo na tela o nome do escolhido.
import random

FristStudent = input('Digite o nome do primeiro estudante: ')
SecudStudente = input('Digite o nome do segundo estudante: ')
ThirdStudent = input('Digite o nome do terceiro estudante: ')
FourStudent = input('Digite o nome do quarto estudante: ')
lista = [FristStudent,SecudStudente,ThirdStudent,FourStudent]
sorteio = random.choice(lista)
print('O aluno escolhido foi {}.'.format(sorteio))
#Toda lista em Python tem que está entre colchetes
#Desafio concluido com sucesso - OK
