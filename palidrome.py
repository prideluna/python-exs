# Escreva um programa que reconhece se uma string é um palíndromo, 
# ou seja, se lida do início para o fim é igual se lida do fim para o início. Exemplos: arara, ovo.

while True:
    palindromo = input("Digite uma palavra para verificar se e palindromo: ")
    if palindromo == palindromo[::-1]:
        print("A palavra e palindromo")
    else:
        print("A palavra nao e palindromo")
