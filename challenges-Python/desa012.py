#Programa que leia o valor de um produto calcule 15% de desconto sobre o preço original
valorproduto = float(input('Qual o valor original do produto? R$ '))

desconto = valorproduto * 0.05

print('O valor do porduto original é R$ {}, aplicando o desconto de 5% nele ficará R$ {:.2f}.'.format(valorproduto,valorproduto - desconto))
#Desafio concluido com sucesso - OK