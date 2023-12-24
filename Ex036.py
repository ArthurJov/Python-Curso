valor = float(input('Digite o valor da casa R$:'))
salario = float(input('Digite o salário do comprador R$:'))
anos = float(input('Digite em quantos anos ele vai pagar: '))

prestacao = valor / (anos * 12)

limite = salario * 0.3

if prestacao > limite:
    print('Infelizmente você não pode financiar esta casa :(')
else:
    print('Parabéns, você pode financiar esta casa')