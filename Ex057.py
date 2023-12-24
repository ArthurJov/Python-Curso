sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo != "M" and sexo != "F":
    sexo = str(input('Sexo inválido, por favor, digite novamente [M/F]: ')).strip().upper()[0]
if sexo == "M":
    print("Masculino")
else:
    print("Feminino")
