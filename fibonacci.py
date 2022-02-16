#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça
#um programa capaz de gerar a série até o n−ésimo termo.


n = int(input('Digite o enésimo termo da sequencia de Fibonacci: '))

ultimo = 1
penultimo = 1
cont = 3
print('1')
print('1')
while cont <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    cont = cont + 1
    
    print(termo)
