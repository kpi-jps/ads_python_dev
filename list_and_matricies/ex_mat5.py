'''
Escreva um programa que leia inicialmente os elementos de 2
matrizes A e B, sendo A de dimensão m x n e B de dimensão n x p. O
programa deverá criar uma matriz produto, representando a matriz produto
de A e B. Ao final, o programa deve mostrar as matrizes A, B e a
matriz produto.
'''
n = int(input("Informe a quantidade de linhas da matriz A"))
m = int(input("Informe a quantidade de colunas da matriz A e de linhas da matriz B"))
p = int(input("Informe a quantidade de colunas da matriz B"))

A = []
for lin in range(n):
    linha = []
    print("Digite os valores (inteiros) para a linha", lin)
    for col in range(m): #constrói cada linha da matriz (coluna por coluna)
        linha.append(int(input(" ")))
    A.append(linha)

B = []
for lin in range(m):
    linha = []
    print("Digite os valores (inteiros) para a linha", lin)
    for col in range(p): #constrói cada linha da matriz (coluna por coluna)
        linha.append(int(input(" ")))
    B.append(linha)

print("Elementos da matriz A:")
for lin in range(n):
    for col in range(m):
        print(f"{A[lin][col]}", end = ' ')
    print('\n')    

print("Elementos da matriz B:")
for lin in range(m):
    for col in range(p):
        print(f"{B[lin][col]}", end = ' ')
    print('\n')

produto = []
for lin in range(n): # para cada linha de A
    linha = []
    for col in range(p): # para cada coluna de B
        soma = 0
        for AB in range(m): # para cada coluna de A e para cada linha de B
            soma += A[lin][AB]*B[AB][col]
        linha.append(soma)    
    produto.append(linha)

print("Elementos da matriz produto de A*B:")
for lin in range(n):
    for col in range(p):
        print(f"{produto[lin][col]}", end = ' ')
    print('\n')
