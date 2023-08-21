#Ex.1 - Aula semana 2 - Condicionais
#Faça um programa que receba 5 números inteiros e informe o maior
#entre eles.
x1 = int(input('Digite um número inteiro para x1 '))
x2 = int(input('Digite um número inteiro para x2 '))
x3 = int(input('Digite um número inteiro para x3 '))
x4 = int(input('Digite um número inteiro para x4 '))
x5 = int(input('Digite um número inteiro para x5 '))

if x1 > x2 and x1 > x3 and x1 > x4 and x1 > x5 :
    print(f'o maior número digitado foi {x1}')

if x2 > x1 and x2 > x3 and x2 > x4 and x2 > x5 :
    print(f'o maior número digitado foi {x2}')

if x3 > x1 and x3 > x2 and x3 > x4 and x3 > x5 :
    print(f'o maior número digitado foi {x3}')

if x4 > x1 and x4 > x2 and x4 > x3 and x4 > x5 :
    print(f'o maior número digitado foi {x4}')

if x5 > x1 and x5 > x2 and x5 > x3 and x5 > x4 :
    print(f'o maior número digitado foi {x5}')

#pode usar o 'print' também da seguinte modo:
# print('string', number)
