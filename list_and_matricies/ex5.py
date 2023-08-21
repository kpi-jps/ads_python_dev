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
n = int(input('Entre com um valor para número de linhas da matriz A: '))
m = int(input('Entre com um valor para número de colunas da matriz A: '))

#definindo o tamanho da matriz A
p = int(input('Entre com um valor para número de linhas da matriz B: '))
q = int(input('Entre com um valor para número de colunas da matriz B: '))

#condição para multiplicação de matrizes é que a o número de colunas da primeira
#matriz deve ser igual ao número de linhas da sugunda matriz. Assim, m = p

if m == p:
    
    #adicionando os elementos da matriz A
    print ('Adicone os elementos da matriz A')
    i = 0 #numero de linhas
    A = []
    while i < n:
        j = 0
        linha = []
        while j < m:
           el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
           linha.append(el)
           j += 1
        A.append(linha)
        i += 1

    #adicionando os elementos da matriz B
    print ('Adicone os elementos da matriz B')
    i = 0 #numero de linhas
    B = []
    while i < p:
        j = 0
        linha = []
        while j < q:
           el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
           linha.append(el)
           j += 1
        B.append(linha)
        i += 1
    
    #criando a estrutura da matriz transposta A
    At = []
    i = 0
    while i < m:
        j = 0
        linha = []
        while j < n:
            el = 0
            linha.append(el)
            j += 1
        At.append(linha)
        i += 1

    #preenchendo a At
    i = 0 
    while i < n:
        j = 0
        while j < m:
           At[j][i] = A[i][j] 
           j += 1
        i += 1

    #criando a estrutura da matriz transposta B
    Bt = []
    i = 0
    while i < q:
        j = 0
        linha = []
        while j < p:
            el = 0
            linha.append(el)
            j += 1
        Bt.append(linha)
        i += 1

    #preenchendo a Bt
    i = 0 
    while i < p:
        j = 0
        while j < q:
           Bt[j][i] = B[i][j] 
           j += 1
        i += 1
        
    #criando matriz C, que é resultado de A.B
    # C terá como número de linhas n e como número de colunas q 
    C = []
    i = 0
    while i < n:
        j = 0
        linha = []
        while j < q:
            el = 0
            linha.append(el)
            j += 1
        C.append(linha)
        i += 1

    #preenchendo C = [] - para isso será usado A e a Bt
    i = 0
    while i < len(Bt):
        j = 0
        while j < len(A):
            k = 0
            soma = 0
            while k < len(A[j]):
                prod = A[j][k]*Bt[i][k]
                soma = soma + prod
                k += 1
            C[j][i] = soma #os índices aqui são invertidos por causa do uso de Bt
            j += 1
        i += 1
        
   
    print('A =',A)
    print('B =', B)
    print('C =', C)
           
        
else:
    print('As matrizes não apresentam numeros de linhas e colunas adequados para a operação de multiplicação!')
