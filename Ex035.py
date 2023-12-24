a = float(input('Digite o tamanho em cm da primeira reta: '))
b = float(input('Digite o tamanho em cm da segunda reta: '))
c = float(input('Digite o tamanho em cm da terceira reta: '))

if a + b < c or a + c < b or b + c < a:
    print('Nao pode formar um triângulo')
else:
    print('Pode formar um triângulo')