from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
resp = radians(angulo)

print('O seno de {:.2f} é igual à: {:.2f}'.format(angulo, sin(resp)))
print('O coseno de {:.2f} é igual à: {:.2f}'.format(angulo, cos(resp)))
print('A tangente de {:.2f} é igual à: {:.2f}'.format(angulo, tan(resp)))
