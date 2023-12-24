primeiro_termo = int(input('Digite o primeiro termo da PA (progressão aritimética): '))
razao = int(input('Digite a razão da PA: '))
contador = 1
termo = primeiro_termo

while contador <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    contador += 1
print('Acabou!!!')
