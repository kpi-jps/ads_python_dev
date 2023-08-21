#Ex.8 - Semana 3 - Estrutura de repetição
#Faça um programa que leia um número inteiro >= 0 e calcule o seu
#fatorial.



fatorial = 0
num = int(input('Entre com um número inteiro '))
if num < 0:
    print('O número digitado é menor que 0')
elif num == 0:
    print(f'{num}! = {fatorial}')
else:
    x = 1
    fatorial = num
    while x < num:
        fatorial = fatorial * (num - x)
        x += 1
if num != 0:
print(f'{num}! = {fatorial}')
