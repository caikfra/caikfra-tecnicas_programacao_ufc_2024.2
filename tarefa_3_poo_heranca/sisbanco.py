class Conta:
    def __init__(self, numero: str):
        self.__numero = numero
        self.__saldo = 0.0

    def creditar(self, valor: float) -> None:
        self.__saldo += valor
        print(f'Valor {valor} creditado. Seu saldo agora é {self.__saldo}')

    def debitar(self, valor: float) -> None:
        self.__saldo -= valor
        print(f'Valor {valor} debitado. Seu saldo agora é {self.__saldo}')

    def get_numero(self) -> str:
        return self.__numero

    def get_saldo(self) -> float:
        return self.__saldo

class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)
    
    def render_juros(self, taxa)->None:
        self.__saldo = self.get_saldo() * taxa

class ContaEspecial(Conta):
    def __init__(self, numero):
        super().__init__(numero)
        self.__bonus = 0

    def render_bonus(self) ->None:
        super().creditar

# -------------------------------------------------------------------------------------------------------------

class Banco:
    def __init__(self):
        self.__contas = []

    def cadastrar(self, conta: Conta) -> None:
        num_conta = conta.get_numero()
        conta_existente = self.procurar(num_conta) #self para usar métodos que estão na classe.
        if conta_existente is None:
            self.__contas.append(conta)
            print(f'Conta de número {num_conta} cadastrada')
            return None
        else: 
            print(f'Conta {num_conta} já existe')

    def procurar(self, numero: str) -> Conta | None:
        for conta in self.__contas:
            if conta.get_numero() == numero: 
                return conta
        print('Conta não encontrada')
        return None 

    def creditar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero) 
        if conta is not None:
            conta.creditar(valor)
        else:
            print(f"Conta com número {numero} não encontrada.")

    def debitar(self, numero: str, valor: float) -> None:
        conta = self.procurar(numero)  
        if conta is not None:
            conta.debitar(valor)
        else:
            print(f"Conta com número {numero} não encontrada.")

    def saldo(self, numero: str) -> float | None:
        conta = self.procurar(numero)  
        if conta is not None:
            return conta.get_saldo()
        print(f"Conta com número {numero} não encontrada.")
        return None

    def transferir(self, origem: str, destino: str, valor: float) -> None:
        origem_conta = self.procurar(origem) 
        destino_conta = self.procurar(destino)
        if origem_conta and destino_conta:
            origem_conta.debitar(valor)
            destino_conta.creditar(valor)
            print(f"Transferência de {valor} realizada de {origem} para {destino}.")
        else:
            print("Transferência falhou: uma ou ambas as contas não foram encontradas.")