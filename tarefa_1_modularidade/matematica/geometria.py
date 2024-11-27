def area_circulo(a: float) -> float:
    if type(a) == float:
        return 3.14*a**2
    else:
        raise ValueError('valor fornecido inválido')

def area_retangulo(a: float, b: float) -> float:
    if isinstance(a,(int, float)) and isinstance(b, (int, float)):
        return a * b
    else:
        raise ValueError('valor forneceido inválido')