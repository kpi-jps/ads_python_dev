#Ex1. - Dada a lista L = [8,0,97,105,21,303], faça um programa que imprima:
#O maior elemento da lista
#O menor elemento da lista
#A soma de todos os elementos da lista
#Os elementos ímpares
#Os elementos maiores do que 18
#Obs: não use funções prontas.

L = [8,0,97,105,21,303]

#é preciso atribuir a num_max e num_min, algum elemento da lista
#pode ser qualquer um deles, eu escolhi o primeiro, de índice 0, o que é mais lógico
#recomendável usar uma estrutura de repetição para cada problema

num_max = L[0]
i = 0
while i < len(L):
    if L[i] > num_max:
        num_max = L[i]
    i += 1 #i = i + 1
print('O maior elemento da lista é ',num_max)


num_min = L[0]
i = 0
while i < len(L):
    if L[i] < num_min:
        num_min = L[i]
    i += 1
print('O menor elemento da lista é ',num_min)

soma = 0
i = 0
while i < len(L):
    soma += L[i] #soma = soma + L[i]
    i += 1
print('A soma dos elementos da liste é igual a ',soma)


print('Os elementos ímpares da lista são: ')
i = 0
while i < len(L):
    if L[i] % 2 != 0:
        print(L[i])
        # a "print(L[i], ' - ', end = '')" imprime os elementos na mesma linha
    i += 1

print('Os elementos maiores que 18 são: ')  
i = 0
while i < len(L):
    if L[i] > 18:
        print(L[i])
    i += 1
     

