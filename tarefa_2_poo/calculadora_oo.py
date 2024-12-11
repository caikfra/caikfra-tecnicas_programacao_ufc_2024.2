class Calculadora:
    def __init__(self) -> None:
        self.__acumulador = 0.0
    
    def soma(self, b: int, a: int | None = None) -> int:
        if a is None:
            self.__acumulador += b
        else:
            self.__acumulador = a + b
        return self.__acumulador
    
    def sub(self, b: int, a: int | None = None) -> int:
        if a is None:
            self.__acumulador -= b
        else:
            self.__acumulador = a - b
        return self.__acumulador
    
    def mult(self, b: int, a: int | None = None) -> int:
        if a is None:
            self.__acumulador *= b
        else:
            self.__acumulador = a * b
        return self.__acumulador
    
    def div(self, b: int, a: int | None = None) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        if a is None:
            self.__acumulador /= b
        else:
            self.__acumulador = a / b
        return self.__acumulador
