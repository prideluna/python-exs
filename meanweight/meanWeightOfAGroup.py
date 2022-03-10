#17. Faça um programa que receba a idade, peso e altura de N pessoas. Calcule e mostre:
#a. A média das idades das N pessoas
#b. A quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50 m.
#c. A percentagem de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1,90 m.
#Pergunte ao usuário do programa quantas pessoas serão cadastradas (valor de N).

N = int(input('Quantidade de pessoas a serem adicionadas: '))
idade = 0
contador = 0
soma =0
qtdePesoAcima = 0
qtdePessoasAltas = 0
while N > 0:
    N = N - 1
    idade = idade + 1
    contador = contador + 1
    idade = int(input('Idade: ')) 
    peso = int(input('Peso: ')) 
    altura = round(float(input('Altura em m: '))) 
    if peso > 90 and altura < 1.5:
        qtdePesoAcima = qtdePesoAcima + 1
    if idade >= 10 and idade <= 30 and altura >= 1.9:
        qtdePessoasAltas = qtdePessoasAltas + 1 
        porc =  qtdePessoasAltas/contador  
    
    print('========================' )
    soma = soma + idade
    media = soma/contador
print('Media de Idades: {}'.format(media))
print('Pessoas com peso > 90kg e altura < 1.5m: {}'.format(qtdePesoAcima))
print('% Pessoas idade entre 10 e 30 e altura > que 1.9m: {}%'.format(porc*100))     

    
 

