from random import randint

print('Pedra, Papel e Tesoura')

itens = ('Pedra', 'Papel', 'Tesoura')

jogador = int(input('''Escolha sua jogada: 
                   \nDigite \033[1;31m[1]\033[m para \033[1;40mPedra\033[m
                   \nDigite \033[1;31m[2]\033[m para \033[1;40mPapel\033[m
                   \nDigite \033[1;31m[3]\033[m para \033[1;40mTesoura\033[m\n'''))

computador = randint(1, 3)

print('O computador escolheu {}'.format(itens[computador-1]))
print('Você escolheu {}'.format(itens[jogador-1]))

if computador == 1:
    if jogador == 1:
        print('Empate -_-')
    elif jogador == 2:
        print('Você ganhou, parabéns!!!')
    elif jogador == 3:
        print('Você perdeu, kkkkkkkkkkkk')
    else:
        print('Jogada inválida, sua anta!!!')

elif computador == 2:
    if jogador == 1:
        print('Você perdeu, kkkkkkkkkkkk')
    elif jogador == 2:
        print('Empate -_-')
    elif jogador == 3:
        print('Você ganhou, parabéns!!!')
    else:
        print('Jogada inválida, sua anta!!!')

elif computador == 3:
    if jogador == 1:
        print('Você ganhou, parabéns!!!')
    elif jogador == 2:
        print('Você perdeu, kkkkkkkkkkkk')
    elif jogador == 3:
        print('Empate -_-')
    else:
        print('Jogada inválida, sua anta!!!')

if jogador > 3:
    print('Jogada inválida, sua anta!!!')
