soma = lambda a, b: a + b
lista = [i for i in range(10)]  
print([soma(a, b) for a, b in zip(lista, lista)] )
