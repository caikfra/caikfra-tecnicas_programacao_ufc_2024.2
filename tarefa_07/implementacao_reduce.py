from functools import reduce 

lista = [i for i in range(1,11,1)]
lista2 =  [("a", 1), ("b", 2), ("a", 3)]

#1. Produto de uma Lista:
'''• Utilize a função reduce() para calcular o produto dos números em uma lista.'''
print(reduce(lambda a, b: a * b, lista), '\n')

#2. Maior Número
'''• Use a função reduce() para encontrar o maior número em uma lista.'''
print(reduce(lambda a, b: a if a > b else b, lista), '\n')

#3. Construção de um Dicionário
'''• Use reduce() para transformar uma lista de tuplas como [("a", 1), ("b", 2), ("a", 3)] em um
dicionário, onde as chaves são únicas e os valores correspondem à soma dos valores associados
àquela chave. Exemplo de saída esperada: {"a": 4, "b": 2}'''
from functools import reduce

lista_tuplas = [("a", 1), ("b", 2), ("a", 3)]

dicionario_resultado = dict(reduce(lambda acumulador, item: {**acumulador, item[0]: acumulador.get(item[0], 0) + item[1]}, lista_tuplas, {}))

print(dicionario_resultado)  # Saída esperada: {"a": 4, "b": 2}