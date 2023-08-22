'''
Ex1. Faça uma função recursiva para encontrar a soma dos elementos de uma lista L de
tamanho n. – Se definirmos a soma dos valores de L por s(L), com indices de
0 a k (L[0..k]), podemos escrever:
s(0) = L[0]
s(k) = s(k-1) + L[k], 1 <= k < n
'''

def s(k, lista):
    if k == 0:
        return lista[k]
    elif 1 <= k and k < len(lista):
        return s(k-1, lista) + lista[k]

L = []

print('-----------------------------------------------------------')
print('Calculando a soma dos elementos de uma lista L:')
n = int(input('Entre com o tamanho da lista: '))
for i in range(n):
    num = float(input(f'Entre com um número para o elemento {i+1} da lista L: '))
    L.append(num)
print(f'L = {L}')
print(f'Soma dos termos da lista L = {s(n-1, L)}')
print('-----------------------------------------------------------')
