#Ex.9 - Crie um programa que leia inicialmente uma sequência de N elementos
#inteiros positivos fornecidos pelo usuário e substitua seus elementos de
#valor ímpar por -1 e os pares por +1. Ao final imprima a sequência
#original e a sequência alterada.

N = int(input('Entre com a quantidades de números para a lista: '))

print('------------------------------------------------------------')

l1 = [] #lista digitada
l2 = [] #alterada

for i in range(0, N, 1):
    num = int(input('Digite um número inteiro para a lista: '))
    l1.append(num)

print('------------------------------------------------------------')


for j in range(0, len(l1), 1): 
    if l1[j] == 0:
        l2.append(1) #para p zero que é considerado par
    elif l1[j] % 2 == 0:
        l2.append(1) #para números pares
    else:
        l2.append(-1) #para números ímpares

   

print('------------------------------------------------------------')
           
print('Lista digitada: ',l1)
print('Lista alterada: ',l2)



