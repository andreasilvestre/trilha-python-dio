#sistema bancário otimizado em função
LIMITE_SAQUE = 3 # pode realizar apenas 3 saques no dia
total_saques = 0
valor_maximo_saque = 500 # os saques serão aceitos até o valor de 500 reais cada
saque = 0 # não pode ser valor negativo
saldo = 0
deposito = 0 # não pode ser valor negativo
numero_conta = 1
extrato = ""
usuarios = []
contas = []
AGENCIA = "0001"


def depositar(deposito, saldo, extrato):
    if deposito > 0:
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        saldo += deposito
        print("Depósito realizado com sucesso")
    else:
        print("O depósito não pode ser valor negativo")
    return saldo, extrato

def sacar(saque, saldo, extrato, total_saques, LIMITE_SAQUE,valor_maximo_saque):
    if saque < 0:
        print ("O saque não pode ser com valor negativo")
    elif total_saques > LIMITE_SAQUE:
        print ("Número excedido. O limite diário de saques é de 3 vezes.")
    elif saque > saldo:
        print ("Sem saldo suficiente. Seu saldo está abaixo do valor do saque")
    elif saque > valor_maximo_saque:
        print ("Excedeu limite. O limite de cada saque é de até 500 reais")
    else:
        total_saques += 1
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
    return saldo, extrato

def ver_extrato(saldo,/,*, extrato):
    print("==================Extrato bancário do dia================= \n")
    print(extrato)
    print(f"O seu saldo é: R$ {saldo:.2f}")
    print("==========================================================")

def criar_usuarios(usuarios):
    cpf = input ("Informe o número do CPF: ")
    cpf_existe = consultar_cpf (usuarios, cpf)
    if cpf_existe:
        print ("Usuário já está cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Inform a data de nascimento no formato dd/mm/aaaa: ")
    endereco = input ("Informe o endereço completo, logradouro, nro - bairro - cidade/Estado: ")

    usuarios.append ({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com sucesso! ===")

def consultar_cpf(usuarios, cpf):
    cpf_existe = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return cpf_existe[0] if cpf_existe else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    cpf_existe = consultar_cpf(usuarios, cpf)

    if cpf_existe:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cpf_existe}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
     
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t  {conta['numero_conta']}
            Titular:\t {conta['usuario']['nome']}
            \n
        """
        print (linha)

        #print("=" * 100)
        #print(textwrap.dedent(linha))


menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair

==> """

while True:
    opcao = input(menu)

    if opcao == "d":

        deposito = float(input ("Informe o valor do depósito: "))
        saldo, extrato = depositar(deposito, saldo, extrato)  

    elif opcao == "s":

        saque = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saque, saldo, extrato, total_saques, LIMITE_SAQUE, valor_maximo_saque)
        
    elif opcao == "e":
        
        ver_extrato(saldo, extrato = extrato)

    elif opcao == "nu":
        
        criar_usuarios(usuarios)

    elif opcao == "nc":
       
       conta =  criar_conta(AGENCIA, numero_conta, usuarios)
       numero_conta += 1
       if conta:
           contas.append(conta)
    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
    
        break

    else:
        print ("Opção inválida. Selecine o menu correto.")


        
