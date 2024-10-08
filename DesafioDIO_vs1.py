saldo = 0
total_de_saques = 3
extrato_deposito = []
extrato_saque = []
while True :
    menu = input("""
----MENU----
[D]Depositar
[S]Sacar
[E]Extrato
[Q]Sair
""")
    if menu.lower() == "d":
        deposito = float(input("Insira o valor do deposito: \n"))
        if deposito > 0:
           extrato_deposito.append(deposito)
           saldo += deposito
           print(f"Deposito realizado no valor de: R${deposito:.2f} !")
        else:
            print("Deposito invalido !")
   
    elif menu.lower() == "s":
        if total_de_saques > 0:
            saque = float(input("Insira o valor do saque: \n"))
            if saque < 501 and saque < saldo :
                extrato_saque.append(saque)
                total_de_saques -= 1
                saldo -= saque
                print(f"Saque realizado no valor de: R${saque:.2f} !")
            elif saque > 501:
                print('Saque invalido, valor limite atingido !')
            elif saque > saldo:
                print('Saque invalido, saldo insuficiente !')
             
        else :
            print("Limite de saques atingido !")

    elif menu.lower() == "e":
        print("\n-----Extrato-----")
        print("Depositos realizados:")
        for deposito in extrato_deposito:
            print(f"R${deposito:.2f}")
        print("Saques realizados:")
        for saque in extrato_saque:
            print(f"R${saque:.2f}")
        print(f"Seu saldo é de: R${saldo:.2f}")
        print('-----------------')
    
    elif menu.lower() == "q":
        print('Progama finalizando...')
        break
    
    else:
        print('Opção inválida !')


