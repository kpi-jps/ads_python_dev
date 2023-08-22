'''
Exercícios Estrutura de Repetição - Extra
Ex2.Escreva um programa que leia um número n (número de termos de uma
progressão aritmética), a1 (o primeiro termo da progressão) e r (a razão da
progressão) e apresenta os n termos desta progressão, bem como a soma de todos
elementos.
'''

n = int(input('Entre com a quantidades de termos para uma progressão aritmética (PA) '))
a1 = float(input('Entre com o primeiro termo da (PA) '))
r = float(input('Entre com a razão da (PA) '))
if n == 1:
    print("Termos da PA")
    print(f'a1 = {a1}')
    print(f'Soma dos termos = {a1}')
elif n == 2:
    print("Termos da PA")
    print(f'a1 = {a1}')
    print(f'a2 = {a1 + r}')
    print(f'Soma dos termos = {a1 + a1 + r}')
else:
    i = 3
    a = a1 + r
    soma = a1 + a
    print("Termos da PA")
    print(f"a1 = {a1}")
    print(f"a2 = {a}")
    while i <= n:
        a += r #a = a + r
        soma += a # soma = soma + a
        print(f"a{i} = {a}")
        i += 1 # i = i + 1
    print(f"Soma dos termos = {soma}")
    
          
