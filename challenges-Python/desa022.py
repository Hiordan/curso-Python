#: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
nomeCompleto = str(input('Por favor, digite seu nome completo: '))#input do nome do usuário
print('Seu nome é {}.'.format(nomeCompleto))#Exibição do nome digitado
print('Seu nome com todas as letras maiusculas {}.'.format(nomeCompleto.upper()))#Exibição do nome digitado maiusculo
print('Seu nome com todas as letras minusculas {}.'.format(nomeCompleto.lower()))#Exibição do nome digitado minusculo
nomeCompletoSem = ''.join(nomeCompleto.replace(" ", ""))
print('Seu nome completo sem nenhum espaço em branco tem exatamente {} letras.'.format(len(nomeCompletoSem)))
FristNome = nomeCompleto.split()
print(len(FristNome[0]))
#desafio ocncluido com sucesso - Ok