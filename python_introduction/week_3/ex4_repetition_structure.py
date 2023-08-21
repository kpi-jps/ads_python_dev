#Ex.4 - Semana 3 - Estrutura de repetição
#Faça um programa que receba um número inteiro maior que 1,
#verifique se o número é primo ou não e mostre a mensagem de
#número primo ou de número não primo. Obs: Um número é
#primo quando é divisível apenas por 1 e por ele mesmo.

num = int(input('Digite um número inteiro maior > 1 '))

if num > 1:
    x = 2
    while num % x != 0:
        x += 1 #equivalente: x = x + 1
        
    if num != x:
        print(f'{num} não é um número primo!')
                
    else:
        print(f'{num} é um número primo!')
        
else:
    print(f'{num} < 1 , digite um número > 1')
      
