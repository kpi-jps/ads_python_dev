'''
Exercício - aula Lista de listas e matrizes
Ex5.Escreva um programa que leia inicialmente os elementos de 2
matrizes A e B, sendo A de dimensão m x n e B de dimensão p x q. O
programa deverá criar uma matriz C, representando a matriz produto
de A e B. Ao final, o programa deve mostrar as matrizes A, B e a
matriz C.

Resolução usando função
'''
#definindo a função principal
def main():
    print('-----------------------------------')
    print('---- Multiplicação de matrizes ----')
    print('-----------------------------------')
    print('\n')
    #definindo o tamanho da matriz A
    m = int(input('Entre com um valor para número de linhas da matriz A: '))
    n = int(input('Entre com um valor para número de colunas da matriz A: '))
    print('\n')
    #definindo o tamanho da matriz B
    p = int(input('Entre com um valor para número de linhas da matriz B: '))
    q = int(input('Entre com um valor para número de colunas da matriz B: '))
    print('\n')
    #condição para multiplicação de matrizes é que a o número de colunas da primeira
    #matriz deve ser igual ao número de linhas da sugunda matriz. Assim, m = p
   
    
    if n == p:
        #criando matriz A
        A = cria_matriz(m, n, 'A')

        #criando matriz B
        B = cria_matriz(p, q, 'B')

        #cria a matriz C, produto entre A e B
        C = prod_matriz(m, q, n, A, B)

        #imprimindo as matrizes A, B e C
        imprime_matriz(A, 'A')
        imprime_matriz(B, 'B')
        imprime_matriz(C, 'C')
        print('***************************************************************')
        print('\n')
        print('Fim do programa')
        #ao final também é possível reinicializar a função main() para o programa
        #ser executado novamente
        #main()
    else:
        print('As ordens das matrizes não permitem realizar a operação de multiplicação!')
        print('\n')
        print('Fim do programa')
        print('***************************************************************')
        #ao final também é possível reinicializar a função main() para o programa
        #ser executado novamente
        #main()

#definindo e criando as funções secundárias usadas pelo programa 
def cria_matriz(lin, col, nome_matriz):
    #adicionando os elementos da matriz
    print (f'Adicone os elementos da matriz {nome_matriz}')
    print('\n')
    i = 0 #numero de linhas
    matriz = []
    while i < lin:
        j= 0
        linha = []
        while j < col:
           el = float(input(f'Entre com o elemento {nome_matriz.lower()}({i+1}x{j+1}): '))
           print('\n')
           linha.append(el)
           j += 1
        matriz.append(linha)
        i += 1
    return matriz


def prod_matriz(linA, colAlinB, colB, matriz_1, matriz_2):
    #construindo a produto
    produto = []
    i = 0 #número de linhas de A
    while i < linA:
        j = 0 #número de colunas em B
        linha = [] #cria a linha de produto
        while j < colAlinB:
            k = 0 #numéro de colunas em A e número de linhas em B
            soma = 0
            while k < colB:
                prod = matriz_1[i][k]*matriz_2[k][j]
                soma = soma + prod
                k += 1
            linha.append(soma)   
            j += 1
        produto.append(linha)
        i += 1
    return produto

def imprime_matriz(matriz, nome_matriz):
    #imprimindo a matriz 
    print('\n')
    print(f'Matriz {nome_matriz}:')
    print('\n')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], ' ', end = '')
        print('\n')

#iniciando execução do programa
main()
    
