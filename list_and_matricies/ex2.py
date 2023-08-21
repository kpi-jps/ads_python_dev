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
N = 3 #número de linhas
M = 2 #número de colunas


i = 0 #numero de linhas
matriz = []
print('Entre com os elementos da matriz 3x2')
while i < N:
    j = 0
    linha = []
    while j < M:
       el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
       linha.append(el)
       j += 1
    matriz.append(linha)
    i += 1

#criando a estrutura da matriz transposta
#para a transposta N é o número de colunas e M o número de linhas
transposta = []
i = 0
while i < M:
    j = 0
    linha = []
    while j < N:
        el = 0
        linha.append(el)
        j += 1
    transposta.append(linha)
    i += 1



#preenchendo a matriz transposta com os elementos
i = 0 
print('Entre com os elementos da matriz 3x2')
while i < N:
    j = 0
    while j < M:
       transposta[j][i] = matriz[i][j] 
       j += 1
    i += 1


    
print('\n')
print('Matriz:')
print('\n')
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], ' ', end = '')
    print('\n')

print('\n')
print('Transposta:')
print('\n')
for i in range(len(transposta)):
    for j in range(len(transposta[i])):
        print(transposta[i][j], ' ', end = '')
    print('\n')
