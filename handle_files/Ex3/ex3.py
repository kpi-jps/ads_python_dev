'''
Faça um programa que crie um arquivo denominado “Notas_AP1S1.txt”, para
armazenar informações sobre as notas obtidas por cada aluno da disciplina de
Algoritmos em cada prova. Considere que cada aluno fara 3 provas e a média final será
a média ponderada das provas, sendo que a primeira e a segunda têm peso 0,3 e a
terceira tem peso 0,4. Cada linha do arquivo terá o nome de um aluno, o seu prontuário
e as notas das 3 provas, conforme no exemplo a seguir:
Maria sc365987 6.5 4.0 7.5
Roberto sc569874 4.5 3.0 6.0
Carlos sc222222 7.0 8.0 9.0
Pedro sc112141 9.0 6.0 10.0
O programa deverá ler o arquivo criado ( Notas_AP1S1.txt ), calcular e apresentar:
a) A média final de cada aluno (média ponderada das 3 provas);
b) A quantidade de alunos aprovados na disciplina (ou seja, que obtiveram
média final maior do que 6.0);
c) A quantidade de alunos reprovados na disciplina (ou seja, que obtiveram
média final menor do que 4.0);
d) A quantidade de alunos que farão o IFA (ou seja, que obtiveram média
final maior ou igual a 4.0 e menor do que 6.0).

'''

######################################################################
# definindo a função principal

def main():
    print('========================================================')
    print('                - CALCULADORA DE NOTAS -                ') 
    print('========================================================')
    check = True
    while check:
        print('--------------------------------------------------------')
        print('                      *MENU*                            ')
        print('--------------------------------------------------------')
        print('         [1] - criar novo banco de notas                ')
        print('     [2] - visualizar banco(s) de notas existente(s)    ')
        print('      [3] - visualizar banco de notas específico        ')
        print('       [4] - inserir notas em um banco de notas         ')
        print('        [5] - deletar banco de notas específico         ')
        print('       [6] - calcular médias de um banco de notas       ')
        print('               [7] - encerrar aplicação                 ')
        print('--------------------------------------------------------')
        print('\n')
        entrada = input('Entre com um número para acessar as funções do menu: ')
        print('\n')
        while entrada.isdigit() == False:
            print('\n')
            entrada = input('Entre com um número para acessar as funções do menu: ')
            print('\n')
        if entrada == '1':
            criarBancoDeNotas()
            
        elif entrada == '2':
            visualizaBancosDeNotas()
            
        elif entrada == '3':
            arquivo = input('Entre com o nome do banco de notas: ') + '.txt'
            visualizaBancoDeNotas(arquivo)
            
        elif entrada == '4':
            arquivo = input('Entre com o nome do banco de notas: ') + '.txt'
            insereDados(arquivo)
            
        elif entrada == '5':
            arquivo = input('Entre com o nome do banco de notas: ') + '.txt'
            deletarBancoDeNotas(arquivo)

        elif entrada == '6':
            arquivo = input('Entre com o nome do banco de notas: ') + '.txt'
            calculaMedia(arquivo, 0.3, 0.3, 0.4)
        
        elif entrada == '7':
            print('\n')
            print('Aplicação finalizada!')
            check = False
        else:
            print('\n')
            print('Valor digitado é inválido!')

######################################################################
# definindo as demais funções 

# checa a existência do arquivo
# o parâmetro "arquivo" que corresponde a uma string contendo o nome
# do arquivo contendo todo o caminho e a extensão
def checaArquivo(nome_arquivo):
    # O módulo "os" fornece uma maneira simples de usar funcionalidades
    # que são dependentes de sistema operacional
    import os
    # "os.path.exists(arquivo)" checa se "arquivo" existe. Se
    # sim, a expressão retorna "True" e se não "False"
    if os.path.exists(nome_arquivo):  
        return True
    else:
        return False

# cria um banco de notas novo
def criarBancoDeNotas():
    print('\n')
    novo_banco_notas = input('Entre com um nome para o novo banco de notas: ') + '.txt'
    print('\n')
    if checaArquivo(novo_banco_notas):
        print('Já existe um banco de notas com o nome digitado!')
        print('\n')
    else:
        #cria o arquivo
        arquivo = open(novo_banco_notas, 'w')
        arquivo.close()
        print(f'O arquivo "{novo_banco_notas}" foi criado com sucesso!')
        print('\n')
        # checa se o arquivo contendo as informações sobre os bancos de notas existe
        if checaArquivo('registro.txt'):
            # se "registro.txt" existe o nome do arquivo de banco de notas criado é adicionado a "registro.txt"
            arquivo = open('registro.txt', 'a')
            arquivo.write(novo_banco_notas + '\n') # adicionar '\n' permite iniciar a escrita no arquivo na linha seguinte
            arquivo.close()
        else:
            # se "registro.txt" não existe  ele é criado  e o nome do arquivo de banco de notas criado anteriormente
            # é adicionado a "registro.txt"
            arquivo = open('registro.txt', 'w')
            arquivo.write(novo_banco_notas + '\n') # adicionar '\n' permite iniciar a escrita no arquivo na linha seguinte
            arquivo.close()
            
# permite visualizar todos os bancos de notas criados e registrados em "registro.txt"
def visualizaBancosDeNotas():
    if checaArquivo('registro.txt'):
        print('\n')
        print('Bancos de notas existentes:')
        print('\n')
        arquivo = open('registro.txt', 'r')
        for linha in arquivo:
            print(linha.replace('.txt', ''))
        arquivo.close()
    else:
        print('\n')
        print('Não existem bancos de notas salvos!')
        print('\n')

# visualiza informações de banco de notas específico
def visualizaBancoDeNotas(endereco_arquivo):
    if checaArquivo(endereco_arquivo):
        arquivo = open(endereco_arquivo, 'r')
        # se o arquivo estiver sem conteúdo executa este bloco de código
        if arquivo.read() == '':
            print('\n')
            print('O arquivo não contem informações a serem apresentadas!')
            print('\n')
            arquivo.close()
              
        # se existir conteúdo no arquivo executa este bloco de código
        else:
            arquivo = open(endereco_arquivo, 'r')
            print('\n')
            for linha in arquivo:
                print(linha.replace('|', ' ')) # o replace() substitui o "|" por um espaço em branco
            arquivo.close()   
    else:
        print('\n')
        print('O arquivo procurado não existe!')
        print('\n')

# checa a exitencia de um dado dentro de um arquivo, recebendo como parâmetro a
# referência para o arquivo e o dado (que é uma string) a ser procurado, retornando
# "True" se o dado existe no arquivo e "False" se ele não existe
def checaDados(endereco_arquivo, dado):
    arquivo = open(endereco_arquivo, 'r') # abrindo arquivo para leitura
    checagem = False # variável de checagem
    for linha in arquivo:
        # o método split() quebra a linha em várias strings e as armazena em uma lista 
        dados = linha.split() # lista com as strings da linha
        # percorendo a lista em busca do dado
        for i in range(len(dados)):
            if dado == dados[i]:
                checagem = True
    arquivo.close() # fechando aquivo
    return checagem
        

# insere os dados em um banco de notas específico, que recebe como parâmetro a
# referência para o arquivo   
def insereDados(endereco_arquivo):
    # esse trecho checa se o arquivo onde serão inseridas as notas existe
    if checaArquivo(endereco_arquivo):
        arquivo = open(endereco_arquivo, 'r')
        print('\n')
        matricula = input('Entre com a matrícula do aluno: ')
        print('\n')
        while checaDados(endereco_arquivo, matricula):
                print('O número de matrícula digitado já consta no banco de notas, escolha outro!')
                print('\n')
                matricula = input('Entre com a matrícula do aluno: ')
        arquivo.close()
        # adicionando os dados no arquivo
        arquivo = open(endereco_arquivo, 'a')
        print('\n')
        dado = input('Entre com o nome do aluno: ')
        dado += '|' + matricula
        for i in range(3): # como são apenas 3 notas, então "range(3)"
            checagem = False
            while checagem == False:
                # desconsidera o erro se for digitado valor diferente de números
                try:
                    print('\n')
                    nota = float(input(f'Entre com a nota {i+1} :'))
                except:
                    print('\n')
                    print('Valor digitado não é um número!')
                else:
                    if nota < 0 or nota > 10:
                        print('\n')
                        print('Digite um número entre 0 e 10!')
                    else:
                        checagem = True
                        dado += '|' + str(nota) # transforma nota em uma string
        arquivo.write(dado + '\n')
        arquivo.close()
    else:
        print('\n')
        print('O arquivo procurado não existe!')
        print('\n')

# deletar um banco de notas específico, recebendo como parâmetro uma referência
# para o banco de notas em questão
def deletarBancoDeNotas(endereco_arquivo):
    if checaArquivo(endereco_arquivo):
        import os # importa o módulo os
        os.remove(endereco_arquivo) # remove o aquivo escolhido
        print('\n')
        print('O arquivo foi deletado!')
        print('\n')
        arquivo = open('registro.txt', 'r')
        conteudo = []
        # percore o arquivo e transfere o conteudo para uma lista onde cada elemento da lista
        # correpsonde ao informação de cada linha do arquivo "registro.txt"
        # a estrutura condicional já exclui o dado do arquivo que foi deletado da lista "conteudo"
        for linha in arquivo:
            if linha.strip() != endereco_arquivo: # o método "strip()" retira o "\n" do final da linha
                conteudo.append(linha.strip())
        arquivo.close()
        os.remove('registro.txt') # remove o aquivo "registro.txt"
        # este bloco de código confere se a a lista gerada com o conteúdo do arquivo "registro.txt"
        # não é uma lista vazia, se a lista não é vazia o arquivo "registro.txt" é criado novamente
        # e preenchido com o novo conteúdo
        if len(conteudo) != 0:
            arquivo = open('registro.txt', 'a')
            for i in range(len(conteudo)):
                arquivo.write(conteudo[i] + '\n')
            arquivo.close()
    else:
        print('\n')
        print('O arquivo procurado não existe!')
        print('\n')
        
# calcula a média para cada aluno contido no arquivo selecionado, recebendo como parâmetros
# a referência para o arquivo que será utilizado no cálculo (que é uma string), e os pesos para
# as provas p1, p2 e p3 (que são floats)
def calculaMedia(endereco_arquivo, p1, p2, p3):
    if checaArquivo(endereco_arquivo):
        arquivo = open(endereco_arquivo, 'r')
        if arquivo.read() == '':
            print('\n')
            print('O arquivo não contem informações a serem apresentadas!')
            print('\n')
            arquivo.close()
        else:
            print('\n')
            arquivo = open(endereco_arquivo, 'r')
            resultado = ''
            alunos_aprovados = 0
            alunos_reprovados = 0
            alunos_IFA = 0
            for linha in arquivo:
                # o método split('|') retorna o conteúdo da linha em uma lista
                # a separador que indica quando a separação deve ocorrer é o '|'
                dados = linha.split('|') 
                resultado += dados[0] + ' ' + dados[1] + ' '
                media = p1*float(dados[2]) + p2*float(dados[3]) + p3*float(dados[4])
                # aqui o método "format" formata a "media" como uma string com dois digitos após a virgula ({:.2f})
                resultado += 'Média = {:.2f} '.format(media)
                if media < 6 and media > 4: 
                    resultado += 'IFA' + '\n'
                    alunos_IFA += 1
                elif media >= 6:
                    resultado += 'Aprovado' + '\n'
                    alunos_aprovados += 1
                else:
                    resultado += 'Reprovado' + '\n'
                    alunos_reprovados += 1
            print(resultado)
            print(f'{alunos_aprovados} aluno(s) foram aprovados.')
            print(f'{alunos_reprovados} aluno(s) foram reprovados.')
            print(f'{alunos_IFA} aluno(s) estão de IFA.')
    else:
        print('\n')
        print('O arquivo procurado não existe!')
        print('\n')
              
       
######################################################################
# inicio da execução do programa

main()
    
