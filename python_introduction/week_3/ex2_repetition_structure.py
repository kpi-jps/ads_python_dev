#Ex.2 - Semana 3 - Estrutura de repetição
#Faça um programa que exiba todos os números de 1 a 100 que
#são divisíveis por 7 e por 3.

#dá para fazer usando o laço "for", "in" "range()" e da para usar o "while"
#usando o "for":
for x in range(1, 101, 1):
    cond1 = x % 3 #calcula o resto da divisão por 3
    cond2 = x % 7 #calcula o resto da divisão por 7
    if cond1 == 0:
        if cond2 == 0:
            print(x,' é divisível por 3 e por 7')
        else:
            print(x,' é divisível por 3')
    elif cond2 == 0:
        print(x,' é divisível por 7')
    
# usando o while:
#x = 1
#while x <= 100:
#    cond1 = x % 3
#    cond1 = x % 7
#    if cond1 == 0:
#       if cond2 == 0:
#           print(x,' é divisível por 3 e por 7')
#       else:
#           print(x,' é divisível por 3')
#    elif cond2 == 0:
#        print(x,' é divisível por 7')
#    x = x + 1
