
# 1. Cadastrar um cliente contendo: nome e idade. Não deve ser possível cadastrar um
# aluno com mesmo nome e a idade deve ser superior a 18 anos.
# 2. Cadastrar um destino de viagem: nome, valor da diária, número mínimo de diárias.
# 3. Cadastrar uma viagem: deve ser salvo o nome do cliente, o destino e número de
# diárias. O valor total da viagem também deverá ser salvo na viagem cadastrada. Em
# cada cliente também deverá ser salvo o valor total gasto na agência.
# 4. Listar as viagens já salvas, categorizadas por destino. Ex: devem ser listadas todas as
# viagens feitas com destino na Cidade X, depois, todas as viagens feitas para a cidade Z,
# e assim por diante.
# 5. Listar os clientes.
# 6. Contabilizar a pontuação de cada cliente. Com o intuito de fidelizar os clientes na
# agência foi criado um programa de pontuação. A cada 1000 reais em viagens, o cliente
# deve receber 100 pontos. Quando ele totalizar 1500 pontos ele pode escolher uma
# cidade de destino e ganhará 3 diárias para esse local. Após calcular a pontuação exibir
# uma tabela com a lista de pontos por cliente. Dica: utilizar um dicionário. Destacar os
# clientes que estão ganhar a viagem.
# 7. Informar o destino mais procurado pelos clientes.
# 8. Informar o destino para o qual mais diárias foram vendidas.
# 9. Efetuar o pagamento de gastos do cliente: o cliente informa o nome e o sistema exibe
# quanto ele está devendo para a agência. O cliente informa o valor que irá pagar e esse
# valor é abatido das faturas em aberto.
# 10. Avaliar status dos clientes: o sistema deve verificar os clientes que possuem mais de
# R$10.000,00 em viagens ainda não pagos. Quando esse valor for atingido não deve ser
# possível mais vender viagens para esse cliente.


def menuCadastro():
    print("")
    print("Menu")
    print("1. Cadastrar cliente")
    print("2. Cadastrar destino")
    print("3. Cadastrar uma viagem")
    print("4. Listar viagens já salvas")
    print("5. Listar clientes")
    print("6. Pontuação por cliente")
    print("7. Destino mais procurado por cliente")
    print("8. Destino para o qual mais diarias foram vendidas")
    print("9. Efetuar pagamento de gastos do cliente ")
    print("10. Avaliar status do cliente")
    print("")
#Nome == ao outro
def cadastrar_cliente(cadastro, nome_cliente, idade_cliente, dados_cliente):
    maiorIdade = False
    if idade_cliente < 18:
        maiorIdade = True
    # for i in range(len(cadastro)):
    #     if cadastro[i][0].upper() == nome_cliente.upper():
    #         print("Cliente ja cadastrado!")
    explica_dado(cadastro, nome_cliente, idade_cliente)
    dados_cliente.append(nome_cliente)
    dados_cliente.append(idade_cliente)
    cadastro.append(dados_cliente)

    if maiorIdade == True:
        return "Cliente menor de idade."
    

def explica_dado(viagem, nome_cliente, idade_cliente): 
    nome_cliente_str = "Cliente: " + str(nome_cliente)      
    viagem.append(nome_cliente_str)
    idade_cliente_str = "Idade: " + str(idade_cliente)
    viagem.append(idade_cliente_str)


def cadastrar_destino(matriz_destino, dados_destino, nome_passageiro, valor_diaria, min_diarias):
    matriz_destino = []
    dados_destino = []
    dados_destino.append("Passageiro: " + str(nome_passageiro))
    dados_destino.append("Valorda diária: " + str(valor_diaria))
    dados_destino.append("Mínimo de diarias" + str(min_diarias))
    matriz_destino.append(dados_destino)

#terminar valor total gasto
def cadastrar_viagem(matriz_viagem,  dados_da_viagem, nome_viagem, destino_viagem, min_diaria, valor_total_viagem):#  add: gasto_na_agencia!!!
    dados_da_viagem.append("Nome: " + str(nome_viagem))
    dados_da_viagem.append("Destino: " + str(destino_viagem))
    dados_da_viagem.append("Numero de diárias: " + str(min_diaria))
    dados_da_viagem.append("Valor total: " + str(valor_total_viagem))  
   # dados_da_viagem.append(str("Gasto total na agencia: ") + gasto_na_agencia) 
    valor_total = ()
   # total_gasto_agencia = ()
    matriz_viagem.append(dados_da_viagem)

def ordenar_por_destino(matriz_viagem):
    ordem_destino = []
    destino =[]
    for i in range(len(matriz_viagem)):
        destino.append(matriz_viagem[i][1])
        destino.sort
        
        ordem_destino.append(destino)
    
    print(destino)
                
    # for words in destino_ordenado:
    #     print(words)

cadastroCliente = [
                    ['Nome: ana paula'],
                    ['Nome: Bruna'],
                    ['Nome: Carolina'],
                    ['Nome: Daniela'],
                    ['Nome: Edna'],
                    ['Nome: Fernanda'],
                    ['Nome: Gabriela'],
                    ['Nome: Helena'],
                    ['Nome: Ingrid'],
                    ['Nome: Jessica']
                    ]
opcao = -1
cadastroDestino = []
cadastroViagem = [  
                    ['Nome: ana paula', 'Destino: sao paulo',     'Numero de diárias: 7', 'Valor total: 400'],
                    ['Nome: Bruna',     'Destino: rio claro',     'Numero de diárias: 2', 'Valor total: 150'],
                    ['Nome: Carolina',  'Destino: ibate',         'Numero de diárias: 6', 'Valor total: 200'],
                    ['Nome: Daniela',   'Destino: riberao preto', 'Numero de diárias: 7', 'Valor total: 700'],
                    ['Nome: Edna',      'Destino: bauru',         'Numero de diárias: 5', 'Valor total: 400'],
                    ['Nome: Fernanda',  'Destino: indaiatuba',    'Numero de diárias: 5', 'Valor total: 400'],
                    ['Nome: Gabriela',  'Destino: araraquara',    'Numero de diárias: 5', 'Valor total: 400'],
                    ['Nome: Helena',    'Destino: bauru',         'Numero de diárias: 5', 'Valor total: 400'],
                    ['Nome: Ingrid',    'Destino: araraquara',    'Numero de diárias: 5', 'Valor total: 400'],
                    ['Nome: Jessica',   'Destino: bauru',         'Numero de diárias: 5', 'Valor total: 400']
                    ]
opcao = -1
while opcao !=0:
    dadosCliente = []
    menuCadastro()
    opcao = int(input("Digite a opcao desejada: "))
    print("")

    if opcao == 1:

        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        cadastrar_cliente(cadastroCliente,nome, idade, dadosCliente)
        if cadastrar_cliente == "Cliente menor de idade.":
            continue   

# 2. Cadastrar um destino de viagem: nome, valor da diária, número mínimo de diárias.
    elif opcao == 2:
        dados_destino = []
        nome = input("Digite o nome do passageiro: ")
        valor_da_diaria = int(input("Digite o valor da diária"))
        num_min_diarias = int(input("Digite o numero minimo de diárias: "))
        cadastrar_destino(cadastroDestino, dados_destino, nome, valor_da_diaria, num_min_diarias)
        print()
# 3. Cadastrar uma viagem: deve ser salvo o nome do cliente, o destino e número de
# diárias. O valor total da viagem também deverá ser salvo na viagem cadastrada. Em
# cada cliente também deverá ser salvo o valor total gasto na agência.  
    elif opcao == 3:
        dadosViagem = []
        nome = input("Digite o nome do cliente: ")
        destino = input("Digite o destino: ")
        num_min_diarias = int(input("Mínimo de diárias: "))
        valor_total = int(input("Valor total da viagem: "))
       # total_gasto_agencia = ("")
        cadastrar_viagem(cadastroViagem,  dadosViagem, nome, destino, num_min_diarias, valor_total)
        print(dadosViagem)
# 4. Listar as viagens já salvas, categorizadas por destino. Ex: devem ser listadas todas as
# viagens feitas com destino na Cidade X, depois, todas as viagens feitas para a cidade Z,
# e assim por diante.
    elif opcao == 4:
        ()
        ordenar_por_destino(cadastroViagem)
        # dadosViagem = []
        # viagens =listar_viagens_por_destino(cadastroViagem)
        # cadastroViagem.append(dadosViagem)
        # viagens =listar_viagens_por_destino(cadastroViagem)
        # print(viagens)

# 5. Listar os clientes.  
    elif opcao == 5:
        listarClientes = []
        for i in range(len(cadastroCliente)):
            listarClientes.append(cadastroCliente[i][1])

        for cliente in listarClientes:
            print(cliente)

# 6. Contabilizar a pontuação de cada cliente. Com o intuito de fidelizar os clientes na
# agência foi criado um programa de pontuação. A cada 1000 reais em viagens, o cliente
# deve receber 100 pontos. Quando ele totalizar 1500 pontos ele pode escolher uma
# cidade de destino e ganhará 3 diárias para esse local. Após calcular a pontuação exibir
# uma tabela com a lista de pontos por cliente. Dica: utilizar um dicionário. Destacar os
# clientes que estão ganhar a viagem.

    elif opcao == 6:
        print()

# 7. Informar o destino mais procurado pelos clientes.
  
    elif opcao == 7:
        for i in range(len(cadastroViagem)):
            ()
# 8. Informar o destino para o qual mais diárias foram vendidas.

    elif opcao == 8:
        print()

# 9. Efetuar o pagamento de gastos do cliente: o cliente informa o nome e o sistema exibe
# quanto ele está devendo para a agência. O cliente informa o valor que irá pagar e esse
# valor é abatido das faturas em aberto.
            
    elif opcao == 9:
        print()

# 10. Avaliar status dos clientes: o sistema deve vererificar os clientes que possuem mais de
# R$10.000,00 em viagens ainda não pagos. Quando esse valor for atingido não deve ser
# possível mais vender viagens para esse cliente.  
    elif opcao == 10:
        print()
    
    else:
        print("Valor inválido!")

