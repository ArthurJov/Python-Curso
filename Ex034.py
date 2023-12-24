salario = float(input('Digite seu salario R$:'))

if salario > 1250.00:
    salario = salario * 1.10
    print('Seu salario com aumento de 10% fica R$:{:.2f}'.format(salario))
else:
    salario = salario * 1.15
    print('Seu salario com aumento de 15% fica R$:{:.2f}'.format(salario))