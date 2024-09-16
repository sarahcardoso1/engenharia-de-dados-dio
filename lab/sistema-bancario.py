menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = []
numero_saques = 0 
LIMITE_SAQUES = 3


class SistemaBancario: 

    def saque(self, valor):
        global saldo, limite, extrato, numero_saques, LIMITE_SAQUES
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite diário de saques. ")
            return
        
        if valor > 0 and valor <= saldo and valor <= limite:
            saldo -= valor
            numero_saques += 1
            extrato.append(f"'Saque de R${valor:.2f} realizado.") 

        elif valor > saldo: 
            print("Saldo insuficiente")
        elif valor > limite:
            print("Limite total excedido")
        elif numero_saques >= LIMITE_SAQUES:
            print("Numero de saques diários atingido")
        else: 
            print("valor inválido para saque")

    def deposito(self, quantia_deposito):
        global saldo, extrato
        if quantia_deposito > 0:
            saldo += quantia_deposito
            extrato.append(f"Depósito de R${quantia_deposito:.2f}")
            print("Você depositou R${quantia_deposito: 2.f}")
        else: 
            print("Transação inválida. Verifique o ")      


        def extrato(self):
        print("\nExtrato:")
        if not extrato: 
            print("Nenhuma transação realizada. ")
        else: 
            for transacao in extrato: 
                print(transacao)
        print(f"\nSaldo atual: R${saldo:2.f}")

sistema = SistemaBancario()

while True: 

    opcao = input(menu)

    if opcao =="d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        sistema.deposito(valor_deposito)
            
    elif opcao =="s":
        vaor_saque = float(input("Digite o valor do saque: "))
        sistema.saque(valor_saque)

    elif opcao =="e":
        sistema.exibir_extrato()
    
    elif opcao =="q":
        print("K.Bye")
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")
        


