#Escrever um programa que permita ao usuário digitar três números inteiros. Após
#a leitura, o programa deve verificar se os três valores podem formar um triângulo.
#Caso possam, o programa deve imprimir uma mensagem especificando se o
#triângulo é eqüilátero (três lados iguais), isósceles (dois lados iguais) ou escaleno
#(todos os lados diferentes). Obs.: Para que três lados formem um triângulo,
#o comprimento de cada um dos lados tem que ser menor que a soma dos outros dois.


A = int(input('Digite um lado para o triangulo: '))
B = int(input('Digite outro lado para o triangulo: '))
C = int(input('Digite o ultimo valor para formar o triangulo: '))

triangVerif = (A < B + C) and (B < A + C) and (C < A + B)

if triangVerif == False:
    print('Não se forma triangulo com os valores informados. ')
elif (A == B or B == C or A == C) and (A != C or B != A or A != B ):
    print('O triangulo e isosceles')
elif A == B == C: 
    print('O triangulo e equilatero')
else: 
    print('O triangulo e escaleno')