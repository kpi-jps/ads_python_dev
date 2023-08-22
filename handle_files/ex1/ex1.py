'''
1- O IBOP deseja realizar uma pesquisa em nível nacional e, para tanto,
precisará de um programa que o auxilie no armazenamento das respostas
fornecidas por cada pessoa entrevistada, para que possa obter algumas
estatísticas. Considere que cada entrevistado deverá responder ao seguinte
questionário:
Sexo: ( ) masculino ( ) feminino Idade: ____ anos
Fumante: ( ) sim ( ) não
Escolaridade: ( ) fundamental ( ) médio ( ) superior
Faça um programa que solicite os dados de cada entrevistado e armazene-os em
um arquivo chamado pesquisa.txt, onde cada linha do arquivo deverá
armazenar as respostas de apenas uma pessoa entrevistada, conforme no
exemplo a seguir. A quantidade de entrevistados não será definida a priori. O
usuário deverá informar ao programa quando desejar encerrar as entrevistas.
Arquivo pesquisa.txt:
feminino 28 não superior
feminino 23 sim superior
masculino 24 sim médio
masculino 17 não médio
feminino 14 não fundamental
...
Após encerrar as entrevistas, o programa deverá abrir o arquivo criado
(pesquisa.txt), calcular e apresentar as seguintes estatísticas sobre os dados
fornecidos pelos entrevistados:
- Qual é o percentual de fumantes em relação ao número total de pessoas
entrevistadas?
- Qual é o percentual de homens não fumantes abaixo de 40 anos, em
relação ao número total de homens entrevistados? 
- Qual é o percentual de mulheres fumantes acima de 40 anos em relação
ao número total de mulheres entrevistadas?

'''

######################################################################
# definindo a função principal

def main():
    print('#########################################################')
    print('#################### PESQUISA IBOP ######################')
    print('#########################################################')
    print('\n')
    questionario()
    

######################################################################
# definindo a função secundárias

# permite que o questionáario seja respondido quantas vezes o usuário desejar
def novamente():
    print('\n')
    responder = input('Gostaria de responder o questionário novamente? ([1] = Sim; [2] = Não) ') 
    print('\n')
    while validarEscolha(responder, 2) == False:
        print('Valor inválido digitado!')
        print('\n')
        responder = input('Gostaria de responder o questionário novamente? ([1] = Sim; [2] = Não) ') 
    if responder == '1':
        questionario()
    elif responder == '2':
        estatisticas()
        
# checa a existência do arquivo
# o parâmetro "arquivo" que corresponde a uma string contendo o nome
# do arquivo contendo todo o caminho e a extensão
def checaArquivo(arquivo):
    # O módulo "os" fornece uma maneira simples de usar funcionalidades
    # que são dependentes de sistema operacional
    import os
    # "os.path.exists(arquivo)" checa se "arquivo" existe. Se
    # sim, a expressão retorna "True" e se não "False"
    if os.path.exists(arquivo):  
        return True
    else:
        return False

# valida a entrada de escolhas
# o parâmetro "entrada" é o dado a ser validado e deve ser uma string
# o prâmetro "limite" é um inteiro equivalente ao maior número
# correspondete as opções disponíveis no menu
def validarEscolha(entrada, limite):
    if entrada.isdigit():
        num = int(entrada)
        if num > 0 and num <= limite:
            return True
        else:
            return False
    else:
        return False 

# cria questionário e salva respostas
def questionario():
    if checaArquivo('pesquisa.txt'):
        arquivo = open('pesquisa.txt', 'a')
    else:
        arquivo = open('pesquisa.txt', 'a')
    conteudo_arquivo = ''
    print('Para participar da pesquisa responda as seguintes perguntas.')
    print('\n')
    entrada = input('Pergunta 1 - Sexo ([1] = feminino; [2] = masculino): ')
    print('\n')
    while validarEscolha(entrada, 2) == False:
        print('Valor inválido digitado!')
        print('\n')
        entrada = input('Pergunta 1 - Sexo ([1] = feminino; [2] = masculino): ')
        print('\n')
    if entrada == '1':
        entrada = 'feminino'
    elif entrada == '2':
        entrada = 'masculino'
    conteudo_arquivo = conteudo_arquivo + entrada
    entrada = input('Pergunta 2 - Idade em anos (apenas números são permitidos): ')
    print('\n')
    while entrada.isdigit() == False:
        print('Valor inválido digitado!')
        print('\n')
        entrada = input('Pergunta 2 - Idade em anos (apenas números são permitidos): ')
        print('\n')
    conteudo_arquivo = conteudo_arquivo + ' ' + entrada
    entrada = input('Pergunta 3 - Fumante ([1] = sim; [2] = não): ')
    print('\n')
    while validarEscolha(entrada, 2) == False:
        print('Valor inválido digitado!')
        print('\n')
        entrada = input('Pergunta 3 - Fumante ([1] = sim; [2] = não): ')
        print('\n')
    if entrada == '1':
        entrada = 'sim'
    elif entrada == '2':
        entrada = 'não'
    conteudo_arquivo = conteudo_arquivo + ' ' + entrada
    entrada = input('Pergunta 4 - Escolaridade ([1] = fundamental; [2] = médio; [3] = superior): ')
    while validarEscolha(entrada, 3) == False:
        print('Valor inválido digitado!')
        print('\n')
        entrada = input('Pergunta 4 - Escolaridade ([1] = fundamental; [2] = médio; [3] = superior): ')
        print('\n')
    if entrada == '1':
        entrada = 'fundamental'
    elif entrada == '2':
        entrada = 'médio'
    elif entrada == '3':
        entrada = 'superior'
    conteudo_arquivo = conteudo_arquivo + ' ' + entrada + '\n' # pula a linha para a próxima inserção de dados
    arquivo.write(conteudo_arquivo) # adiciona "conteudo_arquivo" ao final do arquivo
    arquivo.close() # fecha o arquivo
    novamente() # executa a função que permite responder o questionário novamente

def estatisticas():
    arquivo = open('pesquisa.txt', 'r')
    dados = [] # armazena todos os dados
    linha = arquivo.readline()
    # aqui poderia usar apenas "while linha:", pois o método "split()"
    # retrona a variável linha como uma string vazia ""
    while linha != '': 
        # "dado" armazena cada linha do arquivo na forma de uma lista
        dado = linha.split() 
        dados.append(dado)
        linha = arquivo.readline()
    arquivo.close()
    
    print ('Percentual de fumantes em relação ao número total de pessoas entrevistadas:')
    string_resultado = '{:.1f} %'
    print (string_resultado.format(estatistica1(dados)))
    print ('\n')
    print ('Percentual de homens não fumantes abaixo de 40 anos, em relação ao número total de homens entrevistados:')
    string_resultado = '{:.1f} %'
    print (string_resultado.format(estatistica2(dados)))
    print ('\n')
    print ('Percentual de mulheres fumantes acima de 40 anos em relação ao número total de mulheres entrevistadas:')
    string_resultado = '{:.1f} %'
    print (string_resultado.format(estatistica3(dados)))
    print ('\n')
    print ('\n')

    
# calcula e retorna o percentual de fumantes no universo de entrevistados
# o parâmetro "lista_dados" corresponde a uma lista obtida com a leitura de um arquivo
def estatistica1(lista_dados):
    num_fumantes = 0
    for i in range(len(lista_dados)):
        # Fumante é a pergunta 3 e suas repostas tem index 2 nas listas correspondetes a cada linha lida no arquivo
        if lista_dados[i][2] == 'sim': 
            num_fumantes += 1
    # o número total de entrevistados é dado pelo tamanho da lista "len(lista_dados)"
    return (num_fumantes / len(lista_dados))*100

#  calcula e retorna o percentual de homens não fumantes, com idade inferior a 40 anos, entre os homens entrevistados 
# o parâmetro "lista_dados" corresponde a uma lista obtida com a leitura de um arquivo
def estatistica2(lista_dados):
    total_homens = 0
    # calculando a quantidade de homens no universo entrevistado
    for i in range(len(lista_dados)):
        # Sexo é a pergunta 1 e sua resposta tem index 0 nas listas correspondetes a cada linha lida no arquivo
        if lista_dados[i][0] == 'masculino':
            total_homens += 1
    if total_homens != 0:
        homens_nao_fumantes = 0 # com idade inferior a 40 anos
        for i in range(len(lista_dados)):
            # Sexo é a pergunta 1 e sua resposta tem index 0 nas listas correspondetes a cada linha lida no arquivo
            # Idade é a pergunta 2 e sua resposta tem index 1 nas listas correspondetes a cada linha lida no arquivo
            # Fumante é a pergunta 3 e suas repostas tem index 2 nas listas correspondetes a cada linha lida no arquivo
            if lista_dados[i][0] == 'masculino' and int(lista_dados[i][1]) < 40 and lista_dados[i][2] == 'não':
                homens_nao_fumantes += 1
        return (homens_nao_fumantes / total_homens)*100
    # se não existir homens no universo pesquisado a função retorna 0
    else:
        return 0

#  calcula e retorna o percentual de mulheres fumantes, com idade superior a 40 anos, entre as mulheres evistadas 
# o parâmetro "lista_dados" corresponde a uma lista obtida com a leitura de um arquivo
def estatistica3(lista_dados):
    total_mulheres = 0
    # calculando a quantidade de mulheres no universo entrevistado
    for i in range(len(lista_dados)):
        # Sexo é a pergunta 1 e sua resposta tem index 0 nas listas correspondetes a cada linha lida no arquivo
        if lista_dados[i][0] == 'feminino':
            total_mulheres += 1
    if total_mulheres != 0:
        mulheres_fumantes = 0 # com idade superior a 40 anos
        for i in range(len(lista_dados)):
            # Sexo é a pergunta 1 e sua resposta tem index 0 nas listas correspondetes a cada linha lida no arquivo
            # Idade é a pergunta 2 e sua resposta tem index 1 nas listas correspondetes a cada linha lida no arquivo
            # Fumante é a pergunta 3 e suas repostas tem index 2 nas listas correspondetes a cada linha lidas no arquivo
            if lista_dados[i][0] == 'feminino' and int(lista_dados[i][1]) > 40 and lista_dados[i][2] == 'sim':
                mulheres_fumantes += 1
        return (mulheres_fumantes / total_mulheres)*100
    # se não existir mulheres no universo pesquisado a função retorna 0
    else:
        return 0
       
######################################################################
# inicio da execução do programa

main()
    
