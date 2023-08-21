'''
Exercício - aula Lista de listas e matrizes
Ex3.Faça um programa que solicite do usuário um valor N, representando
a dimensão de uma matriz quadrada (matriz A). Em seguida, o
programa deverá solicitar do usuário os elementos da matriz A e,
posteriormente, deverá verificar se A é simétrica. Obs: Matriz
simétrica: matriz quadrada de ordem n tal que A = At
'''

#definindo o tamanho da matriz
n = int(input('Defina onúmero de linhas e colunas da matriz quadrada: ')) #número de linhas e colunas

#construindo a matriz A
i = 0 
A = []
print('Entre com os elementos da matriz A 3x2')
while i < n:
    j = 0
    linha = []
    while j < n:
       el = float(input(f'Entre com o elemento el{i+1}x{j+1}: '))
       linha.append(el)
       j += 1
    A.append(linha)
    i += 1


#criando a estrutura da matriz transposta de A (At)
At = []
i = 0
while i < n: #aqui i = número de colunas e j = número de linhas
    j = 0
    linha = []
    while j < n:
        el = A[j][i]
        linha.append(el)
        j += 1
    At.append(linha)
    i += 1

#imprimindo as matrizes
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

#checando se a matriz e sua transposta são iguais, o que indica se a matriz é
#simétrica
check = n*n #variável de checagem
cont = 0 #contador de igualdade entre os elementos da matriz
#ao final da comparação de todos os elementos a matriz será simétrica
#se check = cont.
i = 0
while i < n:
    j = 0
    while j < n:
        if A[i][j] == At[i][j]:
            cont += 1
        j += 1
    i += 1

if cont == check:
    print('A matriz digitada é simétrica')
else:
    print('A matriz digitada não é simétrica')
print(check)
print(cont)
   
