# Um anagrama é uma palavra que é feita a partir da transposição das letras de outra palavra ou frase. 
# Por exemplo, “Iracema” é um anagrama para “America”. Escreva um programa que decida se uma string é um anagrama 
# de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres 
# iguais, ou seja, “a” = “A”.
texto1 = input("Type your text here and let see if it is an anagram: ")
texto2 = input("Type another text here and let see if it is an anagram: ")


t1 = texto1.lower()
t1 = "".join(sorted(t1))

t2 = texto2.lower()
print(f"lower >>>{t2}")
t2 = "".join(sorted(t2))

if t1 == t2:
    print("It is an anagram!")
else: 
    print('It isn\'t a anagram!')
print(t1)
print(t2)

