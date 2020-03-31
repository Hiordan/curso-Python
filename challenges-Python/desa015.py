#Programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Quilometros (KM) o carro percorreu? '))
dias = int(input('Por quantos dias ele foi alugado? '))
custo = (km * 0.15) + (dias * 60)
print('Você utilizou o carro por {} e percorreu {}, logo pagará R$ {}.'.format(km, dias, custo))
