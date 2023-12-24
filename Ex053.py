frase = str(input('Digite sua frase: '))
frase.strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('"{}" é um palindromo!!!'.format(frase))
else:
    print('"{}" não é um palindromo!!!'.format(frase))
