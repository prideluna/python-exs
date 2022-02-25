#1 – Faça um programa para informatizar o cadastro de alunos em uma escola de inglês. 
# Você deve cadastrar os alunos com as seguintes informações: 
# nome do aluno, idade, sexo (M ou F) e valor da mensalidade paga. 
# Devem ser cadastrados alunos até que a idade seja 0 (zero). Depois de cadastrados os alunos informe:
#- a quantidade de alunos (homens) com mais de 18 anos.
#- o percentual de alunos que pagam mensalidade maior que R$ 100,00 e menor que R$ 200,00.
#- o nome do aluno do sexo masculino que paga a menor mensalidade.
#- o valor da maior mensalidade paga por alunas com idade maior que 50 anos ou com idade menor que 18 anos.
#- preço médio das mensalidades dos homens com mais de 18 anos.

mensalCont = 0
qtdeMascMais18 = 0
idade = -1
menorValorM = 10000
qtdeFemiMais18 = 0
precoMedMensal = 0
contagemMensalidade = 0
contagemTotalAlunos = 0
alunosEntre100e200 = 0
porcent = 0
MaiorValorFem = 0

while idade != 0:
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    nome = (input('Nome: '))
    sexo = (input('Sexo (M/F): '))
    mensalidade = int(input('Mensalidade: '))
    contagemTotalAlunos += 1
#a quantidade de alunos (homens) com mais de 18 anos    
    if sexo == 'm' or sexo == 'M' and idade > 18: 
        qtdeMascMais18 += 1

# % de alunos que pagam mensalidade > que R$ 100,00 e < que R$ 200,00        
    if mensalidade > 100 and mensalidade < 200:
        alunosEntre100e200 +=1
        porcent = alunosEntre100e200/contagemTotalAlunos

# nome do aluno Masc que paga a < mensalidade
    if sexo == 'M' or sexo == 'm' and mensalidade <= menorValorM:
        menorValorM = mensalidade 
        NomeMenorMensalidadeMasc = nome
#- o valor da > mensalidade paga por F com idade > que 50 anos ou com idade < que 18 anos.
    if sexo == 'f' or sexo == 'F' and idade > 50 or idade < 18: 
        if MaiorValorFem <= mensalidade:
            MaiorValorFem = mensalidade

#- preço médio das mensalidades dos homens com mais de 18 anos.
    if sexo == 'm' or sexo == 'M' and idade > 18:
        mensalidade += 1
        contagemMensalidade += 1 
        precoMedMensal = mensalidade/contagemMensalidade
        print(mensalidade)

print(f'Qtde alunos homens com mais de 18 anos: {qtdeMascMais18} ')
print(f'Percentual de alunos que pagam mensalidade > que R$ 100,00 e < que R$ 200,00: {porcent*100}%.')
print(f'Valor da > mensalidade paga por F com idade > que 50 anos ou com idade < que 18 anos. {MaiorValorFem}')
print(f'O nome do aluno do sexo masculino que paga a menor mensalidade:  {NomeMenorMensalidadeMasc}')
print(f'Preço médio das mensalidades dos homens com mais de 18 anos: {precoMedMensal}')
