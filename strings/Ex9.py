#Ex9. Um anagrama é uma palavra que é feita a partir da transposição das
#letras de outra palavra ou frase. Por exemplo, “Iracema” é um
#anagrama para “America”. Escreva um programa que decida se uma
#string é um anagrama de outra string, ignorando os espaços em
#branco. O programa deve considerar maiúsculas e minúsculas como
#sendo caracteres iguais, ou seja, “a” = “A”.

string1 = input('Digite uma palavra: ')
string2 = input('Digite outra palavra: ')

string1 = string1.upper()
string2 = string2.upper()

i = 0
while i < len(string1):
    caracter = string1[i]
    #desconsiderando acentuação
    if caracter == 'Á' or caracter == 'À' or caracter == 'Ã' or caracter == 'Â':
        string1 = string1.replace(caracter, 'A')
    elif caracter == 'É' or caracter == 'È' or caracter == 'Ê':
        string1 = string1.replace(caracter, 'E')
    elif caracter == 'Í' or caracter == 'Ì' or caracter == 'Î':
        string1 = string1.replace(caracter, 'I')
    elif caracter == 'Ó' or caracter == 'Ò' or caracter == 'Ô':
        string1 = string1.replace(caracter, 'O')
    elif caracter == 'Ú' or caracter == 'Ù':
        string1 = string1.replace(caracter, 'U')
    elif caracter == ' ':
        string1 = string1[:i] + string1[i + 1:] #eliminando espaços em branco
    i += 1

j = 0
while j < len(string2):
    caracter = string2[j]
    #desconsiderando acentuação
    if caracter == 'Á' or caracter == 'À' or caracter == 'Ã' or caracter == 'Â':
        string2 = string2.replace(caracter, 'A')
    elif caracter == 'É' or caracter == 'È' or caracter == 'Ê':
        string2 = string2.replace(caracter, 'E')
    elif caracter == 'Í' or caracter == 'Ì' or caracter == 'Î':
        string2 = string2.replace(caracter, 'I')
    elif caracter == 'Ó' or caracter == 'Ò' or caracter == 'Ô':
        string2 = string2.replace(caracter, 'I')
    elif caracter == 'Ú' or caracter == 'Ù':
        string2 = string2.replace(caracter, 'U')
    elif caracter == ' ':
        string2 = string2[:j] + string2[j + 1:] #eliminando espaços em branco
    j += 1

 
if len(string1) == len(string2):
    string3 = string1
    k = 0
    while k < len(string1):
        
        l = 0
        while l < len(string2):
            if string1[k] == string2[l]:
                string3 = string3.replace(string1[l], '')
            l += 1
        k += 1
    if string3 == '':
        print('As palavras digitadas são anagramas')
    else:
        print('As palavras digitadas não são anagramas')

else:
    print('As palavras digitadas não são anagramas')

