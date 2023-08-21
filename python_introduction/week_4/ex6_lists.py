#Ex.6 - Crie um programa que leia inicialmente duas sequências de N
#elementos cada uma e ao final mostre as duas sequências originais e a
#sequência resultante da soma de seus elementos. Exemplo:
#a=[5, 9, 0] b=[12, 34, 101] soma=[17, 43, 101]



N = int(input('Entre com a quantidades de números para duas listas: '))

print('------------------------------------------------------------')

l1 = [] #lista 1
l2 = [] #lista 2
lsoma = [] #lista com a soma

for i in range(0, N, 1):
    num1 = int(input('Digite um número inteiro para a primeira lista: '))
    l1.append(num1)

print('------------------------------------------------------------')

for j in range(0, N, 1):
    num2 = int(input('Digite um número inteiro para a segunda lista: '))
    l2.append(num2)

for k in range(0, N, 1):
    soma = l1[k] + l2[k]
    lsoma.append(soma)

print('------------------------------------------------------------')
           
print('Lista 1: ',l1)
print('Lista 2: ',l2)
print('Lista com a soma dos elementos das listas 1 e 2: ',lsoma)


