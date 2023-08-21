'''
Exercício - aula Lista de listas e matrizes
Ex4.Escreva um programa que leia inteiros positivos m e n e os elementos
de uma matriz A de números inteiros de dimensão m x n e ao final
mostra a quantidade de linhas e colunas que tem apenas zeros (linhas
nulas e colunas nulas).
'''
#para checar o número de linhas nulas será usado a própria matriz
#para checar a quantidade de colunas nulas será usado a transposta da matriz
#uma vez que na transposta as colunas da matriz inicial viram linhas
#as linhas são mais fáceis de serem checadas


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
while i < N:
    j = 0
    while j < M:
       transposta[j][i] = matriz[i][j] 
       j += 1
    i += 1


#checando linhas nulas, usando a matriz
cont_linha = 0 #variável de contagem de linhas nulas
i = 0
while i < N:
    j = 0
    cont_zero_linha = 0 #variável de contagem de zeros nas linhas
    while j < M:
        if matriz[i][j] == 0:
            cont_zero_linha += 1
        j += 1
    if cont_zero_linha == len(matriz[i]):
        cont_linha += 1
    i += 1

#checando colunas nulas com a transposta da matriz
cont_coluna = 0 #variável de contagem de linhas nulas
i = 0
while i < M:
    j = 0
    cont_zero_coluna = 0 #variável de contagem de zeros nas linhas
    while j < N:
        if transposta[i][j] == 0:
            cont_zero_coluna += 1
        j += 1
    if cont_zero_coluna == len(transposta[i]):
        cont_coluna += 1
    i += 1

print(matriz)
print(transposta)
print(f'A quantidade de linhas nulas na matriz digitada é {cont_linha}')
print(f'A quantidade de colunas nulas na matriz digitada é {cont_coluna}')
