saldo = 0
saques_diarios = 0
historico = []

while True:
    menu = int(input('''
Digite um número para escolher sua opção: 

[0] "Sair"
[1] "Depósito"
[2] "Saque"
[3] "Extrato"
'''))

    if menu == 0:
        print("Saindo do programa...")
        print("Obrigado por ser nosso cliente!")
        break

    elif menu == 1:
        print("Opção escolhida: depósito")
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo += valor_deposito
        historico.append("Depósito de R$ {:.2f}".format(valor_deposito))
        print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor_deposito))

    elif menu == 2:
        if saques_diarios < 3:
            print("Opção escolhida: saque")
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 500:
                print("Valor máximo de saque excedido. Saque não realizado.")
            elif valor_saque > saldo:
                print("Saldo insuficiente. Saque não realizado.")
            else:
                saldo -= valor_saque
                saques_diarios += 1
                historico.append("Saque de R$ {:.2f}".format(valor_saque))
                print("Saque de R$ {:.2f} realizado com sucesso.".format(valor_saque))
        else:
            print("Limite diário de saques atingido. Saque não realizado.")

    elif menu == 3:
        print("Opção escolhida: extrato")
        print("Saldo atual: R$ {:.2f}".format(saldo))
        print("Histórico de transações:")
        for transacao in historico:
            print(transacao)

    else:
        print("Opção inválida. Por favor, digite uma opção válida.")

