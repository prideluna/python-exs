# Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
# conte a quantidade de espaços em branco e a quantidade de vezes que aparecem as vogais a, e, i, o, u.

contadorVogal = 0
contadorEspaco = 0
vogais = "aeiouAEIOU"
texto = input("Digite a frase que desejar: ")
for i in texto:
    if i == " ":
        contadorEspaco +=1
                      
    if i in vogais:
        contadorVogal += 1
print(f"Quantidade de espacos: {contadorEspaco}")
print(f" Quantidade de vogais: {contadorVogal}")
