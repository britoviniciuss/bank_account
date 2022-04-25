from datetime import datetime
import pytz
from account import ContaCorrent, CartaoCredito
from Agencias import AgenciaComum, AgenciaPremium
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print(Fore.LIGHTBLUE_EX + "########################################")
print(Fore.LIGHTBLUE_EX + "#### Bem vindo ao cadastro bancario ####")
print(Fore.LIGHTBLUE_EX + "########################################")
print("\n")


def data_hora():

    fuso_BR = pytz.timezone('Brazil/East')
    horario_BR = datetime.now(fuso_BR)
    return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

def pegar_emprestimo(lista_de_contas, num, agencia1, agencia2):
    nome = login()
    valor = int(input("Quanto você deseja pegar de emprestimo?"))
    for i in range(num):
        if nome in lista_de_contas[i].nome and lista_de_contas[i].agencia == agencia1.numero:
            agencia1.emprestar_dinheiro(valor, lista_de_contas[i].cpf)
            lista_de_contas[i].saldo += valor
            print(Fore.RED + "Emprestimo realizado com sucesso!!")
        elif nome in lista_de_contas[i].nome and lista_de_contas[i].agencia == agencia2.numero:
            agencia2.emprestar_dinheiro(valor, lista_de_contas[i].cpf)
            lista_de_contas[i].saldo += valor
            print(Fore.RED + "Emprestimo realizado com sucesso!!")
          
def criar_agencias():
    ## Agencias pré-definidas ##
    agencia_comum = AgenciaComum(35211111, 70798540000148, 5999)
    agencia_premium = AgenciaPremium(35221199, 86758520000438, 8101)
    return agencia_comum, agencia_premium

def escolher_agencia(agencia1, agencia2):
    nome_agencia = input("De qual agencia você quer fazer parte?")
    nome_agencia = nome_agencia.capitalize()
    agencia_escolhida = ''
    agencia_escolhida2 = ''
    if nome_agencia == 'Comum':
        agencia_escolhida = agencia1
    elif nome_agencia == 'Premium':
        agencia_escolhida2 = agencia2
    
    return agencia_escolhida, agencia_escolhida2, nome_agencia

def criar_conta(agencia1, agencia2):
    lista_contas = []
    print(Fore.GREEN +"## Cadastro conta ##")
    num = int(input("Quantas contas você deseja criar? "))
    for i in range(num):
        nome = input(f"Digite o nome da conta {i+1}: ")
        cpf = input(f"Digite o cpf da conta {i+1}: ")
        nome = nome.capitalize()
        agencia_escolhida1, agencia_escolhida2, nome_agencia = escolher_agencia(agencia1, agencia2)
        
        ## Tratamento do cadastro ##
        try:
            if cpf and nome:
                if len(cpf) == 11 and int(cpf) and str(nome) and nome_agencia == 'Comum':
                    conta = ContaCorrent(nome, cpf, agencia_escolhida1.numero, 2222)
                    lista_contas.append(conta)
                    agencia1.add_cliente(nome, cpf, 0)
                                        
                elif len(cpf) == 11 and int(cpf) and str(nome) and nome_agencia == 'Premium':
                    conta = ContaCorrent(nome, cpf, agencia_escolhida2.numero, 4444)
                    agencia2.add_cliente(nome, cpf, 0)
                    lista_contas.append(conta)
                else:
                    print("Preencha os campos corretamente(CPF: 11 digitos e só numeros)")
                    break       
            else:
                print("Você deixou campos vazios..")
                break 
        except:
            print("Error, preencha os campos corretamente.")
    print(Fore.RED + "##Cadastro de conta realizado com sucesso!!##")
    return lista_contas, num

def login():
    print(Fore.GREEN +"### Login ###")
    nome = input("Qual o nome da sua conta?")
    nome = nome.capitalize()

    return nome

def consultar_saldo_conta(lista_de_contas, num):
    nome = login()
    [lista_de_contas[i].consultar_saldo() for i in range(num) if nome in lista_de_contas[i].nome]

def sacar_conta(lista_de_contas, num):
    nome = login()
    sacar_valor = int(input("Qual valor você deseja sacar?"))
    [lista_de_contas[i].sacar(sacar_valor) for i in range(num) if nome in lista_de_contas[i].nome]
       
def depositar_conta(lista_de_contas, num):
    nome = login()
    depositar_valor = int(input("Quanto você deseja depositar na conta? "))
    [lista_de_contas[i].depositar(depositar_valor) for i in range(num) if nome in lista_de_contas[i].nome]
    print(Fore.RED + "##Deposito realizado com sucesso##")

def registrar_cartao(lista_de_contas, num):
    print(Fore.GREEN +"## Cadastro Cartão ##")
    nome = login()
    titular = input("Digite o nome do titular que sera cadastrado no cartão ")
    [CartaoCredito(titular, lista_de_contas[i]) for i in range(num) if nome in lista_de_contas[i].nome]    

def mostrar_cartao(lista_de_contas, num):
    nome = input(f"Quer ver os cartões da conta da conta com qual nome?")
    for i in range(num):
        if nome in lista_de_contas[i].nome:
            print("## CARTÕES DO CLIENTE##")
            for cartao in lista_de_contas[i].cartoes:
                
                print("############################")
                print(f"Titular: {cartao.titular}")
                print(f"NUMERO: {cartao.numero}")
                print(f"Validade: {cartao.validade}")
                print("############################")
                print("\n")

def tipos_agencia(agencia1,agencia2):
    print(Fore.GREEN +"##### Agencia Comum #####")
    print("Numero: 5999")
    print(f"Essa agencia possuia os seguintes beneficios:")
    print("---------------------------------------------------")
    print(Fore.GREEN +"##### Agencia Premium #####")
    print("Numero: 8101")
    print(f"Essa agencia possuia os seguintes beneficios:")
    print(f"---------------------------------------------------")
    iniciar(agencia1, agencia2)
    
def transferencia(lista_de_contas, num):
    nome = login()
    valor_transferir = int(input(f"Quanto você deseja transferir? "))
    conta_destino = input(f"Pra qual conta você deseja fazer a transferencia?")

    conta_a_ser_transferida = [lista_de_contas[i] for i in range(num) if conta_destino in lista_de_contas[i].nome]
    [lista_de_contas[i].transferir(valor_transferir, conta_a_ser_transferida[0]) for i in range(num) if nome in lista_de_contas[i].nome]

def transacoes_consultar(lista_de_contas, num):
    nome = login()
    [lista_de_contas[i].consultar_historico() for i in range(num) if nome in lista_de_contas[i].nome]

def mostrar_emprestimos(agencia1, agencia2):
    num_agencia = int(input("De qual agencia você quer ver os emprestimos? Obs: Digite o numero \n"))
    
    if num_agencia == agencia1.numero:
        print(Fore.GREEN + "## Emprestimos feito na agencia Comum ##")
        for i in range(len(agencia1.emprestimos)):
            valor, cpf = agencia1.emprestimos[i]
            
            print(f"Valor: {valor}")
            print(f"Cpf: {cpf}")
            print(f"Horario: {data_hora()}")
            print("---------------------------")
            
    elif num_agencia == agencia2.numero:
        print(Fore.GREEN + "## Emprestimos feito na agencia Premium ##")
        for i in range(len(agencia2.emprestimos)):
            valor, cpf = agencia2.emprestismos[i]

            print(f"Valor: {valor}")
            print(f"Cpf: {cpf}")
            print(f"Horario: {data_hora()}")
            print("---------------------------")
            
def mostrar_clientes(agencia1, agencia2):
    num_agencia = int(input("De qual agencia você quer ver os clientes? Obs: Digite o numero \n"))
    print("\n")
    
    if num_agencia == agencia1.numero:
        print(Fore.GREEN + "## Contas cadastradas na Agencia comum ##")
        for i in range(len(agencia1.clientes)):
            nome, cpf, patri_inicial = agencia1.clientes[i]
            
            print(f"Nome: {nome}")
            print(f"Cpf: {cpf}")
            print(f"Patrimonio inicial: {patri_inicial}")
            print("--------------------")
            
    elif num_agencia == agencia2.numero:
        print(Fore.GREEN + "## Contas cadastradas na Agencia Premium ##")
        for i in range(len(agencia2.clientes)):
            nome, cpf, patri_inicial = agencia2.clientes[i]
            
            print(f"Nome: {nome}")
            print(f"Cpf: {cpf}")
            print(f"Patrimonio inicial: {patri_inicial}")
            print("--------------------")
            

def menu_agencia(lista_de_contas, num, agencia1, agencia2):
    opcao = ''
    while opcao != '3':
        opcao = input(f"Digite o que deseja fazer: \n1 - Emprestimos \n2 - Clientes \n3 - Voltar \n")

        if opcao == '1':
            mostrar_emprestimos(agencia1, agencia2)

        elif opcao == '2':
            mostrar_clientes(agencia1, agencia2)
        
        elif opcao == '3':
            segundo_menu(lista_de_contas, num, agencia1, agencia2)
            
def segundo_menu(lista_de_contas, num, agencia1, agencia2):
     opcao = ''
     while opcao != '3':
         opcao = input(f"Digite o que deseja fazer: \n1 - Pedir um cartão \n2 - Mostrar um cartão \n3 - Voltar\n")
         if opcao == '1':
             registrar_cartao(lista_de_contas, num)
         elif opcao == '2':
             mostrar_cartao(lista_de_contas, num)
         elif opcao =='3':
             menu(lista_de_contas, num, agencia1, agencia2)
         else:
             print("Opção digitada errada..")

def menu(lista_de_contas, num, agencia1, agencia2):
    '''Função que inicia o segundo menu'''
    print(Fore.GREEN + "### Bem vindo a sua conta ###")
    opcao = ''
    while opcao != '9':
        opcao = input(f"Digite para o que deseja fazer:\n1 - Consultar Saldo \n2 - Sacar \n3 - Depositar \n4 - Cartão de Crédito \n5 - Fazer transferencia \n6 - Histórico de transação \n7 - Pegar emprestimo \n8 - Dados sobre agencia \n9 - Voltar\n")
   
        if opcao == '1':
            consultar_saldo_conta(lista_de_contas, num)
                        
        elif opcao == '2':
            sacar_conta(lista_de_contas, num)
            
        elif opcao == '3':
            depositar_conta(lista_de_contas, num)

        elif opcao == '4':
            segundo_menu(lista_de_contas, num, agencia1, agencia2)

        elif opcao == '5':
            transferencia(lista_de_contas, num)

        elif opcao == '6':
            transacoes_consultar(lista_de_contas, num)
        
        elif opcao == '7':
            pegar_emprestimo(lista_de_contas, num, agencia1, agencia2)
        
        elif opcao == '8':
            menu_agencia(lista_de_contas, num, agencia1, agencia2)

        elif opcao == '9':
            iniciar(agencia1, agencia2)
        else:
            print("Opção digitada invalida")

def iniciar(agencia1, agencia2):
    '''
    Função que inicia o primeiro MENU '''
    opcao = ''
    while opcao != '4':
        print(Fore.GREEN + "### MENU ###")
        
        opcao = input(f"Digite para o que deseja fazer:\n1 - Criar conta \n2 - Ja possuo uma conta \n3 - Tipos de agencia \n4 - Sair \n")

        if opcao == "1":

            lista_de_contas, num = criar_conta(agencia1, agencia2)
     
        elif opcao == '2':
            menu(lista_de_contas, num, agencia1, agencia2)
        
        elif opcao == '3':
            tipos_agencia(agencia1,agencia2)
       
        elif opcao == '4':
            print(Fore.RED + "Finalizando programa...")
            exit()
            
        else:
            print("Opção invalida!")


## Agencias padronizadas ##
agencia1, agencia2 = criar_agencias()
iniciar(agencia1, agencia2)
