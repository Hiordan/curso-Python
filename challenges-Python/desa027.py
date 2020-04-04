#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip().split()
print('Analisando seu nome...')
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
print('Seu primeiro nome é {}.'.format(nome[0]))
#Desafio concluido com sucesso - OK