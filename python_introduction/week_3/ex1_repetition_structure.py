#Ex.1 - Semana 3 - Estrutura de repetição
#Faça um programa que exiba todos os números de 1 a 100 que
#são divisíveis por 7.

#dá para fazer usando o laço "for", "in" "range()" e da para usar o "while"
#usando o "for":
for x in range(1, 101, 1):
    cond = x % 7 #calcula o resto da divisão por 7
    if cond == 0:
        print(x)

# usando o while:
x = 1
while x <= 100:
    cond = x % 7
    if cond == 0:
        print(x)
    x = x + 1
