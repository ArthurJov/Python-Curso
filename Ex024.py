cidade = str(input('Digite o nome da sua cidade: '))
cidade = cidade.upper()
dividido = cidade.split()
print('A sua cidade começa com "Santo"?')
print('SANTO' in dividido[0])