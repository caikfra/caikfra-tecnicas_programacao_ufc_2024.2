class Conta:
    def __init__(self, numero: str):
        self.__numero = numero
        self.__saldo = 0.0
    
    def creditar(self, valor: float) -> str:
        self.__saldo += valor
        return print(f'Valor {valor} creditado.\n'+f'Seu saldo agora é {self.__saldo}')

    def deditar(self, valor: float) -> str:
        self.__saldo -= valor
        return print(f'Valor {valor} debitado\n'+f'Seu saldo agora é {self.__saldo}')
    
    def get_numero(self) -> str:
        return print(f'O número da conta é {self.__numero}')
    
    def get_saldo(self) -> float:
        return print(f'Seu saldo é {self.__saldo}')
