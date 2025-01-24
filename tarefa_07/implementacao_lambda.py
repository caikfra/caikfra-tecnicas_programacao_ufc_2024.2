lista = [i for i in range(10)]

#1.1 Soma:
soma = lambda a, b: a + b  
print([soma(a, b) for a, b in zip(lista, lista)], "\n")

#1.2 Paridade:
paridade = lambda num: num % 2 == 0
resultados = [paridade(a) for a in lista]
print(resultados,'\n')

print(list(paridade(a) for a in lista), '\n')

#1.3 Elevar ao quadrado
quadrado = lambda num : num ** 2
print(list(map(quadrado, lista)), '\n')

#1.4 Composição de Funções
lista2 = [i for i in range(10, 40, 5)]
c_para_f = lambda temp_converter: float((temp_converter * 9/5) +32)
arredondamento = lambda num: int(num) + 1 if num % 1 > 0.5 else int(num)
conversor = lambda temp: (arredondamento(c_para_f(temp)))
print([conversor(a) for a in lista2])