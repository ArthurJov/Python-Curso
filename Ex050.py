soma = 0
for c in range(1, 6+1):
    numero = int(input('Digite um numero inteiro:'))
    if numero % 2 == 0:
        soma += numero
print('A soma entre os pares é: {}'.format(soma))
