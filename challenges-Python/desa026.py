#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('Analisando sua frase...')
print('A frase digitada a letra A aparece {}.'.format(frase.count('A')))
print('Sendo que o primeiro A foi digitado na posição {}.'.format(frase.find('A')+1))
print('E a última letra A aparece que na posição {}.'.format(frase.rfind('A')+1))
#Desafio concluido com sucesso - OK