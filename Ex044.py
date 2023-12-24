preco = float(input('Digite o preço do produto: R$'))
forma_pagamento = int(input('Digite qual será a forma de pagamento: '
                   '\nDigite \033[1;31m[1]\033[m para à vista \033[1;40mDinheiro/Cheque\033[m'
                   '\nDigite \033[1;31m[2]\033[m para à vista no \033[1;40mCartão\033[m'
                   '\nDigite \033[1;31m[3]\033[m em até \033[1;40m2x no cartão\033[m'
                   '\nDigite \033[1;31m[4]\033[m para \033[1;40m3x no cartão, ou mais\033[m\n'))
if forma_pagamento == 1:
    print('O valor do produto com 10% de desconto é R${:.2f}'.format(preco * 0.90))
elif forma_pagamento == 2:
    print('O valor do produto com 5% de desconto é R${:.2f}'.format(preco * 0.95))
elif forma_pagamento == 3:
    print('O valor do produto é R${:.2f}'.format(preco))
elif forma_pagamento == 4:
    print('O valor do produto com 20% de juros é R${:.2f}'.format(preco * 1.20))
else:
    print('Opção inválida, tente novamente.')