#Um motorista de de taxi deseja calcular o rendimento de seu carro na praça.
#Sabendo-se que o preço do combustível é de R$2,50, escreva um programa em C    para ler:
#- a marcação do odômetro no início do dia
#- a marcação no final do dia
#- o número de litros de combustível gasto
#- o valor total (R$) recebido dos passageiros.
#Calcule e escreva a média do consumo em Km/l e o lucro líquido do dia. Se o
#lucro líquido no dia for inferior a R$ 100,00 exiba a mensagem que o
#taxista precisa melhorar seu desempenho.

Comb_RS = 2.50
odInicio = float(input('Odometro inicial: '))
odFim = float(input('odometro final: '))
Litros = float(input('Quantos litros foram gastos? '))
RSpassageiro = float(input('Qual o valor total recebido dos passageiros? '))

kmPorL = (odFim - odInicio)/Litros
LucroLiquido = RSpassageiro - kmPorL*Comb_RS
print(kmPorL)
print(LucroLiquido)
if LucroLiquido < 100:
    print('Voce precisa melhorar seu desempenho! ')
else: 
    print('Seu lucro liquido foi: R$' + str(LucroLiquido))
