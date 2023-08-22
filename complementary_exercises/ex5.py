'''
Exercícios Estrutura de Repetição - Extra
Ex4.Faça um programa que calcule e apresente o mmc entre dois números.
'''

n1 = int(input('Entre com o primeiro número para calculo do MMC '))
n2 = int(input('Entre com o segundo número para calculo do MMC '))

resto1 = n1
x1 = 2
resultado1 = 1


resto2 = n2
x2 = 2
resultado2 = 1


while resto1 > 1:
    if resto1 % x1 == 0:
        resto1 = resto1 / x1
        resultado1 = resultado1 * x1
    else:
        x1 += 1

while resto2 > 1:
    if resto2 % x2 == 0:
        resto2 = resto2 / x2
        resultado2 = resultado2 * x2
    else:
        x2 += 1

MMC = resultado1*resultado2
print(f'O MMC para os números digitados é {MMC}')
        
          
