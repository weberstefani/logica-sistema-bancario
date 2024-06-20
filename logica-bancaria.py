menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_valor_saque = 500
extrato = ""
qtde_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_valor_saque
        excedeu_saques = qtde_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Seu saldo é insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque solicitado está acima do seu limite")
        
        elif excedeu_saques:
            print("Operação falhou! Você atingiu o limite diário de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtde_saques += 1

        else:
            print("Operação inválida!")
        
    elif opcao == "e":
        print("\n====================EXTRATO====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===============================================")

    elif opcao == "q":
        break

    else:
        print("A operação selecionada é inválida! Por favor selecione novamente a operação.")