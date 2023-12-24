print('A soma entre todos os números ímpares que são múltiplos de 3 entre 1 e 500 é:')
soma = 0
for impares in range(1, 500 + 1, 2):
    if impares % 3 == 0:
        soma += impares
print(soma)
