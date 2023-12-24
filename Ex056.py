somaIdade = 0
idadeMaisVelho = 0
nomeMaisVelho = ''
mulherMenor20 = 0

for p in range(1, 4 + 1):
    print('----- {}º Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaIdade += idade

    if p == 1 and sexo in 'Mm':
        nomeMaisVelho = nome
        idadeMaisVelho = idade
    if sexo in 'Mm' and idade > idadeMaisVelho:
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade <= 20:

        mulherMenor20 += 1

mediaIdade = somaIdade / 4

print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho é o {} com {} anos'.format(nomeMaisVelho, idadeMaisVelho))
print('No total, {} mulher(es) tem menos do que 20 anos'.format(mulherMenor20))
