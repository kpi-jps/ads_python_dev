#Ex.3 - Crie um programa que leia inicialmente uma sequência de N notas de
#alunos fornecidas pelo usuário e ao final mostre a sequência e sua
#média aritmética.

N = int(input('Entre com a quantidades de notas a serem digitadas: '))
notas = []
soma = 0
for i in range(0, N, 1):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    soma += nota
media = soma / N
print('A lista de notas digitadas é',notas)
print('A média das notas é',media)

