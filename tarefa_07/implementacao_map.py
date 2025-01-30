lista = ['python', 'lambda','map']
lista2 = [i for i in range(10)]
lista3 =  ["Python é incrível", "Lambda são úteis", "Map é funcional"]

#1.1 Maiúscula:
print(list(map(lambda palavra: palavra.upper(), lista)), '\n')

#1.2 Quadrado:
print(list(map(lambda numero: numero ** 0.5, lista2)), '\n')

#1.3 Análise_Strings:
print(list(map(lambda frase: {"palavras": frase.count("") + 1, "caracteres": len(frase)}
, lista3)), '\n')



