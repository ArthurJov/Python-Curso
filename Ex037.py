n = int(input('Digite um número inteiro: '))
choose = int(input('Digite qual será a base de conversão: '
                   '\n\033[1;31m1\033[m para \033[1;40mBinário\033[m'
                   '\n\033[1;31m2\033[m para \033[1;40mOctal\033[m'
                   '\n\033[1;31m3\033[m para \033[1;40mHexadecimal\033[m\n'))

if choose == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
elif choose == 2:
    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
elif choose == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida, tente novamente.')
