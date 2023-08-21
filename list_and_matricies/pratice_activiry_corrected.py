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
nome = input('Entre com o nome de aluno ou pressione ENTER para encerrar: ')
while nome != '':
    aluno = []
    aluno.append(nome)
    prontuario = input('Entre com o prontuário do aluno:')
    aluno.append(prontuario)
    notas = []
    nota = float(input('Entre com uma nota ou com um valor negativo para encerrar: ' ))
    num_notas = 1
    while  nota >= 0 and num_notas <= 4:
        notas.append(nota)
        nota = float(input('Entre com uma nota ou com um valor negativo para encerrar: ' ))  
        num_notas += 1 #num_notas = num_notas + 1
    aluno.append(notas)
    turma.append(aluno)
    nome = input('Entre com o nome de aluno ou pressione ENTER para encerrar: ')

for i in range(len(turma)): #equivalente a range(0, len(turma), 1), 0 e 1 podem ser omitidos
    soma = 0
    for j in range(len(turma[i][2])): #equivalente range(0, len(turma[i][2]), 1)
        soma += turma[i][2][j] #soma = soma + turma[i][2][j]
    #essa estrutura condicional impede erro por divisão por zero em média
    #e por não definir a variável média    
    if len(turma[i][2]) > 0:
        media = soma / len(turma[i][2])
    else:
        media = 0
    turma[i].append(media)

for i in range(0, len(turma), 1):
    print(f'Aluno: {turma[i][0]}')
    print(f'Prontuário: {turma[i][1]}')
    print(f'Média: {turma[i][3]}')
    print('*******************************\n\n')


menor_media = turma[0][3] #valor inicial atribuído arbitrariamente
for i in range(len(turma)): #equivalente a range(0, len(turma), 1)
    if turma[i][3] < menor_media:
        menor_media = turma[i][3]

maior_media = turma[0][3] #valor inicial atribuído arbitrariamente
for i in range(len(turma)): #equivalente a range(0, len(turma), 1)
    if turma[i][3] > maior_media:
        maior_media = turma[i][3]
        
print(f'Maior média da turma: {maior_media}')
print(f'Aluno(s) que obtiveram a maior média:')
for i in range(len(turma)): #equivalente a range(0, len(turma), 1)
    if maior_media == turma[i][3]:
        print(turma[i][0])
        print('*******************************\n')

print(f'Menor média da turma: {menor_media}')
print(f'Aluno(s) que obtiveram a menor média:')
for i in range(len(turma)): #equivalente a range(0, len(turma), 1)
    if menor_media == turma[i][3]:
        print(turma[i][0])
        print('*******************************\n')
    
