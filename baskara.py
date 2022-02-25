
from math import sqrt

print('Para resolver a equacao no formato: a.x² + b.x + c: ')
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

delta = b*b -(4*a*c)

if delta < 0:
    print('não existem raizes reais')
    
else:
    x1 = (-b + sqrt(delta))/(2*a)
    if delta == 0:
        print('Existe uma raiz real e o valor é: ' + str(x1))
    else:
        x2 = (-b - sqrt(delta))/(2*a)
        print('Existem duas raizes reais e o valor é: ' + str(x1) + ' e ' + str(x2))
    
