maior = 0
menor = 0
n_maior = 0
n_menor = 0

for c in range(1, 5 + 1):
    peso = float(input('Digite o peso da {}º pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            n_maior = c
        if peso < menor:
            menor = peso
            n_menor = c

print('A {}º pessoa é a mais pesada, com {}kg'.format(n_maior, maior))
print('A {}º pessoa é a mais leve, com {}kg'.format(n_menor, menor))
