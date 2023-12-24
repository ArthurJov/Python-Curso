print('----- Digite dois números -----\n')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

print('\033[33m[1]\033[m Somar\n'
      '\033[33m[2]\033[m Multiplicar\n'
      '\033[33m[3]\033[m Maior número\n'
      '\033[33m[4]\033[m Inserir novos números\n'
      '\033[33m[5]\033[m Sair\n')

opção = int(input('Escolha uma opção: '))

while opção != 5:
    if opção == 1:
        resposta = n1 + n2
        print('{} + {} = {}'.format(n1, n2, resposta))
        opção = int(input('Escolha uma opção: '))

    if opção == 2:
        resposta = n1 * n2
        print('{} x {} = {}'.format(n1, n2, resposta))
        opção = int(input('Escolha uma opção: '))

    if opção == 3:
        if n1 == n2:
            print('Os números são iguais')
        elif n1 > n2:
            print('Entre {} e {}, o maior número é: {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {}, o maior número é: {}'.format(n1, n2, n2))
        opção = int(input('Escolha uma opção: '))

    if opção == 4:
        print('Digite novos números\n')
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        opção = int(input('Escolha uma opção: '))

print("Você saiu do programa")
