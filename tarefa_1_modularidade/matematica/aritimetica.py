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
