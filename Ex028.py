from random import randint
computador = randint(0, 5)
player = int(input(('Eu pensei em um número entre 0 e 5, tente adivinhar qual é: ')))

if computador == player:
    print('Você acertou, parabéns!!!')
else:
    print('Resposta errada, o número era {}'.format(computador))
