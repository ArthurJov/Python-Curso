from datetime import date

atual = date.today().year
maior = 0
menor = 0

for pessoas in range(1, 7 + 1):
    nascimento = int(input('Em que ano a {}º pessoa nasceu?: '.format(pessoas)))
    idade = atual - nascimento

    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('{} Pessoas são maiores de idade'.format(maior))
print('{} Pessoas são menores de idade'.format(menor))
