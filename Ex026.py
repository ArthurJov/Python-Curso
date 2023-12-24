frase = str(input('Digite uma frase: ')).lower().strip()
print('A quantidade da "A" na sua frase é: {}'.format(frase.count('a')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))