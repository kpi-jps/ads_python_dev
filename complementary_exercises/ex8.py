'''
Exercícios Estrutura de Repetição - Extra
Ex8. Calcular e escrever o valor do número pi, com precisão de 0.0001, usando a
a série :
pi = 4 - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + ...
'''
pi = 0
div = 1
num_termos = 20000
cont = 0
while cont < num_termos:
    if cont % 2 == 0:
        pi = pi + (4/div)
    else:
        pi = pi - (4/div)
    div += 2
    cont += 1

print(pi)
print(cont)

