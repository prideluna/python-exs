matriz = []
m = 8
for i in range(m):
    linha = []
    for j in range(m):
        if (j % 2) != 0:
            linha.append(1)
        else:
            linha.append(0)
 
    matriz.append(linha)
    print(matriz[i])
 
