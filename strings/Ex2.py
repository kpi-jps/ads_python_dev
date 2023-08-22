#Ex2. Escreva um programa que remove todas as ocorrências de uma letra
#de uma string. A string e a letra devem ser fornecidas pelo usuário.

frase = input('Digite uma palavra ou frase: ')
nova_frase = ''
caracter = input('Digite uma letra: ')

check = False #variável de checagem

for i in frase:
    if i == caracter:
        check = True
if check:
    index = frase.find(caracter)
    k = 0
    for k in frase:
        if k != caracter:
            nova_frase = nova_frase + k 
    print(nova_frase) 

else:
    print('O caracter digitado não existe na frase!')

