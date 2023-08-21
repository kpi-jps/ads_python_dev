'''
Exercício - aula Lista de listas e matrizes
Ex3.Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = At
'''

#definindo o tamanho da matriz
N = int(input('Defina onúmero de linhas e colunas da matriz quadrada: ')) #número de linhas e colunas

#construindo a matriz 
i = 0 
matriz = []
print('Entre com os elementos da matriz 3x2')
while i < N:
    j = 0
    linha = []
    while j < N:
       el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
       linha.append(el)
       j += 1
    matriz.append(linha)
    i += 1
print(matriz)

#criando a estrutura da matriz transposta
transposta = []
i = 0
while i < N:
    j = 0
    linha = []
    while j < N:
        el = 0
        linha.append(el)
        j += 1
    transposta.append(linha)
    i += 1
print(transposta)


#preenchendo a matriz transposta com os elementos
i = 0 
print('Entre com os elementos da matriz 3x2')
while i < N:
    j = 0
    while j < N:
       transposta[j][i] = matriz[i][j] 
       j += 1
    i += 1
print(matriz)
print(transposta)

#checando se a matriz e sua transposta são iguais, o que indica se a matriz e
#simétrica
check = False #variável de checagem

i = 0
while i < N:
    j = 0
    while j < N:
        if matriz[i][j] == transposta[j][i]:
            check = True
        else:
            check = False
        j += 1
    i += 1

if check:
    print('A matriz digitada é simétrica')
else:
    print('A matriz digitada não é simétrica')
        
