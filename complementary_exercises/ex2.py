"""
Exercícios Estrutura de Repetição - Extra
Ex2. Faça um programa que gere aleatoriamente um número entre 0 e 100. Em seguida,
o programa deve pedir que o usuário tente acertar qual o número gerado. Por
exemplo, suponha que o programa gere o número 21 e o usuário tente adivinhá-lo
digitando o número 50. O programa deve, então, imprimir a mensagem:
“Número incorreto, tente um valor menor”. O usuário digita, então, o número 10.
Após a análise deste número, o programa deverá imprimir a mensagem “Número
incorreto, tente um valor maior”. O processo deve continuar até que o usuário
acerte o número gerado pelo programa. O programa deve finalizar informando o
número de tentativas até o acerto.
Obs: use a função randint() para gerar o número aleatoriamente. 
"""
import random

num_ran = 17##random.randint(0, 100)
cont = 1 #precisa ser iniciado em 1 para contar a primeira tentativa
num = int(input('Entre com um número inteiro entre 0 e 100 '))
if num == num_ran:
    print('Você acertou o número escolhido pelo computador! ')
else:
    num = int(input('Você errou, tente outro número! '))
    while num != num_ran:    
        if num > num_ran:
            num = int(input('Você errou novamente, tente um número menor '))
        elif num < num_ran:
            num = int(input('Você errou novamente, tente um número maior '))
        else:
            print(f'Parabéns você acertou o número depois de {cont} tentativas!')
        cont += 1
    
        

