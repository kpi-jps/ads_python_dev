#Ex.5 - Semana 3 - Estrutura de repetição
#Faça um programa em Python que receba dois valores inteiros,
#representando a base e o expoente. O programa deverá calcular e
#apresentar o resultado da base elevada ao expoente. Por
#exemplo, para base = 5 e expoente = 3, ou seja, 53
#, o programadeverá imprimir 125.
#Obs: não utilize o operador de exponenciação (**). Utilize
#somente estrutura de repetição.

#usando o "for"
base = int(input('Digite um número inteiro para a base '))
expoente = int(input('Digite um número inteiro para expoente '))
resultado = 1
for x in range(0, expoente, 1):
    resultado = resultado * base
print(base, ' ^ ', expoente, ' = ', resultado)

#usando "while"
x = 1
resultado = 1
while x <= expoente:
    resultado = resultado * base
    x = x + 1
print(base, ' ^ ', expoente, ' = ', resultado)
    
