#Ex.4 - Aula semana 2 - Condicionais
#Faça um algoritmo que receba três valores A, B e C e verifica se
#eles podem ser os comprimentos dos lados de um triângulo. Se
#forem, mostrar se é um triângulo equilátero, isósceles ou escaleno.
#Considere que:
#Para ser triângulo: cada lado é menor que a soma dos outros dois lados.
#Triângulo equilátero: tem três lados iguais
#Triângulo isósceles: tem dois lados iguais e um diferente
#Triângulo escaleno: tem três lados diferentes

A = float(input('Entre com o valor de A: '))
B = float(input('Entre com o valor de B: '))
C = float(input('Entre com o valor de C: '))

#Partindo da informação que para ser triângulo: cada lado é menor
#que a soma dos outros dois lados. Então tem-se que:
#A + B > C
#A + C > B
#B + C > A
#condição de exixtência de um triangulo

if A + B > C and A + C > B and B + C > A:
    print('A, B e C podem ser valores para os lados de um triangulo')
    if A == B and A == C and B == C:
        print('e como A = B = C o triangulo é equilátero')
    elif A == B or B == C or A == C:
        print('e como dois lados são iguais o triangulo é isósceles')
    else:
        print('e como todos os lados são diferentes o triangulo é escaleno')
else:
    print('A, B e C não podem ser valores para os lados de um triangulo')
    print('Pois: A + B < C; A + C < B e B + C < A')
