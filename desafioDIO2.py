def fun_deposito(saldo,extrato_deposito):

    deposito = float(input("Insira o valor do deposito: \n"))
    if deposito > 0:
        extrato_deposito.append(deposito)
        saldo += deposito
        print(f"Deposito realizado no valor de: R${deposito:.2f} !")
        return saldo, extrato_deposito
    else:
        print("Deposito invalido !")
def fun_saque(saldo,total_de_saques,extrato_saque):

    if total_de_saques > 0:
            saque = float(input("Insira o valor do saque: \n"))
            if saque < 501 and saque < saldo :
                extrato_saque.append(saque)
                total_de_saques -= 1
                saldo -= saque
                print(f"Saque realizado no valor de: R${saque:.2f} !")
                return saldo,extrato_saque, total_de_saques
            elif saque > 501:
                print('Saque invalido, valor limite atingido !')
            elif saque > saldo:
                print('Saque invalido, saldo insuficiente !')
    else :
        print("Limite de saques atingido !")    
def fun_extrato(extrato_deposito,extrato_saque,saldo):
       print("\n-----Extrato-----")
       print("Depositos realizados:")
       if len(extrato_deposito) == 0:
            print('ainda não houve depositos')
       else:
         for deposito in extrato_deposito:
             print(f"R${deposito:.2f}")
       print("Saques realizados:")
       if len(extrato_saque) == 0:
            print('Ainda não houve saques')
       else:
         for saque in extrato_saque:
            print(f"R${saque:.2f}")
       print(f"Seu saldo é de: R${saldo:.2f}")
       print('-----------------')
def opcao():
   opcao = input("""
  ----MENU----
  [D]Depositar
  [S]Sacar
  [E]Extrato
  [Q]Voltar 
  ---------------
  Escolha uma opção:""")
   return opcao

def main(banco_de_dados):
    saldo = 0
    total_de_saques = 3
    extrato_deposito = []
    extrato_saque = []
    
    while True:
        menu = opcao()
        if menu.lower() == 'd':
            saldo, extrato_deposito = fun_deposito(saldo=saldo, extrato_deposito= extrato_deposito)
        elif menu.lower() == 's':
            saldo, extrato_saque, total_de_saques = fun_saque(saldo= saldo, extrato_saque= extrato_saque, total_de_saques= total_de_saques)
        elif menu.lower() == 'e':
            fun_extrato(saldo= saldo, extrato_deposito= extrato_deposito, extrato_saque= extrato_saque)
        elif menu.lower() == 'q':
            login(banco_de_dados= banco_de_dados)
        else:
            print('Opção invalida !')
def fun_criar_usuario(banco_de_dados):
    cpf = input('Informe seu CPF: ')
    
    if cpf in banco_de_dados:
        print('Operação inválida, usuário já cadastrado!')
    else:
        usuario = {
            'Nome': input('Informe seu nome: '),
            'Data de nascimento': input('Informe sua data de nascimento:()'),
            'Endereço': input('Informe seu endereço: '),
        }
        banco_de_dados[cpf] = usuario
        print('Usuário cadastrado com sucesso')
    
    return banco_de_dados
def fun_entrar_conta(banco_de_dados):
    tentativa_cpf = input('Qual o seu cpf: ')
    if tentativa_cpf in banco_de_dados:
       print(f'Usuario aceito!, bem vindo {banco_de_dados[tentativa_cpf]['Nome']} !')
       main(banco_de_dados= banco_de_dados)
    else:
       print('Usuario invalido!')

def login(banco_de_dados):
    while True:
        menu = input('''
        -----login-----
        [E] Entrar em conta
        [C] Criar uma conta
        [M] Mostrar Contas
        [Q] Sair
        ---------------
        Escolha uma opção: ''')
        
        if menu.lower() == 'e':
            fun_entrar_conta(banco_de_dados= banco_de_dados)
        elif menu.lower() == 'c':
            banco_de_dados = fun_criar_usuario(banco_de_dados= banco_de_dados)  
        elif menu.lower() == 'm':
            if banco_de_dados.__len__() != 0:
                print(banco_de_dados)
            else:
                print('Ainda não há usuarios!')
        elif menu.lower() == 'q':
            print('Finalizando progama...')
            break
         
        else:
            print('Opção inválida!')
banco_de_dados = {}
login(banco_de_dados= banco_de_dados )



  

        

          

