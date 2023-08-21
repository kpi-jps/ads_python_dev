#Ex.6 - Semana 3 - Estrutura de repetição
#Faça um programa em Python que leia um conjunto de valores
#correspondentes às notas que os alunos obtiveram em uma prova
#de Algoritmos. Quando o valor fornecido for um número negativo,
#significa que não existem mais notas para serem lidas. Após isso
#seu programa deverá:
#Escrever quantas notas são maiores ou iguais a 6.0
#Escrever quantas notas são maiores ou iguais a 4.0 e menores
#que 6.0
#Escrever quantos notas são menores que 4.0
#Escrever a média das notas fornecidas pelo usuário.

entrada = 0
nota = 0
nota_menor_que_4 = 0
nota_maior_que_4 = 0
nota_maior_que_6 = 0
quantidade_notas = 0
while entrada >= 0:
    entrada = float(input("Entre com os valores de notas entre 1 e 10 ou com valor negativo ou maior que 10 para finalizar as entradas "))
    if entrada >= 0 and entrada <= 10:
        nota += entrada # equivalente: nota = nota + entrada
        elif entrada >= 6:
            nota_maior_que_6 += 1    
        elif entrada >= 4:
            nota_maior_que_4 += 1
        elif entrada < 4:
            nota_menor_que_4 += 1
        quantidade_notas += 1
    else:
        print("Digite um número negativo para cessar as entradas ou um número entre 1 e 10 para as notas")
media = nota / quantidade_notas

print('quantidade de notas inseridas = ', quantidade_notas)
print('notas maiores ou iguais a 6 = ', nota_maior_que_6)
print('notas maiores ou iguais a 4 = ', nota_maior_que_4)
print('notas menores que 4 = ', nota_menor_que_4)
print('média = ', media)

        
        
    
