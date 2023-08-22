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
entrada = input('Entre com o tamanho da lista: ')
while entrada.isdigit() == False or entrada == '0':
    print('Valor digitado inválido!')
    entrada = input('Entre com o tamanho da lista: ')
n = int(entrada)
for i in range(n):
    entrada = input('Entre com um número para a lista: ')
    while entrada.isdigit() == False:
        print('Valor digitado inválido!')
        entrada = input('Entre com um número para a lista: ')
    num = float(entrada)
    L.append(num)

print(f'Soma dos termos da lista = {s(n-1, L)}')

