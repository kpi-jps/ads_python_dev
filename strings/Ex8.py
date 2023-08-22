#Ex8. Dada uma string com uma frase informada pelo usuário (incluindo
#espaços em branco), conte a quantidade de espaços em branco e a
#quantidade de vezes que aparecem as vogais a, e, i, o, u.


string1 = input('Digite um nome: ')
string1 = string1.upper() #é necessário tornar todas maisculas para contar as vogais
contador1 = 0 #contador de espaços em branco
contador2 = 0 #contador de vogais

for i in range(0, len(string1), 1):
    if string1[i] == ' ':
        contador1 += 1
    elif string1[i] == 'A' or string1[i] == 'Ã':
        contador2 += 1
    elif string1[i] == 'Á' or string1[i] == 'À' or string1[i] == 'Â':
        contador2 += 1
    elif string1[i] == 'E' or string1[i] == 'É' or string1[i] == 'Ê':
        contador2 += 1
    elif string1[i] == 'I' or string1[i] == 'Í' or string1[i] == 'Î':
        contador2 += 1
    elif string1[i] == 'O' or string1[i] == 'Ó' or string1[i] == 'Ô':
        contador2 += 1
    elif string1[i] == 'U' or string1[i] == 'Ú':
        contador2 += 1

print(f'A frase digitada contem {contador1} espaços em branco e {contador2} vogais')

#este exercício também pode ser feito usando o método count()

contador1 = 0 
contador2 = 0 

contador1 = string1.count(' ')
contador2 = contador2 + string1.count('A')
contador2 = contador2 + string1.count('Ã')
contador2 = contador2 + string1.count('Á')
contador2 = contador2 + string1.count('Â')
contador2 = contador2 + string1.count('E')
contador2 = contador2 + string1.count('É')
contador2 = contador2 + string1.count('Ê')
contador2 = contador2 + string1.count('I')
contador2 = contador2 + string1.count('Í')
contador2 = contador2 + string1.count('Î')
contador2 = contador2 + string1.count('O')
contador2 = contador2 + string1.count('Ó')
contador2 = contador2 + string1.count('Ô')
contador2 = contador2 + string1.count('U')
contador2 = contador2 + string1.count('Ú')

print(f'A frase digitada contem {contador1} espaços em branco e {contador2} vogais')
