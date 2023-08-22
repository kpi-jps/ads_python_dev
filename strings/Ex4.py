#Ex4. Escreva um programa que reconhece se uma string é um palíndromo,
#ou seja, se lida do início para o fim é igual se lida do fim para o início.
#Exemplos: arara, ovo, reter e Renner.

string1 = input('Digite uma palavra: ')
string1 = string1.upper() #python é case sensitive
string2 = "" #string invertida
i = len(string1) - 1
while i >= 0:
    string2 = string2 + string1[i]
    i -= 1
if string1 == string2:
    print('A palavra digitada é um palíndromo')
else:
    print('A palavra digitada não é um palíndromo')
    

