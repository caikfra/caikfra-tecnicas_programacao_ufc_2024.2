from functools import reduce
#1. Gerador de Pares
'''• Crie um gerador que produza todos os números pares entre 1 e 50. Use um loop for para
 exibir os números gerados.'''
def gerador_pares():
    for num in range(2, 51, 2):  
        yield num

for par in gerador_pares():
    print(par, end=" ")  


#2. SomadeQuadradoscomExpressãoGeradora
'''• Use uma expressão geradora para calcular a soma dos quadrados dos números de 1 a 10.'''
print('\n',reduce(lambda a,b: a+b, [x**2 for x in range(11)]))
print(sum(x**2 for x in range(1, 11)),'\n')

#3. Gerador de Sequência Infinita
'''• Crie um gerador infinito que produza números da sequência de Fibonacci. Exiba os primeiros 10 números gerados.'''
def gerador_fibonnaci():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a+b
        
fib = gerador_fibonnaci()
list = [next(fib) for _ in range(10)]
print(list, '\n')

#4. Gerador Personalizado
'''• Crie um gerador que receba dois números, start e end, e produza todos os números primos
 dentro desse intervalo. Teste o gerador imprimindo os números gerados para o intervalo de
 10 a 50.'''
def eh_primo(num: int):
    if num < 2:
        return False
    if num > 2 and num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def gerador_primos(start: int, end: int):
    for num in range(start, end + 1):
        if eh_primo(num):
            yield num

for primo in gerador_primos(10, 50): 
    print(primo, end=" ")  
print()     
       
#5. Gerador Infinito com Condição de Parada
'''• Crie umgerador infinito que produza números da sequência de Fibonacci. Ele deve parar au
tomaticamente quando o número gerado exceder um valor limite fornecido como argumento
 (por exemplo, 10.000)'''
def gerador_fib_limitado(limite: int):
    a, b = 0,1
    while a <= limite:
        yield a
        a, b = b, a + b

for num in gerador_fib_limitado(1000):
    print(num, end=" ")
print()
    