from random import randint

contador = 0

computador = randint(0, 10)

player = int(input("Eu pensei em um número entre 0 e 10, tente adivinhar qual é: "))

while player != computador:
    contador += 1
    player = int(input('Resposta errada, tente novamente: '))

if contador == 0:
    print('Você acertou de primeira, parabéns!!!!')
else:
    print('Voce acertou na {}º tentativa, parabéns!!!!'.format(contador))
