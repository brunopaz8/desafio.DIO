from datetime import datetime

class pessoa_fisica():
    def __init__(self, nome, cpf, data_nascimento, senha):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.senha= senha
        self.conta = conta(saldo=0)  

class conta():
    def __init__(self, saldo):
        self._saldo = saldo
        self.limite_saque = 3
        self.extrato_deposito = []
        self.extrato_saque = []
    
    def depositar(self):
        deposito = float(input('Insira o valor do depósito: \n'))
        if deposito > 0:
            self._saldo += deposito
            data_hora = datetime.now()
            self.extrato_deposito.append((deposito, data_hora))
            print(f'Depósito realizado no valor de: {deposito:.2f}')
        else:
            print('Depósito inválido!')
    
    def sacar(self):
        if self.limite_saque > 0:
            saque = float(input('Insira o valor do saque: \n'))
            if saque <= 500 and self._saldo >= saque:
                self._saldo -= saque
                data_hora = datetime.now()
                self.extrato_saque.append((saque, data_hora))
                self.limite_saque -= 1
                print(f'Saque realizado no valor de {saque:.2f}')
            elif saque > 500:
                print('Limite de saque por operação excedido!')
            else:
                print('Saldo insuficiente!')
        else:
            print('Limite diário de saques atingido!')
    
    def extrato(self):
        print('====== EXTRATO ======')
        print('DEPÓSITOS:')
        if len(self.extrato_deposito) > 0:
            for deposito, data in self.extrato_deposito:
                print(f'{deposito:.2f} realizado em {data.strftime("%d/%m/%Y %H:%M:%S")}')
        else:
            print('Nenhum depósito realizado.')

        print('SAQUES:')
        if len(self.extrato_saque) > 0:
            for saque, data in self.extrato_saque:
                print(f'{saque:.2f} realizado em {data.strftime("%d/%m/%Y %H:%M:%S")}')
        else:
            print('Nenhum saque realizado.')

        print(f'SALDO ATUAL: {self._saldo:.2f}')


def login(banco_de_dados):
    while True:
        menu = input('''
=======LOGIN=======
[E] Entrar na conta
[C] Criar conta
[M] Mostrar contas
===================
Escolha uma opção: ''')
        
        if menu.lower() == 'e':
            tentativa_cpf = input('Informe seu CPF: ')
            tentativa_senha = input('informe sua senha: ')
            for usuario_dados in banco_de_dados:
                if usuario_dados.cpf == tentativa_cpf and usuario_dados.senha == tentativa_senha:  
                    print(f'Bem vindo de volta {usuario_dados.nome}!')
                    return banco_de_dados, usuario_dados
                else:
                    print('Usuário ou senha incorretos!')

        elif menu.lower() == 'c':
             nome = input('Qual o seu nome: ')
             cpf = input('Qual o seu CPF: ')
             if any(usuario.cpf == cpf for usuario in banco_de_dados):
                 print('Usuário com este CPF já existente!')
             else:
                 data_nascimento = input('Qual a sua data de nascimento: ')
                 senha = input('Crie uma senha: ')
                 novo_usuario = pessoa_fisica(nome, cpf, data_nascimento, senha)
                 banco_de_dados.append(novo_usuario)
                 print(f'Usuário criado com sucesso para {novo_usuario.nome}!')
                 return banco_de_dados, novo_usuario
        elif menu.lower() == 'm':
           if len(banco_de_dados) !=0:
             for usuario in banco_de_dados:
                 print(f'Nome: {usuario.nome}, CPF: {usuario.cpf}, Data de nascimento: {usuario.data_nascimento}')
           else:
               print('Ainda não há contas !')
        else:
            print('Opção invalida !')

banco_de_dados = []
banco_de_dados, usuario = login(banco_de_dados)

def opcao():
    return input('''
  -----MENU-----
  [D] Depositar
  [S] Sacar
  [E] Extrato
  [Q] Voltar 
  ---------------
  Escolha uma opção: ''')


while True:
    menu = opcao()
    if menu.lower() == 'd':
        usuario.conta.depositar()
    elif menu.lower() == 's':
        usuario.conta.sacar()
    elif menu.lower() == 'e':
        usuario.conta.extrato()
    elif menu.lower() == 'q':
        banco_de_dados, usuario = login(banco_de_dados)
    else:
        print('Opção inválida!')
