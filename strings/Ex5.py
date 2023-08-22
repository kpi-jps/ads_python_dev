#Ex5. Faça um programa que recebe uma frase e retorna o número de
#palavras que a frase contém.

string1 = input('Digite uma frase: ')
contador = 1 #precisa começar em um para contar a primeira palavra

for i in range(0, len(string1), 1):
    if string1[i] == ' ':
        contador += 1
if contador == 1:
    print(f'A frase digitada contém apenas uma palavra!')
else:
    print(f'A frase digitada contém {contador} palavras!')
    

