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


#definindo o tamanho da matriz A
m = int(input('Entre com um valor para número de linhas de uma matriz A: '))
n = int(input('Entre com um valor para número de colunas de uma matriz A: '))

print ('Adicone os elementos da matriz')
i = 0 #numero de linhas
A = []
while i < m:
    j = 0
    linha = []
    while j < n:
       el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
       linha.append(el)
       j += 1
    A.append(linha)
    i += 1


#checando linhas nulas
cont_linha = 0 #variável de contagem de linhas nulas
i = 0
while i < m:
    j = 0
    cont_zero_linha = 0 #variável de contagem de zeros nas linhas
    while j < n:
        if A[i][j] == 0:
            cont_zero_linha += 1
        j += 1
    if cont_zero_linha == len(A[i]):
        cont_linha += 1
    i += 1

#checando colunas nulas 
cont_coluna = 0 #variável de contagem de linhas nulas
i = 0
while i < n: #aqui i é número de colunas
    j = 0
    cont_zero_coluna = 0 #variável de contagem de zeros nas linhas
    while j < m:
        if A[j][i] == 0:
            cont_zero_coluna += 1
        j += 1
    if cont_zero_coluna == len(A):
        cont_coluna += 1
    i += 1

#imprimindo a matriz A
print('\n')
print('Matriz A:')
print('\n')
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], ' ', end = '')
    print('\n')
print(f'A quantidade de linhas nulas na matriz digitada é {cont_linha}')
print(f'A quantidade de colunas nulas na matriz digitada é {cont_coluna}')
