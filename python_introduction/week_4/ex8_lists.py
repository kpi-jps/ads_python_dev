#Ex.8 - Crie um programa que leia inicialmente uma sequência de N números
#inteiros fornecidos pelo usuário e mostre ao final da leitura a sequência
#original e a sequência invertida.

N = int(input('Entre com a quantidades de números para a lista: '))

print('------------------------------------------------------------')

l1 = [] #lista digitada
l2 = [] #lista invertida

for i in range(0, N, 1):
    num = int(input('Digite um número inteiro para a lista: '))
    l1.append(num)

print('------------------------------------------------------------')


for j in range(len(l1)-1, -1 , -1): # aqui é necessário usar -1 para o índice final
    #len(l1)-1 como índice inicial
    l2.append(l1[j])


# é possível também fazer como o while:
#k = len(l1)-1
#while k >=0:
    #l2.append(l1[k])
    #k -= 1 #k = k - 1

print('------------------------------------------------------------')
           
print('Lista digitada: ',l1)
print('Lista invertida: ',l2)



