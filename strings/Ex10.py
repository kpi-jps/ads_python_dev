#Ex10. Escreva um programa que solicite ao usuário a entrada de um
#número inteiro positivo ou negativo e mostre a quantidade de dígitos
#desse número.

entrada = int(input('Digite um número inteiro positivo ou negativo: '))
if entrada >= 0:
    string1 = str(entrada)
    digitos = len(string1)
else:
    string1 = str(entrada)
    digitos = len(string1) - 1

print(f'O número digitado apresenta {digitos} digitos!')
