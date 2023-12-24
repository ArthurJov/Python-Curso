from time import sleep

numero = int(input('Digite um número inteiro: '))

print('Calculando...')
sleep(3)

print('A tabuada de {} é:'.format(numero))
for c in range(1, 10 + 1):
    print('{} x {} = {}'.format(numero, c, numero * c))
    sleep(0.2)
