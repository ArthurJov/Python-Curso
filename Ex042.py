a = float(input('Digite o tamanho em cm da primeira reta: '))
b = float(input('Digite o tamanho em cm da segunda reta: '))
c = float(input('Digite o tamanho em cm da terceira reta: '))

# Verifica se as retas podem formar um triângulo
if a + b < c or a + c < b or b + c < a:
  print('Não pode formar um triângulo')

# Verifica se é equilátero
elif a == b == c:
  print('Pode formar um triângulo equilátero')

# Verifica se é isósceles
elif a == b or a == c or b == c:
  print('Pode formar um triângulo isóceles')

# Se não caiu em nenhuma condição, é escaleno
else:
  print('Pode formar um triângulo escaleno')