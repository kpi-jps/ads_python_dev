#Ex7. Faça um programa que permita ao usuário digitar o seu nome e em
#seguida mostre-o de trás para frente utilizando somente letras
#maiúsculas.

string1 = input('Digite um nome: ')
string1 = string1.upper()
string2 = ''

for i in range(len(string1) - 1,-1 , -1):
    string2 = string2 + string1[i]
print(string2)
