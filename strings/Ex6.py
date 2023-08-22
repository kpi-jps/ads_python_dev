#Ex6. Faça um programa que solicite o nome do usuário e imprima-o na
#vertical e em formato de escada. Por exemplo, o nome “Fulano”, o
#programa deverá imprimir:
#F
#Fu
#Ful
#Fula
#Fulan
#Fulano

string1 = input('Digite um nome: ')
string2 = ''

for i in range(0, len(string1), 1):
    string2 = string2 + string1[i]
    print(string2)
