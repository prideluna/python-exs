#Elabore um programa que peça para n pessoas a sua idade, ao final o programa
#devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior
#que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
#calculada. (Leia o valor de n)


    
lista = []

while True: 
    a = int(input('Digite sua idade ou 0 para calcular a media: '))
    lista.append(a)
    print(lista)
    if a == 0:
        lista.remove(a)
        media = sum(lista)/(len(lista))
        if media > 0 and media <= 25:
            print('Turma jovem')
            print(media)
        elif media > 26 and media < 60:
            print('turma adulta')
            print(media)
        else:
            print('Turma idosa')
            print(media)
            break


        
    
   
