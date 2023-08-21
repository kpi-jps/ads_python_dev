#Ex.4 - Crie um programa que leia inicialmente uma sequência de N números
#inteiros e ao seu final mostre a sequência original, a soma de seus
#elementos que forem pares e a multiplicação dos elementos que
#forem ímpares.
N = int(input('Entre com a quantidades de número para a sequencia: '))
seq = []
soma = 0
prod = 1
for i in range(0, N, 1):
    num = int(input('Digite um número inteiro: '))
    seq.append(num)

for j in range(0, len(seq), 1):
    if seq[j] % 2 == 0:
        soma += seq[j] #soma = soma + num
    else:
        prod *= seq[j] #prod = prod * seq[j]  

print('A sequência de números digitados é ',seq)
print('A soma dos elementos pares é = ',soma)
print('O produto dos elementos ímpares é = ',prod)

