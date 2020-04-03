#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input('Digite um número que esteja entre 0 e 9999: '))
#Calculo para a unidade
unidade = numero % 10
#Calculo para a dezena
numero = (numero - unidade)/10
dezena = numero % 10
#Calculo para a centena
numero = (numero - dezena)/10
centena = numero % 10
#calculo para a milhar
numero = (numero - centena)/10
milhar = numero % 10
print('O número que você digitou tem \n {} unidade(s)\n {} dezena(s)\n {} centena(s)\n {} milhares.'.format(unidade, dezena, centena, milhar))
#Desafio concluido com sucesso - OK