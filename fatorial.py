#6. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
#usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input('Digite o valor para calcular o fatorial: '))

fat = n
for i in range(1, n):
    n = n - 1
    fat = fat*n
    print('{}! é {}'.format(i, fat))
