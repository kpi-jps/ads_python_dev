def exibirMenu():
    print("Menu")
    print("0 - sair")
    print("1 - cadastrar aluno")
    print("2 - carregar dados")
    print("3 - carregar e exibir dados formatados")
    print("4 - informar a média de idade dos alunos")
    print("5 - exibir matriz de dados")
    print("6 - exibir a média de idade dos alunos de ADS")
    print("7 - exibir o nome e curso do aluno mais velho")
    print("8 - informar quantos alunos existem em cada curso")

def cadastrarAluno():
    #arquivo = open('CadastroAlunos.txt','w') -> com o w um arquivo novo sempre é gerado
    arquivo = open('CadastroAlunos.txt','a') #-> com o a eu escrevo no final do arquivo
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    curso = input("Digite o curso: ")
    #andre;23;ads
    #maria;34;tpg
    linha = nome+";"+idade+";"+curso+"\n"
    arquivo.write(linha)
    arquivo.close()

def lerDadosAlunos(mat):
    arquivoLeitura =open("CadastroAlunos.txt",'r')
    contador = 0
    for linha in arquivoLeitura: # para cada linha do meu arquivo de leitura
        linha = linha.replace("\n","")
        lista = linha.split(";")
        #print(lista)
        mat.append(lista) #adicionando uma linha(lista) na minha matriz(mat)
        contador = contador + 1
    return contador

def lerDadosFormatado():
    arquivo = open("CadastroAlunos.txt",'r')
    contador = 0
    for linha in arquivo: # para cada linha do meu arquivo de leitura
        linha = linha.replace("\n","")
        lista = linha.split(";")
        contador = contador + 1
        print("\nAluno #" + str(contador))
        print("Nome: " + lista[0])
        print("Idade: "+ lista[1])
        print("Curso: " + lista[2])


def exibirMatriz(mat,qtddLinhas):
    for i in range(qtddLinhas):
        print(mat[i])

def calcularMediaIdade(mat,qtddLinhas):
    soma = 0
    for i in range(qtddLinhas):
        soma = soma + int(mat[i][1])
    #print("soma: " + str(soma))
    media = soma / qtddLinhas
    return media

# calculando a média de idade dos alunos de ADS
def calcularMediaIdadeADS(mat,qtddLinhas):
    soma = 0
    contador = 0
    for i in range(qtddLinhas):
        if mat[i][2].upper() == 'ADS':
            soma = soma + int(mat[i][1])
            contador += 1
    media = soma / contador
    return media

# exibindo o nome e curso do aluno mais velho
def alunoMaisVelho(mat,qtddLinhas):
    maiorIdade = 0
    indice = 0
    for i in range(qtddLinhas):
        if int(mat[i][1]) > maiorIdade:
            maiorIdade = int(mat[i][1])
            indice = i
    return 'Nome: ' + mat[indice][0] + ';' + 'Aluno: ' + mat[indice][2]

# informando quantos alunos existem em cada curso
def alunosNosCursos(mat,qtddLinhas):
    cursos = []
    alunos = []
    for i in range(qtddLinhas):
        if len(cursos) == 0:
            cursos.append(mat[i][2].upper())
        else:
            check = True
            for j in range(len(cursos)):
                if mat[i][2].upper() == cursos[j]:
                    check = False
            if check:
                cursos.append(mat[i][2].upper())
    for i in range(len(cursos)):
        contador = 0
        for j in range(qtddLinhas):
            if cursos[i] == mat[j][2].upper():
                contador += 1
        alunos.append(contador)
    info = ''
    for i in range(len(cursos)):
        info += cursos[i] + ':' + str(alunos[i]) + ' alunos \n'
    
    return info
    

opcao = -1
qtddAlunos = 0
matriz = []
while opcao !=0:
    exibirMenu()
    opcao = int(input("Digite a opcao: "))
    if opcao == 1:
        cadastrarAluno()
    elif opcao == 2:
        qtddAlunos = lerDadosAlunos(matriz)
    elif opcao == 3:
        qtddAlunos = lerDadosFormatado()
    elif opcao == 4:
        qtddAlunos = lerDadosAlunos(matriz)
        mediaIdade = calcularMediaIdade(matriz, qtddAlunos)
        print("Media de Idade: " + str(mediaIdade))
    elif opcao == 5:
        exibirMatriz(matriz, qtddAlunos)
    elif opcao == 6:
        qtddAlunos = lerDadosAlunos(matriz)
        mediaIdadeADS = calcularMediaIdadeADS(matriz, qtddAlunos)
        print("Media de Idade dos alunos de ADS: " + str(mediaIdadeADS))
    elif opcao == 7:
        print('Aluno mais velho: ')
        print(alunoMaisVelho(matriz, qtddAlunos))
    elif opcao == 8:
        print('Quantidade de alunos nos cursos: ')
        print(alunosNosCursos(matriz, qtddAlunos))
