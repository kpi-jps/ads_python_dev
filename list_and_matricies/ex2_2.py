'''
Exercício - aula Lista de listas e matrizes
Ex2. Faça um programa que solicite do usuário os elementos de uma matriz 3
x 2 (matriz A). Em seguida, o programa deverá criar a matriz transposta
de A (At). Ao final, deve ser mostrada a matriz original e sua respectiva
transposta. Lembre-se que a matriz transposta At será obtida a partir da
matriz A trocando-se ordenadamente as linhas por colunas (ou as
colunas por linhas):
'''

#definindo o tamanho da matriz
m = 3 #número de linhas
n = 2 #número de colunas


i = 0 #numero de linhas
A = []
print('Entre com os elementos da matriz 3x2')
while i < m:
    j = 0
    linha = []
    while j < n:
       el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
       linha.append(el)
       j += 1
    A.append(linha)
    i += 1


#criando a matriz transposta
#para a transposta m é o número de colunas e n o número de linhas
At = []
i = 0
while i < n: #aqui i = número de colunas e j = número de linhas
    j = 0
    linha = []
    while j < m:
        el = A[j][i]
        linha.append(el)
        j += 1
    At.append(linha)
    i += 1


    
print('\n')
print('Matriz A:')
print('\n')
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], ' ', end = '')
    print('\n')

print('\n')
print('Transposta de A:')
print('\n')
for i in range(len(At)):
    for j in range(len(At[i])):
        print(At[i][j], ' ', end = '')
    print('\n')
