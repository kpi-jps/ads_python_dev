"""
Exercícios Estrutura de Repetição - Extra
Ex1. Elabore um programa que efetue a soma de todos os números ímpares que são
múltiplos de 3 e que se encontram no intervalo de 1 a 500.
"""

soma = 0
i = 1
while i <= 500:
    if i % 2 != 0 and i % 3 == 0:
        soma += i #soma = soma + i
    i += 1 #i = i + 1
print(f'A soma dos números ímpares entre 1 e 500 é = {soma}')
