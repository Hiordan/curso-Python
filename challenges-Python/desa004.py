# Faça um programa que leia algo do tecladoe mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
leitura = input('Digite algo: ')
print('O tipo do texto digitado é: ', type(leitura))
print('Tem apenas espaços? ', leitura.isspace())
print('É número? ', leitura.isnumeric())
print('É um tipo decimal? ', leitura.isdecimal())
print('É alfa numerico? ', leitura.isalnum())
print('Contém letras? ', leitura.isalpha())
print('É minuscula? ', leitura.islower())
print('É maiusculo? ', leitura.isupper())
print('Está capitalizada? ', leitura.istitle())
print('Todos os caracter forma digitados ou algum foi copiado? ', leitura.isdigit())
print('É uma identificação válida? ', leitura.isidentifier())
print('É imprimível? ', leitura.isprintable())
# Desafio concluído com sucesso - OK
