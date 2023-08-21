'''
Exercício - aula Lista de listas e matrizes
Ex1. Crie um programa que solicita do usuário um valor N representando a
quantidade linhas e um valor M representando a quantidade de colunas
de uma matriz. Depois, o programa deverá solicitar do usuário N x M
elementos para serem incluídos na matriz. Por fim, o programa deverá
percorrer a matriz para encontrar e imprimir o seu maior elemento e o
seu menor elemento.
'''
#definindo o tamanho da matriz
N = int(input('Entre com um valor para número de linhas de uma matriz: '))
M = int(input('Entre com um valor para número de colunas de uma matriz: '))

print ('Adicone os elementos da matriz')
i = 0 #numero de linhas
matriz = []

while i < N:
    j = 0
    linha = []
    while j < M:
       el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
       linha.append(el)
       j += 1
    matriz.append(linha)
    i += 1

print('\n')
print('Matriz:')
print('\n')
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], ' ', end = '')
    print('\n')


#valores adotados arbitrariamente
el_maior = matriz[0][0]
el_menor = matriz[0][0]

for x in range(len(matriz)):
    for y in range(len(linha)):
        if el_maior < matriz[x][y]:
            el_maior = matriz[x][y]
        if el_menor > matriz[x][y]:
            el_menor = matriz[x][y]
            
print(f'Elemento de menor valor = {el_menor}')
print(f'Elemento de maior valor = {el_maior}')
        
