#Ex. 5 - Aula semana 1
#Faça um programa que receba dois inteiros x e y e calcule o valor de z,
#dado pela expressão a seguir:
#z = (x^2 +y^2) / (x-y)^2
x = int(input('Digite um valor inteiro para x: '))
y = int(input('Digite um valor inteiro para y: '))
z = (x**2 + y**2) / (x-y)**2
print(f'O valor da expressão z = (x^2 +y^2) / (x-y)^2 é: {z}' )
