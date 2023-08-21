#Ex.7 - Crie um programa que dada uma sequência de N elementos fornecidos
#pelo usuário mostre a sequência original e a sequência elevada ao cubo.



N = int(input('Entre com a quantidades de números para a lista: '))

print('------------------------------------------------------------')

l1 = [] #lista digitada
l2 = [] #lista com elementos elevado ao cubo

for i in range(0, N, 1):
    num = int(input('Digite um número inteiro para a lista: '))
    l1.append(num)

print('------------------------------------------------------------')

for j in range(0, N, 1):
    el = l1[j]*l1[j]*l1[j] #ou usar l1[j]**3
    l2.append(el)

print('------------------------------------------------------------')
           
print('Lista digitada: ',l1)
print('Lista digitada com elementos elevados ao cubo: ',l2)



