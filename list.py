##Faça um programa que pergunte ao usuário o número de elementos de uma lista A e popule essa lista com números inteiros. 
#Os números digitados pelo usuário precisam ser entre 1 e 10.
#Depois popule uma lista B com o dobro de elementos da lista A. Esses números devem ser gerados randomicamente. 
#Depois informe:
#- a média dos valores da lista A
#- o maior valor das duas listas 
#- informe se existem valores na lista A que também estão na lista B. Se existirem valores, coloque em uma lista C e a exiba.
#- informe qual a média de valores é maior, da lista A ou da lista B. 

from random import randint
a = True
lenList = int(input("Put here the list length of your list: "))
La = []
Lb = []
Lc = []
while len(La) < lenList:
    numInt = int(input("Enter some number: "))
    if numInt > 10:
        print("Just numbers below 10, please!")
    else:
        La.append(numInt)
        a = False
  
    num = randint(0,10)
    while 2*len(La) > len(Lb):
        Lb.append(num) 
for i in La:
    if i in Lb:
        Lc.append(i)

Lc = [i for i in La if i in Lb]
greatestLa = max(La)
greatestLb = max(Lb)

meanA = sum(La)/len(La)
meanB = sum(Lb)/len(Lb)

if meanA > meanB:
    greatest = meanA
else: 
    greatest = meanB
print(f"Mean A list: {meanA}")
print(f"A List: {La}")
print(f"B List: {Lb}")
print(f"Same number in both list: {Lc}")
print(f"Major mean is {greatest}")
print(f"Greatest value from List A and List B: {greatestLa} and {greatestLb}")
