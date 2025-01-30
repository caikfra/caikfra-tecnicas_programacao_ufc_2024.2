lista = [-10, 15,-20, 25, 0, 30]
lista2 = ['python', 'lambda', 'map']
lista3 = [i for i in range(11)]

# 1. Filtrar Números Positivos
print(list(filter(lambda num: num > -1, lista)), '\n')
'''• Use a função filter() para obter somente os números positivos de uma lista como [-10, 15,
-20, 25, 0, 30].'''

#2. Filtrar Palavras Curtas
'''• Dada uma lista de palavras, use filter() para selecionar apenas as palavras com mais de 5
caracteres.'''
print(list(filter(lambda palavra: len(palavra) > 5, lista2 )),'\n')

#3. Filtragem baseada em Múltiplas Condições
'''• Dada uma lista de números inteiros, use filter() para selecionar apenas aqueles que: (i) são
múltiplos de 3 ou de 5; e (ii) são positivos. Retorne o resultado como uma lista.'''
print(list(filter(lambda num: (num % 3 == 0 or num % 5 == 0) and num > -1, lista3 )),'\n')
