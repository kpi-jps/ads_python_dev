#Atividade 1 - Semana 3 - Estrutura de repetição
#Faça um programa para mostrar a tabuada de um número qualquer
#fornecido pelo usuário.

numero = int(input("Digite um número inteiro para escrever a sua tabuada: "))

for x in range(1, 11, 1):
    resultado = numero * x
    print(f'{numero} x {x} = {resultado}')
    #daria para usar também:
    #print(numero, " x ", x, " = "resultado')
