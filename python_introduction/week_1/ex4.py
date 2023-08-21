#Ex. 4 - Aula Semana 1
#Faça um programa que leia 2 notas de um aluno, onde a primeira nota
#possui peso um, a segunda possui peso dois. Calcule a média
#ponderada do aluno baseada nos pesos e exiba.
nota1 = float(input('Digite o valor da nota 1'))
nota2 = float(input('Digite o valor da nota 2'))
media = (nota1 * 1 + nota2 * 2)/3
print(f'A média do aluno é: {media}')
