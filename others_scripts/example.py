def exibirMenu():
    print("Menu")
    print("0 - sair")
    print("1 - cadastrar aluno")
    print("2 - carregar dados")
    print("3 - carregar e exibir dados formatados")

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

def lerDadosAlunos():
    arquivoLeitura =open("CadastroAlunos.txt",'r')
    contador = 0
    for linha in arquivoLeitura: # para cada linha do meu arquivo de leitura
        linha = linha.replace("\n","")
        lista = linha.split(";")
        print(lista)
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



opcao = -1
qtddAlunos = 0
while opcao !=0:
    exibirMenu()
    opcao = int(input("Digite a opcao: "))
    if opcao == 1:
        cadastrarAluno()
    elif opcao == 2:
        qtddAlunos = lerDadosAlunos()
    elif opcao == 3:
        qtddAlunos = lerDadosFormatado()
