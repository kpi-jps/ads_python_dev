#Atividade 2 - Semana 3 - Estrutura de repetição
#Refaça o programa da tabuada (Atividade 1) usando a
#estrutura while.

numero = int(input("Digite um número inteiro para escrever a sua tabuada: "))
x = 0
while x <= 10:
    resultado = numero * x
    print(f'{numero} x {x} = {resultado}')
    x = x + 1
    #daria para usar também:
    #print(numero, " x ", x, " = "resultado')
