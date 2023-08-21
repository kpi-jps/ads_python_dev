#Ex.3 - Aula semana 2 - Condicionais
#Escreva um programa que leia três números inteiros e os imprima em
#ordem crescente.
x1 = int(input('Digite um número inteiro para x1 '))
x2 = int(input('Digite um número inteiro para x2 '))
x3 = int(input('Digite um número inteiro para x3 '))

if x1 > x2 > x3:
    print(f'a ordem crescente para os números digitados é: {x1}, {x2}, {x3}')
if x2 > x1 > x3:
    print(f'a ordem crescente para os números digitados é: {x2}, {x1}, {x3}')
if x3 > x2 > x1:
    print(f'a ordem crescente para os números digitados é: {x3}, {x2}, {x1}')
if x2 > x1 > x3:
    print(f'a ordem crescente para os números digitados é: {x2}, {x1}, {x3}')
