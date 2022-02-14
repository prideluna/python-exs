#Escrever um programa que permita ao usuário digitar o dia e mês de seu
#aniversário e a data de hoje (dia e mês); em seguida, o programa deve calcular
#quantos dias faltam entre a data de hoje e a data do próximo aniversário. Suponha
#todos os meses com 30 dias.


diaNiver = int(input('Digite o dia de seu aniversario: '))
mesNiver = int(input('Digite o mes de seu aniversario: '))

diaAtual = int(input('Digite o dia de hoje: '))
mesAtual = int(input('Digite o mes atual:  '))

niverEsseAno = (30*mesNiver + diaNiver) - (mesAtual*30 + diaAtual)
niverAnoQvem = 360 + niverEsseAno

if mesNiver <= mesAtual:
    print('Seu anivesario é em ' + str(niverAnoQvem) + ' dias.')
else:
    print('Seu anivesario é em ' + str(niverEsseAno) + ' dias.')