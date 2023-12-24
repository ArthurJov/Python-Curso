speed = float(input('Digite a velocidade do carro em km/h: '))
limite = float(80)
multa = speed - limite
valor = 7 * multa
if speed > limite:
    print('Você tomou uma muta de R$:{:.2f}'.format(valor))
else:
    print('Você está abaixo do limite de velocidade')
