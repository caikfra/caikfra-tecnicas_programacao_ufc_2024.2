# Inicializa o acumulador
acumulador = 0  # Valor inicial

def soma(a: float | None = None, b: float | None = None) -> float:
    global acumulador
    if a is None:
        acumulador += b
    elif b is None:
        acumulador += a
    else:
        acumulador = a + b
    return acumulador

def sub(a: float | None = None, b: float | None = None) -> float:
    global acumulador
    if a is None:
        acumulador -= b
    elif b is None:
        acumulador -= a
    else:
        acumulador = a - b
    return acumulador

def mul(a: float | None = None, b: float | None = None) -> float:
    global acumulador
    if a is None:
        acumulador *= b
    elif b is None:
        acumulador *= a
    else:
        acumulador = a * b
    return acumulador

def div(a: float | None = None, b: float | None = None) -> float:
    global acumulador
    if b == 0:
        raise ValueError("b não pode ser zero")
    if a is None:
        acumulador /= b
    elif b is None:
        acumulador /= a
    else:
        acumulador = a / b
    return acumulador
