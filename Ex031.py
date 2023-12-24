distancia = float(input('Digite a distância da viagem em Km: '))

if distancia <= 200:
    distancia = distancia * 0.50
else:
    distancia = distancia * 0.45

print('O valor da sua viagem é de R$:{:.2f}'.format(distancia))