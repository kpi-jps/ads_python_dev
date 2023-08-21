"""

Atividade prática

Escreva um programa que crie uma lista para representar a turma de
alunos de AP1S1, a partir de dados fornecidos pelo usuário. Para cada
aluno deverão ser gravados os seguintes dados: nome, prontuário e
uma lista de até 4 notas.
turma=[ [nome_aluno1, pront_aluno1, [N1, N2, N3,
N4]], [nome_aluno2, pront_aluno2, [N1, N2, N3]],
...]
A quantidade de notas pode NÃO ser a mesma para todos os alunos, de
modo que você deve estabelecer um critério de parada para a entrada de
notas de cada aluno (por ex., nota negativa). Estabeleça também um
critério de parada para a inclusão de um novo aluno.
Ao final, o programa deverá calcular a média aritmética das notas de cada
aluno e apresentar o nome, o prontuário e a média de todos os alunos da
turma. Deverá apresentar também a maior e a menor média da turma,
bem como informar o nome dos alunos que tiveram a maior e menor
média.

"""

turma = []
maior_media = 0 #valor mínimo da média
menor_media = 10 #valor máximo da média
nome = input('Entre com o nome de aluno ou pressione ENTER para encerrar: ')
while nome != '':
    aluno = []
    aluno.append(nome)
    prontuario = input('Entre com o prontuário do aluno:')
    aluno.append(prontuario)
    notas = []
    nota = 0
    num_notas = 0
    while  nota >= 0 and num_notas < 4:
        nota = float(input('Entre com uma nota ou com um valor negativo para encerrar: ' ))
        if nota > 0:
            notas.append(nota)
            num_notas += 1 #num_notas = num_notas + 1
    aluno.append(notas)
    turma.append(aluno)
    nome = input('Entre com o nome de aluno ou pressione ENTER para encerrar: ')

for i in range(0, len(turma), 1):
    soma = 0
    for j in range(0, len(turma[i][2]), 1):
        soma += turma[i][2][j] #soma = soma + turma[i][2][j]
    media = soma / len(turma[i][2]) 
    turma[i].append(media)
    if media > maior_media:
        maior_media = media
    elif media < menor_media:
        menor_media = media

for i in range(0, len(turma), 1):
    print(f'Aluno: {turma[i][0]} - Prontuário: {turma[i][1]} - Média: {turma[i][3]}')

for i in range(0, len(turma), 1):
    if maior_media == turma[i][3]:
        print(f'Maior média apresentada pelo aluno: {turma[i][0]} - {maior_media}')
    elif menor_media == turma[i][3]:
        print(f'Menor média apresentada pelo aluno: {turma[i][0]} - {menor_media}')
    
