#Programa que converta um valor em metros para centimetros e milimetros
valormetros =float(input('Digite um valor em metros(m) para ser convertido em centimetros e milimetros: '))
centimetros = valormetros*100
milimetros = valormetros*1000
print('O valor de {} convertido para centimetros é: {:.0f}.'.format(valormetros, centimetros))
print('O valor de {} convertido para milimetros é: {:.0f}.'.format(valormetros, milimetros))
#Desafio concluido com sucesso - OK