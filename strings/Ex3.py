#Ex3. Escreva um programa que verifique se duas strings fornecidas pelo
#usuário são iguais e mostre o total de caracteres de cada uma delas.
#Diferencie letras maiúsculas das minúsculas.

string1 = input('Digite uma palavra ou frase: ')
string2 = input('Digite outra palavra ou frase: ')

if string1 == string2:
    print('As palavras ou frases digitadas são identicas e apresentam',len(string1), 'caracteres!')
else:
    print('As palavras ou frases digitadas são diferentes!')
    


