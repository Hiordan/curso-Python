#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
PrimeiroAluno = input('Digite o nome do primeiro Estudante: ')
SegundoAluno = input('Digite o nome do segundo Estudante: ')
TerceiroAluno = input('Digite o nome do terceiro Estudante: ')
QuartoAluno = input('Digite o nome do quarto Estudante: ')
lista = [PrimeiroAluno, SegundoAluno, TerceiroAluno, QuartoAluno]
random.shuffle(lista) #A função 'shufle' do método randam não pode ser colocado dentro de uma variavel como o método 'choice'
print('A ordem de apresentação será {}.'.format(lista))
#Desafio concluido com sucesso - OK