#Programa que pela altura e a largura consiga dizer a quantidade de tinta para pintar toda a superficie
altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual largura da parede: '))
area = largura * altura
quantlitros = area / 2
print('A área da parede é {}. Você precisará de {} litros de tinta para pintar toda a parede.'.format(area, quantlitros))
#Desafio concluido com sucesso - OK