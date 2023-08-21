'''
Exercício - aula Lista de listas e matrizes
Ex5.Escreva um programa que leia inicialmente os elementos de 2
matrizes A e B, sendo A de dimensão m x n e B de dimensão p x q. O
programa deverá criar uma matriz C, representando a matriz produto
de A e B. Ao final, o programa deve mostrar as matrizes A, B e a
matriz C.
'''
print('Multiplicação entre a matriz A e a matriz B (A.B)')

#definindo o tamanho da matriz A
m = int(input('Entre com um valor para número de linhas da matriz A: '))
n = int(input('Entre com um valor para número de colunas da matriz A: '))

print('\n')
#definindo o tamanho da matriz A
p = int(input('Entre com um valor para número de linhas da matriz B: '))
q = int(input('Entre com um valor para número de colunas da matriz B: '))

#condição para multiplicação de matrizes é que a o número de colunas da primeira
#matriz deve ser igual ao número de linhas da sugunda matriz. Assim, m = p

if n == p:
    
    print('\n')
    #adicionando os elementos da matriz A
    print ('Adicone os elementos da matriz A')
    i = 0 #numero de linhas
    A = []
    while i < m:
        j = 0
        linha = []
        while j < n:
           el = float(input(f'Entre com o elemento a{i+1}x{j+1}: '))
           linha.append(el)
           j += 1
        A.append(linha)
        i += 1

    print('\n')
    #adicionando os elementos da matriz B
    print ('Adicone os elementos da matriz B')
    i = 0 #numero de linhas
    B = []
    while i < p:
        j = 0
        linha = []
        while j < q:
           el = float(input(f'Entre com o elemento b{i+1}x{j+1}: '))
           linha.append(el)
           j += 1
        B.append(linha)
        i += 1
    
    #construindo a matriz C = A.B
    C = []
    i = 0 #número de linhas de A
    while i < m:
        j = 0 #número de colunas em B
        linha = [] #cria a linha de C
        while j < q:
            k = 0 #numéro de colunas em A e número de linhas em B
            soma = 0
            while k < n:
                prod = A[i][k]*B[k][j]
                soma = soma + prod
                k += 1
            linha.append(soma)   
            j += 1
        C.append(linha)
        i += 1

    #imprimindo a matriz A
    print('\n')
    print('Matriz A:')
    print('\n')
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], ' ', end = '')
        print('\n')

    #imprimindo a matriz B
    print('\n')
    print('Matriz B:')
    print('\n')
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], ' ', end = '')
        print('\n')

    #imprimindo a matriz C (C = A.B)
    print('\n')
    print('Matriz C = A.B:')
    print('\n')
    for i in range(len(C)):
        for j in range(len(C[i])):
            print(C[i][j], ' ', end = '')
        print('\n') 
    
           
        
else:
    print('As matrizes não apresentam numeros de linhas e colunas adequados para a operação de multiplicação!')
