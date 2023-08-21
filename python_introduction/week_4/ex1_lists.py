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
num_max = L[0]
num_min = L[0]
maiores_que_18 = []
impares = []
pares = []
#i = 0
for i in range(0, len(L), 1):
    if L[i] > num_max:
        num_max = L[i]
    elif L[i] < num_min:
        num_min = L[i]
    if L[i] == 0:
        pares.append(L[i])
    elif L[i] % 2 == 0:
        pares.append(L[i])
    else:
        impares.append(L[i])
    if L[i] > 18:
        maiores_que_18.append(L[i])

#imprimindo os resultados
print('O maior elemento da lista é ',num_max)
print('O menor elemento da lista é ',num_min)
print('Os elementos ímpares da lista são ',impares)
print('Os elementos pares da lista são ',pares)
print('Os elementos maiores que 18 são ',maiores_que_18)
#dica da professora: manter as estruturas de repetição específicas. No
#caso do exercício fazer uma estrutura de repetição para cada problema
