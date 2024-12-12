from sisbanco import Banco, Conta

def terminal():
    sisbanco = Banco()
    while True:
        print("SisBanco :: Bem-Vindo!")
        print(". :: Opcoes :: .")
        print("[0] - CriarConta")
        print("[1] - Creditar")
        print("[2] - Debitar")
        print("[3] - Transferir")
        print("[4] - Saldo")
        print("[5] - Sair")
        opcao = input("Digite: ")

        if opcao == "0":
            num_conta = input("Digite o número da conta") #num_conta é str
            conta = Conta(num_conta) #cria a instância da conta
            sisbanco.cadastrar(conta) 
            #se fosse num_conta, não estaria passando instância da conta
            
        elif opcao == "1":
            num_conta = input("Digite o número da conta: ")
            valor = input("Digite o valor a ser creditado: ")
            try: 
                valor = float(valor)
                sisbanco.creditar(num_conta, valor)
            except ValueError:
                print('Valor inválido')    

        elif opcao == "2":
            num_conta = input("Digite o número da conta: ")
            valor = input("Digite o valor a ser debitado: ")
            try: 
                valor = float(valor)
                sisbanco.debitar(num_conta, valor)
            except ValueError:
                print('Valor inválido')

        elif opcao == "3":
            num_conta_origem = input("Digite o número da conta de origem: ")
            num_conta_destino = input("Digite o número da conta de destino: ")
            valor = input("Digite o valor a ser debitado: ")
            try: 
                valor = float(valor)
                sisbanco.transferir(num_conta_origem, num_conta_destino, valor)
            except ValueError:
                print('Valor inválido')


        elif opcao == "4":
            num_conta = input("Digite o número da conta: ")
            conta = sisbanco.procurar(num_conta)
            if conta is not None:
                saldo = sisbanco.saldo(num_conta)
                print(f'O saldo da conta {num_conta} é {saldo}.')
            else:
                print('Conta não cadastrada')

        elif opcao == "5":
            print("SisBanco :: Bye!")
            break

if __name__ == "__main__":
    terminal()