primeiro_termo = int(input('Digite o primeiro termo da PA (progressão aritimética): '))
razao = int(input('Digite a razão da PA: '))
contador = 1
termo = primeiro_termo
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Acabou com um total de {} termos'.format(total))
