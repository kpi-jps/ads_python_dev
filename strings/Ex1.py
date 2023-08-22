#Ex1. Escreva um programa que remove a primeira ocorrência de uma letra
#de uma string. A string e a letra devem ser fornecidas pelo usuário.

frase = input('Digite uma palavra ou frase: ')

caracter = input('Digite uma letra: ')

check = False

for i in frase:
    if i == caracter:
        check = True
if check:
    index = frase.find(caracter)
    print(frase[:index] + frase[index + 1:]) #usando operador de fatiamento ":"
else:
    print('O caracter digitado não existe na frase!')
