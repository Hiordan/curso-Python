#Convertesão de temperatura - De Celsius para Fahrenheit e Kelvin
celsius = float(input('Qual a temperatura em Celsius: °C '))
grausf = (celsius * 9/5)+32
grausk = celsius + 273.15
print('{} graus Celsius em Fahrenheit é {} e em Kelvin é {}'.format(celsius,grausf,grausk))
