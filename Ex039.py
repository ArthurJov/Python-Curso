from datetime import date  # Importa a biblioteca date do módulo datetime

data_nascimento = int(input('Digite seu ano de nascimento: '))  # Lê o ano de nascimento como inteiro

ano_atual = date.today().year  # Obtém o ano atual da data de hoje

idade = ano_atual - data_nascimento  # Calcula a idade subtraindo o ano atual pelo ano de nascimento

# Verifica se a idade é menor que 18
if idade < 18:
    print('Você tem {} anos e ainda vai se alistar'.format(idade))
    if 18 - idade == 1:
        print('Falta 1 ano para você se alistar')
    else:
        print('Você tem {} anos e falta {} anos para você se alistar'.format(idade, 18 - idade))

# Verifica se a idade é maior que 18
elif idade > 18:
    if idade - 18 == 1:
        print('Você tem {} anos e já passou 1 ano do tempo de alistamento'.format(idade))
    elif idade - 18 > 1:
        print('Você tem {} anos e já passou {} anos do tempo de alistamento'.format(idade, idade - 18))

# Se não caiu em nenhuma condição acima, é porquê tem exatos 18 anos
else:
    print('Você tem {} anos e está na hora de se alistar'.format(idade))

print('Obrigado por usar nosso sistema!!!')  # Mensagem de agradecimento