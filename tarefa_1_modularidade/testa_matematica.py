import matematica as mat
from .matematica.estatistica import media

def main():
    global acumulador

    print("Testando função soma:")
    acumulador = 0
    print(mat.soma(3, 4))  # Esperado: 7
    print(mat.soma(a=5))   # Esperado: 12
    print(mat.soma(b=3))   # Esperado: 15

    print("\nTestando função mat.soma:")
    acumulador = 20
    print(mat.soma(10, 5))  # Esperado: 5
    print(mat.soma(a=2))    # Esperado: 3
    print(mat.soma(b=1))    # Esperado: 2

    print("\nTestando função area_circulo:")
    print(mat.area_circulo(3.0))  # Esperado: 28.26
    try:
        print(mat.area_circulo("3"))  # Deve lançar um erro
    except ValueError as e:
        print(e)

    print("\nTestando função area_retangulo:")
    print(mat.area_retangulo(5, 10))  # Esperado: 50
    print(mat.area_retangulo(4.0, 3.5))  # Esperado: 14.0
    try:
        print(mat.area_retangulo(5, "10"))  # Deve lançar um erro
    except ValueError as e:
        print(e)

    print("\nTestando função media:")
    print(media([1,2]))

if __name__ == "__main__":
    main()
