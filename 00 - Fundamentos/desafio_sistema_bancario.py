LIMITE_SAQUE = 3 # pode realizar apenas 3 saques no dia
total_saques = 0
valor_maximo_saque = 500 # os saques serão aceitos até o valor de 500 reais cada
saque = 0 # não pode ser valor negativo
saldo = 0
deposito = 0 # não pode ser valor negativo
extrato = ""


menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

==> """

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input ("Informe o valor do depósito: "))
        if deposito > 0:
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            saldo += deposito
            print("Depósito realizado com sucesso")
        else:
            print("O depósito não pode ser valor negativo")
    elif opcao == "s":
        saque = float(input("Informe o valor do saque: "))
        if saque < 0:
            print ("O saque não pode ser com valor negativo")
        elif total_saques > LIMITE_SAQUE:
            print ("Número excedido. O limite diário de saques é de 3 vezes.")
        elif saque > saldo:
            print ("Sem saldo suficiente. Seu saldo está abaixo do valor do saque")
        elif saque > valor_maximo_saque:
            print ("EXcedeu limite. O limite de cada saque é de até 500 reais")
        else:
            total_saques += 1
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
    elif opcao == "e":
        print("==================Extrato bancário do dia================= \n")
        print(extrato)
        print(f"O seu saldo é: R$ {saldo:.2f}")
        print("==========================================================")
    elif opcao == "q":
        break
    else:
        print ("Opção inválida. Selecine o menu correto.")