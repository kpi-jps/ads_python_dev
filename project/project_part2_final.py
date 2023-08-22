''' 
Projeto AP1S1
Tema 1: Hospital
Alunos: João Pedro da Silva e Thiane Deprá Saravalle
Etapa 2
'''

##########################################################################
################### Definindo a função principal #########################
##########################################################################
def main():
    # definindo referências para os arquivos usados como banco de dados
    arq_medicos = 'medicos.txt'
    arq_pacientes = 'pacientes.txt'
    arq_consultas = 'consultas.txt'

    # estrutura de dados nos arquivos:
    
    # - arquivo médicos
    # CRM; nome do médico; data de nascimento; sexo; especialidade; universidade que se formou; lista de email; lista de telefone \n
    # lista de e-mail: email 1| email 2|...email n
    # lista de telefone: telefone 1| telefone 2|...telefone n

    # - arquivo pacientes
    # CPF, nome do paciente; data de nascimento; sexo; plano de saúde; lista de email; lista de telefone \n
    # lista de e-mail: email 1| email 2|...email n
    # lista de telefone: telefone 1| telefone 2|...telefone n

    # - arquivo consultas
    # chave da consulta; Diagnótico:strig; Medicamentos:string \n
    # a chave da consulta será uma string contendo o "CRM, CPF, Data, Hora"

    # após carregados dos arquivos os dados serão estruturados da seguinte maneira:
    # dados = [
    # [medicos](índice 0), [pacientes] (ínidice 1), [consultas](ínidice 2)
    # ]
    
    # medicos = [[medico1], [medico2], ... , [medicoN]]
    
    # pacientes = [[paciente1], [paciente2], ..., [pacienteN]]

    #consultas = {{'chave1':consulta1}, {'chave1':consulta2}, ..., {'chaveN':consultaN}}
    # aqui a chave será uma string contendo o "CRM, CPF, Data, Hora"
    
    # medicoN = [
    # CRM (chave), Nome, Data de Nascimento, Sexo, Especialidade, Universidade em que
    # se formou, [E-mails] (uma lista com mais de um e-mail), [Telefones] (uma lista
    # com mais de um telefone)
    # ]
    
    # pacienteN = [
    # CPF(chave), Nome, Data de Nascimento, Sexo, Plano de saúde,
    # [E-mails] (uma lista com mais de um e-mail), [Telefones] (uma lista
    # com mais de um telefone)
    # ]

    #consulaN = {"chaveDiagnostico":"Diagnostico", "chaveMedicamentos":"Medicamentos"}
    # aqui as chaves "chaveDiagnostico" e "chaveMedicamentos" serão respectivamente as strings "Diagnostico" e "Medicamentos"
    
    dados = []
    medicos = []
    pacientes = []
    consultas = {}
    
    # carregando dados dos médicos e dos pacientes.
    # a ordem com que os dados são carregados é importante e não pode ser invertida,
    # pois os indíces dos bancos de dados de médicos e pacientes são usados por outras funções.
    # na ordem escrita abaixo, os dados dos médicos tem índice 0 e o de
    # pacientes tem índice 1, na lista "dados"
    # consultas tem índice 2, na lista "dados"
    
    carregaDoArquivo(arq_medicos, medicos) # carega os dados a partir do arquivo de médicos e popula a lista "medicos"
    dados.append(medicos) # adiciona a lista "medicos" a lista de total de dados "dados"

    carregaDoArquivo(arq_pacientes, pacientes) # carega os dados a partir do arquivo de pacientes e popula a lista "pacientes"
    dados.append(pacientes) # adiciona a lista "pacientes" a lista de total de dados "dados"

    carregaDoArquivo2(arq_consultas, consultas) # carrega os dados a partir do arquivo de consultas e popula o dicionário "consultas"
    dados.append(consultas)
 
    criaCabecalho() # cria o cabeçalho
    menu(dados) # carrega o menu  
    
##########################################################################
############# Definindo as funções secundárias gerais ####################
##########################################################################
    
#====================================================================
# - checa a existência do arquivo
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
    
#====================================================================
# - cria o cabeçalho da aplicação
def criaCabecalho():
    print('\n###################################################')
    print('###### Aplicação de gerenciamento Hospitalar ######')
    print('###################################################')
    
#====================================================================
# - cria o menu principal
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def menu(dados):
    print('\n')
    print('---------------------------------------------------')
    print('---------------- Menu de opções -------------------')
    print('---------------------------------------------------')
    print('\n')
    print(' - [1] - Submenu de Médicos')
    print(' - [2] - Submenu de Pacientes')
    print(' - [3] - Submenu de Consultas')
    print(' - [4] - Submenu de Relatórios')
    print('\n')
    print('---------------------------------------------------')
    print('\n')
    opcao = input('Entre com o valor numérico da opção desejada: ')
    while validarEscolha(opcao, 4) == False:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('O valor digitado não corresponde a um valor válido!')
        print('-----------------------------------------------------')
        print('\n')
        opcao = input('Entre com o valor numérico da opção desejada: ')
        print('\n')
    submenu(opcao, dados)

#====================================================================
# - cria o submenu
# - o parâmetro "cod_submenu" precisa ser uma string e
# corresponde ao valor númerico da opção selecionada no menu
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def submenu(cod_submenu, dados):
    if int(cod_submenu) <= 3:
        if cod_submenu == '1':
            nome_do_submenu = 'Médicos'
            index_dados = 0
        elif cod_submenu == '2':
            nome_do_submenu = 'Pacientes'
            index_dados = 1
        elif cod_submenu == '3':
            nome_do_submenu = 'Consultas'
            index_dados = 2    
        print('\n')
        print('---------------------------------------------------')
        print(f'Submenu de {nome_do_submenu}')
        print('---------------------------------------------------')
        print('\n')
        print(' - [1] - Listar todos')
        print(' - [2] - Listar com especificação')
        print(' - [3] - Incluir')
        print(' - [4] - Alterar')
        print(' - [5] - Excluir')
        print(' - [6] - Voltar')
        print('\n')
        print('---------------------------------------------------')
        opcao = input('Entre com o valor numérico da opção desejada: ')
        while validarEscolha(opcao, 6) == False:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('O valor digitado não corresponde a um valor válido!')
            print('-----------------------------------------------------')
            print('\n')
            opcao = input('Entre com o valor numérico da opção desejada: ')
            print('\n')
        # oções de submenu para menu de médicos e pacientes
        if index_dados == 0 or index_dados == 1:
            if opcao == '1':
                listaTodos(index_dados, dados)
            elif opcao == '2':
                listaEspecifico(index_dados, dados)
            elif opcao == '3':
                incluirItem(index_dados, dados)
            elif opcao == '4':
                alterarItem(index_dados, dados)
            elif opcao == '5':
                excluirItem(index_dados, dados) 
            elif opcao == '6':
                menu(dados)
        # oções de submenu para menu de consultas
        elif index_dados == 2:
            if opcao == '1':
                listarConsultas(dados)
            elif opcao == '2':
                listarConsultaEspecifica(dados)
            elif opcao == '3':
                incluirConsulta(dados)
            elif opcao == '4':
                alterarConsulta(dados)
            elif opcao == '5':
                deletaConsulta(dados)
            elif opcao == '6':
                menu(dados)
    else:
        nome_do_submenu = 'Relatórios'
        print('\n')
        print('---------------------------------------------------')
        print(f'Submenu de {nome_do_submenu}')
        print('---------------------------------------------------')
        print('\n')
        print(' - [1] - Informar médicos por especialidade')
        print(' - [2] - Informar pacientes por idade')
        print(' - [3] - Informações sobre consultas ')
        print(' - [4] - Voltar')
        print('\n')
        print('---------------------------------------------------')
        opcao = input('Entre com o valor numérico da opção desejada: ')
        while validarEscolha(opcao, 6) == False:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('O valor digitado não corresponde a um valor válido!')
            print('-----------------------------------------------------')
            print('\n')
            opcao = input('Entre com o valor numérico da opção desejada: ')
            print('\n')
        if opcao == '1':
            medicosPorEspecialidade(dados)
            submenu('4', dados)
        elif opcao == '2':
            pacientesPorIdades(dados)
            submenu('4', dados)
        elif opcao == '3':
            consultasPorData(dados)
            submenu('4', dados)
        elif opcao == '4':
            menu(dados)
            
#====================================================================
# - retorma para o submenu
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def retornaSubmenu(index_banco_de_dados, dados):
    comando = input('Digite 1 para voltar ao submenu: ')
    while validarEscolha(comando, 1) == False:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('O valor digitado não corresponde ao valor requerido!')
        print('-----------------------------------------------------')
        print('\n')
        comando = input('Digite 1 para voltar ao submenu:')
        print('\n')
    # esta variável precisa ser uma string, a função "submenu" requer este tipo de variável
    opcao = str(index_banco_de_dados + 1)
    submenu(opcao, dados)
        
#====================================================================    
# - valida a entrada das escolhas dos menus e submenus
# - o parâmetro "entrada" é o dado a ser validado e deve ser uma string
# - o prâmetro "limite" é um inteiro equivalente ao maior número
# correspondete as opções disponíveis no menu e submenu
def validarEscolha(entrada, limite):
    if entrada.isdigit():
        num = int(entrada)
        if num > 0 and num <= limite:
            return True
        else:
            return False
    else:
        return False

#====================================================================     
# valida a entrada da data fornecida pelo usuário como dia/mes/ano, onde dia
# tem dois digitos, mês tem dois digitos e ano quatro digitos
def validaData(entrada):
    check = False
    contador = 0
    for caracter in entrada:
        if caracter == '/':
            contador += 1
    if contador == 2:
        # exclui o caracter '/' e agrupa os caracteres restantes em uma lista
        caracteres = entrada.split('/')
        string = ''
        for i in range(len(caracteres)):
            string += caracteres[i]
        # checando se os caracteres são apenas digitos, se a string tem 8 carcteres (ddmmaaaa) e se o 0 < dia <= 31 e se 0 < mês <= 12 
        if string.isdigit() and len(string) == 8 and int(caracteres[0]) > 0 and int(caracteres[0]) <= 31 and int(caracteres[1]) > 0 and int(caracteres[1]) <= 12:
            check = True
    return check

#==================================================================== 
# valida a entrada de horário no formato "hh:mm", o parâmetro "entrada" precisa ser uma string
def validaHorario(entrada):
    check = False
    # verifica se ":" existe na string "entrada"
    if ':' in entrada:
        caracteres = entrada.split(':')
        string = ''
        print(string)
        for i in range(len(caracteres)):
            string += caracteres[i]
        # checando se os caracteres são apenas digitos 
        if string.isdigit():
            # checando se os minutos da hora assumem apenas os valores entre  "00" e "59"
            if int(caracteres[1]) >= 0 and int(caracteres[1]) <= 59:
                # definindo hora entre as 0 e 23
                if int(caracteres[0])>= 0 and int(caracteres[0]) <= 23:
                    check = True
    return check
#==================================================================== 
# busca por uma chave em um dicionário e retorna "True" se ela existe ou "False" se não
# recebe como parâmetros a chave a ser buscada e o dicionário onde será feita a busca
def buscaChave(chave, dicionario):
    if chave in dicionario:
        return True
    else:
        return False

# checa se um ano é ou não bissexto, retornando "True" se sim,
# e "False" se não.
# recebe como parâmetro o ano na forma de um inteiro
def checaAnoBissexto(ano):
    # checa se o ano é divisível por 4
    if ano % 4 == 0:
        # se for divisível por 4 checa se é divisível por 100 
        if ano % 100 == 0:
            # se for divisível por 4 e 100, checa se é divisível por 400,
            # se sim é ano bissexto e retorna "True"
            if ano % 400 == 0:
                return True
            # se não for divisível por 400 não é bissexto e retorna "False"
            else:
                return False
        # se não for divisível por 100 é bissexto e retona "True" 
        else:
            return True
    # senão for divisível por 4 não é bissexto e retona "False"
    else:
        return False
    
#====================================================================    
# retorna a quantidade de dias que um mês possui, na forma de um inteiro,
# usando como parâmetros o ano e o mês também na forma de  inteiros
def quantidadeDiasMes(ano, mes):
    # para os meses de janeiro (1), março (3), maio (5), julho (7), agosto (8),
    # outubro (10) e dezembro (12) retorna 31 dias
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31 # retorn 31 dias
    # para o mes de fevereiro (2) checa se o ano é bissexto, se sim retorna 29 dias
    # e se não retorna 28 dias
    elif mes == 2:
        if checaAnoBissexto(ano):
            return 29 # retorna 29 dias
        else:
            return 28 # retorna 28 dias
    # para os demais meses, abril (4), junho (6), setembo (8) e novembro (11), retorna 30 dias.
    else:
        return 30 # retorna 30 dias

#==================================================================== 
# calcula uma data no passado, usando como base uma data de referência, no presente ou futuro, e a
# quantidade de dias anteriores a data de referência
# os parâmetros o "dia", "mes", "ano" e "num_dias" devem ser inseridos como strings
def calculaDataPassada(dia,mes,ano,num_dias):
    # convertendo os parâmetros para inteiros
    d = int(dia)
    m = int(mes)
    a = int(ano)
    nd = int(num_dias)
    # variável de controle para o "loop" while
    check = False
    while check == False:
        # testa se a diferença entre o dia da data informada e o número de dias anterios
        # é negativo, se verdadeiro significa que o mês informada deve ser decrementado de 1
        if d - nd < 0:
            # descobrindo se o mês informado é janeiro, se sim o ano deve ser decrementado de 1
            # e o novo valor para mês deve ser igual a 12, que corresponde a dezembro
            if m == 1: 
                a = a - 1
                m = 12
            # se o mês informado não é 1, ou seja janeiro, o mês é decrementado em 1
            else:
                m = m-1
            # calculando um novo valor para nd, que será utilizado na próxima interação
            # do "loop" while
            nd = (d - nd)*(-1)
            # determinando o novo valor para o dia que será utilizado na próxima interação
            # do "loop" while
            d = quantidadeDiasMes(a, m)
        # se a diferença entre o dia da data informada e o número de dias anterios é 0,
        # se verdadeiro significa que o mês informada também deve ser decrementado de 1 
        elif d - nd == 0:
            # novamente checa se o mês informado é janeiro e se sim atualiza o valor do ano
            if m-1 == 0:
                a = a - 1
                m = 12
            # se o mês não for janeiro apenas decrementa o valor do mês em 1 e
            # atualiza o valor do dia 
            else:
                m = m-1
                d = quantidadeDiasMes(a, m)
            # uma das condições de parada do "loop" while é quando d - nd == 0, sendo assim,
            # é necessário atualizar a variável "check"
            check = True
        # d - nd > 0 também é condição de parada para "loop" while, sendo assim, atualiza-se
        # a variável dia e a variável "check"
        else:
            d = d - nd
            check = True
    # construindo data a ser retornada na forma de uma string (dd/mm/aaaa)
    # se dia for um valor menor que 10 adiciona-se um zero antes ao valor do dia
    if d < 10:
        data = '0' + str(d) + '/'
    else:
        data = str(d) + '/'
    # se mês for um valor menor que 10 adiciona-se um zero antes ao valor do mês
    if m < 10:
        data += '0' + str(m) + '/'
    else:
        data += str(m) + '/'
    data += str(a)
    return data


##########################################################################
## Definindo as funções secundárias implementadas para dados em listas ###
##########################################################################
# funções para os submenus de Pacientes e médicos

#====================================================================
# carrega os dados a partir de um arquivo específico e popula uma lista de dados
# específica com os dados oriundos do arquivo
# recebe como parâmetros o nome do arquivo que será utilizado e a lista que será
# populada
def carregaDoArquivo(nome_arquivo,lista_dados_especificos):
    if checaArquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        for linha in arquivo:
            linha = linha.strip() # o método ".strip()" retira o "\n" do conteúdo da linha do arquivo
            conteudo = linha.split(';') # ; é o separador usado nos arquivos
            lista_dados = []
            for i in range(len(conteudo)):
                # condicional para casos com mais de um e-mail ou telefone salvo
                if '|' in conteudo[i]:
                    lista_dados.append(conteudo[i].split('|')) # | é o separador usado para a lista de emails e telefones 
                # condicional para casos com apenas um e-mail ou telefone salvo
                # este bloco de código cria uma lista e mantem os dados na memória com estrutura
                # que permite que mais e-mails ou telefones possam ser adicionados ao cadastra
                # usando a função alterar
                elif i == len(conteudo) - 2 or i == len(conteudo) - 1:
                    lista = []
                    lista.append(conteudo[i])
                    lista_dados.append(lista)
                else:
                    lista_dados.append(conteudo[i])
            lista_dados_especificos.append(lista_dados)
        arquivo.close()
    else:
        arquivo = open(nome_arquivo, 'w')
        arquivo.close()
        
#====================================================================
# popula arquivos com informações, recebendo como parâmetro uma lista
# contendo as informações que serão adicionadas e a referência ao
# arquivo que será utilizado
def adicionaAoArquivo(lista, nome_arquivo):
    arquivo = open(nome_arquivo, 'a')
    linha = ''
    for i in range(len(lista)):
        # testa se a variável da lista "lista" é também uma lista
        # isto é para as listas de telefones e emails
        if type (lista[i]) == type (lista): 
            for j in range(len(lista[i])):
                if j == len(lista[i]) - 1:
                    linha += lista[i][j]
                else:
                    linha += lista[i][j] + '|'
            if i == len(lista) - 2:
                linha +=  ';'
            else:            
                linha += '\n'
        else:
            if i == len(lista)-1:
                linha += lista[i] + '\n' 
            else:
                linha += lista[i] + ';'
    arquivo.write(linha)
    arquivo.close()           

#====================================================================
# adiciona informações a um arquivo específico quando a função "incluir",
# contida nos menus, é solicitada
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def adicionarNoArquivo(index_banco_de_dados, dados):
    if index_banco_de_dados == 0:
        nome_arquivo = 'medicos.txt'
    elif index_banco_de_dados == 1:
        nome_arquivo = 'pacientes.txt'
    lista_dados = dados[index_banco_de_dados]
    # referênciando a ultima lista de dados da lista "medicos" ou "pacientes"
    lista = lista_dados[len(lista_dados)-1]
    adicionaAoArquivo(lista, nome_arquivo) # adiciona a informação ao arquivo

#====================================================================
# adiciona informações a um arquivo específico quando a função quando informações
# são alteradas ou deletadas
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def atualizaArquivo(index_banco_de_dados, dados):
    if index_banco_de_dados == 0:
        nome_arquivo = 'medicos.txt'
    elif index_banco_de_dados == 1:
        nome_arquivo = 'pacientes.txt'
    lista_dados = dados[index_banco_de_dados]
    # recria o arquivo sendo manipulado em branco
    arquivo = open(nome_arquivo, 'w')
    arquivo.close()
    for i in range(len(lista_dados)):
        adicionaAoArquivo(lista_dados[i], nome_arquivo)
 
#====================================================================
# - checa se o banco de dados acessado esta vazio
# e escolhe os titulos dos itens do bancos de dados a serem listados
# ou alteradados
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
# a função retorna um booleano indicando se o banco de dados está vazio
# ou não (True = vazio; False = não vazio)
def checaDados(index_banco_de_dados, dados):
    if  len(dados[index_banco_de_dados]) == 0:
        return True
    else:
        return False
    
#====================================================================
# - define os titulos dos dados a serem listados
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - retorna os titulos na forma de uma lista 
def titulosDados(index_banco_de_dados):
    if index_banco_de_dados == 0: # identifica o banco de dados de médicos
        titulos = ['CRM',
                   'Nome',
                   'Nascimento',
                   'Sexo',
                   'Especialidade',
                   'Formado (a) na Universidade',
                   'E-mail(s)',
                   'Telefone(s)'
                    ]
    elif index_banco_de_dados == 1: # identifica o banco de dados de pacientes
        titulos = ['CPF',
                   'Nome',
                   'Nascimento',
                   'Sexo',
                   'Plano de saúde',
                   'E-mail(s)',
                   'Telefone(s)'
                    ]
    return titulos

#====================================================================
# - imprime itens do banco de dados
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "titulo" corresponde aos titulos dos dados
# - os parametros i e j são indexes das listas contidas nos bancos de dados
def imprimeItens(index_banco_de_dados, dados, titulos, i, j):
    # identifica se a váriavel percorrida pela estrutura de repetição
    # é do tipo lista 
    if type(dados[index_banco_de_dados][i][j]) == type(dados[index_banco_de_dados][i]):
        print(f'{titulos[j]}: ')
        for k in range(len(dados[index_banco_de_dados][i][j])):
            print(dados[index_banco_de_dados][i][j][k])
    else:
        print(f'{titulos[j]}: {dados[index_banco_de_dados][i][j]}')

#====================================================================
# - busca por item no banco da dados e retorna um booleano (True se o
# o item foi encontrado e False se o item não existe na lista)
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
# - entrada corresponde a item a ser buscado, esta variável deve ser uma string
def buscaItem(index_banco_de_dados, dados, entrada):
    check = False
    for i in range(len(dados[index_banco_de_dados])):
        # aqui o index é 0, pois o elemento chave é o primeiro da
        # lista "paciente" ou "medico"
        if entrada == dados[index_banco_de_dados][i][0]:
           check = True
    return check
        
#====================================================================        
# - busca por item no banco da dados e seu índice
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
# - entrada corresponde a item a ser buscado, esta variável deve ser uma string        
def retornaIndice(index_banco_de_dados, dados, entrada):
    for i in range(len(dados[index_banco_de_dados])):
        # aqui o index é 0, pois o elemento chave é o primeiro da
        # lista "paciente" ou "medico"
        if entrada == dados[index_banco_de_dados][i][0]:
            return i
       

#====================================================================    
# lista todos os elementos do banco de dados selecionado
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def listaTodos(index_banco_de_dados, dados):
    # verifica se a lista contendo os dados esta vazia
    if  checaDados(index_banco_de_dados, dados):
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')
        retornaSubmenu(index_banco_de_dados, dados)
    else:
        print('\n')
        print('-----------------------------------------------------')
        print('Listando Iten(s)')
        print('-----------------------------------------------------')
        print('\n')
        titulos = titulosDados(index_banco_de_dados)
        for i in range(len(dados[index_banco_de_dados])):
            for j in range(len(dados[index_banco_de_dados][i])):
                imprimeItens(index_banco_de_dados, dados, titulos, i, j)
            print('-----------------------------------------------------')
    print('\n')
    retornaSubmenu(index_banco_de_dados, dados)

    
#====================================================================        
# - lista item específico e retorna o atributo chave do item buscado se o mesmo
# for encontrado ou retorno uma string vazia se o mesmo não for encontrado
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def listaItem(index_banco_de_dados, dados):
    # verifica se a lista contendo os dados esta vazia
    if  checaDados(index_banco_de_dados, dados):
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')
        return "" # string vazia
    else:
        print('\n')
        print('-----------------------------------------------------')
        print('Listando Iten(s)')
        print('-----------------------------------------------------')
        print('\n')
        titulos = titulosDados(index_banco_de_dados)
        if index_banco_de_dados == 0:
            chave = 'CRM'
            objeto = 'médico'
        elif index_banco_de_dados == 1:
            chave = 'CPF'
            objeto = 'paciente'
        busca = input(f'Digite o {chave} (apenas digitos) para buscar por um {objeto}: ')
        while busca.isdigit() == False:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('Digite apenas números para realizar a busca!')
            print('-----------------------------------------------------')
            print('\n')
            busca = input(f'Digite o {chave} (apenas digitos) para buscar por um {objeto}: ')
            print('\n')
        if buscaItem(index_banco_de_dados, dados, busca):
            print('\n')
            indice = retornaIndice (index_banco_de_dados, dados, busca)
            for j in range(len(dados[index_banco_de_dados][indice])):
                imprimeItens(index_banco_de_dados, dados, titulos, indice, j)
            print('-----------------------------------------------------')
            print('\n')
            return busca
        else:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('Item não encontrado!')
            print('-----------------------------------------------------')
            print('\n')
            return ""
        
#====================================================================        
# - dispara a listagem de item específico
def listaEspecifico(index_banco_de_dados, dados):
    listaItem(index_banco_de_dados, dados)
    retornaSubmenu(index_banco_de_dados, dados)
    
#====================================================================    
# - inclui item não existente ao banco de dados
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def incluirItem(index_banco_de_dados, dados):
    titulos = titulosDados(index_banco_de_dados)
    if index_banco_de_dados == 0:
        objeto = 'médico'
    elif index_banco_de_dados == 1:
        objeto = 'paciente'
    print('\n')
    print('-----------------------------------------------------')
    print(f'Incluindo novo registro de {objeto}')
    print('-----------------------------------------------------')
    print('\n')
    lista = []
    for i in range(len(titulos)):
        if i == 0: # inclusão de valor chave CPF ou CRM
            item = input(f'{titulos[i]}: ')
            while buscaItem(index_banco_de_dados, dados, item) == True:
                print('\n')
                print('-----------------------Atenção!---------------------------')
                print(f'O {titulos[i]} digitado já está cadastrado, digite outro!')
                print('----------------------------------------------------------')
                print('\n')
                item = input(f'{titulos[i]}: ')
            while item.isdigit() == False:
                print('\n')
                print('-----------------------Atenção!---------------------------')
                print(f'O {titulos[i]} digitado não é válido, use apenas números!')
                print('----------------------------------------------------------')
                print('\n')
                item = input(f'{titulos[i]}: ') 
            lista.append(item)
        elif i == 2: # inclusão de data de nascimento
            item = input(f'{titulos[i]}: ')
            while validaData(item) == False:
                print('\n')
                print('----------------------------Atenção!--------------------------------')
                print('Data em formato inválido. \n')
                print(f'{titulos[i]} deve ser digitado no formato dd/mm/aaaa!')
                print('--------------------------------------------------------------------')
                print('\n')
                item = input(f'{titulos[i]}: ')
            lista.append(item)    
        elif titulos[i] == 'E-mail(s)' or titulos[i] == 'Telefone(s)': # inclusão de telefones ou e-mails
            item = []
            num_itens = input(f'Entre com a quantidade de {titulos[i]} a registrar: ')
            while num_itens.isdigit() == False or num_itens == '0':
                print('\n')
                num_itens = input(f'Entre com a quantidade de {titulos[i]} a registrar: ')   
            j = 0
            # como "num_itens" é uma string, a variável precisa ser convertida
            # para inteiro
            while j < int(num_itens):
                print('\n')
                itens = input(f'Entre com o {titulos[i]} {j+1}: ')
                item.append(itens)
                j += 1
            lista.append(item) 
        else: #inclusão dos demais itens de cadastro
            item = input(f'{titulos[i]}: ')
            lista.append(item)
    dados[index_banco_de_dados].append(lista)
    adicionarNoArquivo(index_banco_de_dados, dados)
    retornaSubmenu(index_banco_de_dados, dados)
    
#====================================================================
# deleta item escolhido pela função "excluirItem"
# - o parâmetro "entrada" é a string correspondente ao valor do atributo
# chave que esta sendo buscado
def excluiItem(index_banco_de_dados, dados, entrada):
    comando = input('Digite 1 para deletar o item ou 2 para voltar ao submenu: ')
    while validarEscolha(comando, 2) == False:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('O valor digitado não corresponde ao valor requerido!')
        print('-----------------------------------------------------')
        print('\n')
        comando = input('Digite 1 para deletar o item ou 2 para voltar ao submenu: ')
        print('\n')
    if comando == '1': # deleta item
        indice = retornaIndice (index_banco_de_dados, dados, entrada)
        del dados[index_banco_de_dados][indice]
        # função atualiza o arquivo depois que o dados foi deletado
        atualizaArquivo(index_banco_de_dados, dados)
        # esta variável precisa ser uma string, a função "submenu" requer este tipo de variável
        opcao = str(index_banco_de_dados + 1)
        submenu(opcao, dados)
    elif comando == '2': #volta para o submenu
        opcao = str(index_banco_de_dados + 1)
        submenu(opcao, dados)
        
#====================================================================          
# - exclui item específico do banco de dados
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def excluirItem(index_banco_de_dados, dados):  
    titulos = titulosDados(index_banco_de_dados)
    if index_banco_de_dados == 0:
        objeto = 'médico'
    elif index_banco_de_dados == 1:
        objeto = 'paciente'
    print('\n')
    print('-----------------------------------------------------')
    print(f'Excluíndo registro de {objeto}')
    print('-----------------------------------------------------')
    print('\n')
    chave = listaItem(index_banco_de_dados, dados)
    if chave != "":
        excluiItem(index_banco_de_dados, dados, chave)
    else:
        retornaSubmenu(index_banco_de_dados, dados)
        
#====================================================================
# altera valores do item escolhido pela função "alterarItem"
# - o parâmetro "entrada" é a string correspondente ao valor do atributo
# chave que esta sendo buscado
def alteraItem(index_banco_de_dados, dados, titulos, entrada):
    comando = input('Digite 1 para alterar o item ou 2 para voltar ao submenu: ')
    while validarEscolha(comando, 2) == False:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('O valor digitado não corresponde ao valor requerido!')
        print('-----------------------------------------------------')
        print('\n')
        comando = input('Digite 1 para alterar o item ou 2 para voltar ao submenu: ')
        print('\n')
    if comando == '1': # altera item
        indice = retornaIndice (index_banco_de_dados, dados, entrada)
        for i in range(1,len(dados[index_banco_de_dados][indice])): 
            comando = input(f'Digite 1 para alterar e 2 para não alterar o {titulos[i]}: ')
            while validarEscolha(comando, 2) == False:
                print('\n')
                print('--------------------Atenção!-------------------------')
                print('O valor digitado não corresponde ao valor requerido!')
                print('-----------------------------------------------------')
                print('\n')
                comando = input(f'Digite 1 para alterar e 2 para não alterar o {titulos[i]}: ')
                print('\n')
            if comando == '1': # altera item
                print(f'O valor atual do {titulos[i]} é {dados[index_banco_de_dados][indice][i]}.')
                # altera atributo chave, para isso o novo atributo chave não pode estar
                # contido no banco de dados (evita redundância) e tem que ser apenas números
                if i == 0: # alterando atributo chave CPF ou CRM 
                    entrada = input(f'Entre com o novo {titulos[i]} ')
                    print('\n')
                    while entrada.isdigit() == False:
                        print('\n')
                        print('--------------------Atenção!-------------------------')
                        print('O valor digitado precisa ser apenas números!')
                        print('-----------------------------------------------------')
                        print('\n')
                        entrada = input(f'Entre com o novo {titulos[i]}: ')
                        print('\n')
                    while buscaItem(index_banco_de_dados, dados, entrada) == True:
                        print('\n')
                        print('--------------------Atenção!-------------------------')
                        print('O valor digitado já consta no banco de dados!')
                        print('-----------------------------------------------------')
                        print('\n')
                        entrada = input(f'Entre com o novo {titulos[i]}: ')
                        print('\n')
                    dados[index_banco_de_dados][indice][i] = entrada
                elif i == 2: # alteração de data de nascimento
                    entrada = input(f'Entre com o novo {titulos[i]} ')
                    print('\n')
                    while validaData(entrada) == False:
                        print('\n')
                        print('----------------------------Atenção!--------------------------------')
                        print('Data em formato inválido. \n')
                        print(f'{titulos[i]} deve ser digitado no formato xx/xx/xxxx (dia/mês/ano)!')
                        print('--------------------------------------------------------------------')
                        print('\n')
                        entrada = input(f'Entre com o novo {titulos[i]} ')
                    dados[index_banco_de_dados][indice][i] = entrada   
                # checa se o item da lista que esta sendo percorrida é tambem uma lista
                # como no caso dos telefones e emails                
                elif type(dados[index_banco_de_dados][indice][i]) == type (dados):
                    comando = input(f'Digite 1 para incluir um novo {titulos[i]} ou 2 para alterar os existentes: ')
                    while validarEscolha(comando, 2) == False:
                        print('\n')
                        print('--------------------Atenção!-------------------------')
                        print('O valor digitado não corresponde ao valor requerido!')
                        print('-----------------------------------------------------')
                        print('\n')
                        comando = input(f'Digite 1 para incluir um novo {titulos[i]} ou 2 para alterar os existentes: ')
                        print('\n')
                    # inclui item nos existentes
                    if comando == '1':
                        entrada = input(f'Digite o novo {titulos[i]} a ser incluído: ')
                        dados[index_banco_de_dados][indice][i].append(entrada)
                    # altera os demais item existentes
                    elif comando == '2':
                        for j in range(len(dados[index_banco_de_dados][indice][i])):
                            entrada = input(f'Digite o novo valor de {titulos[i]}: ')
                            dados[index_banco_de_dados][indice][i][j] = entrada                
                        
                else:
                    entrada = input(f'Digite o novo valor de {titulos[i]}:')
                    dados[index_banco_de_dados][indice][i] = entrada

        # função atualiza o arquivo depois da alteração       
        atualizaArquivo(index_banco_de_dados, dados)
        # esta variável precisa ser uma string, a função "submenu" requer este tipo de variável
        opcao = str(index_banco_de_dados + 1)
        submenu(opcao, dados)
    elif comando == '2': #volta para o submenu
        opcao = str(index_banco_de_dados + 1)
        submenu(opcao, dados)

#====================================================================
# - exclui item específico do banco de dados
# - o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def alterarItem(index_banco_de_dados, dados):
    titulos = titulosDados(index_banco_de_dados)
    if index_banco_de_dados == 0:
        objeto = 'médico'
    elif index_banco_de_dados == 1:
        objeto = 'paciente'
    print('\n')
    print('-----------------------------------------------------')
    print(f'Alterando registro de {objeto}')
    print('-----------------------------------------------------')
    print('\n')
    chave = listaItem(index_banco_de_dados, dados)
    if chave != "":
        alteraItem(index_banco_de_dados, dados, titulos, chave)
    else:
        retornaSubmenu(index_banco_de_dados, dados)


##############################################################################
## Definindo as funções secundárias implementadas para dados em dicionários ##
##############################################################################
# funções para os submenus de Consultas 

#==================================================================== 
# carrega os dados a partir de um arquivo específico e popula um dicionário 
# específico com os dados oriundos do arquivo
# recebe como parâmetros o nome do arquivo que será utilizado e o dicionário
# que será populado
def carregaDoArquivo2(nome_arquivo,dicionario):
    if checaArquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        for linha in arquivo:
            linha = linha.strip() # o método ".strip()" retira o "\n" do conteúdo da linha do arquivo
            conteudo = linha.split(';') # ; é o separador usado nos arquivos
            # conteudo é uma lista contendo os dados que no arquivo estavam separados por ";"
            # onde índice 0 corresponde a chave do dicionário, ínidice 1 o diagnóstico e
            # índice 2 corresponde aos medicamentos
            dicionario[conteudo[0]] = {
                "Diagnóstico:" : conteudo[1],
                "Medicamento:" : conteudo[2]
                }
        arquivo.close()
    else:
        arquivo = open(nome_arquivo, 'w')
        arquivo.close()

#==================================================================== 
# popula arquivos com informações, recebendo como parâmetro a referência ao
# arquivo que será utilizado e conteúdo que será adicionado 
def adicionaAoArquivo2(nome_arquivo,conteudo):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(conteudo)
    arquivo.close()

def atualizaArquivo2(nome_arquivo,dicionario):
    arquivo = open(nome_arquivo, 'w')
    conteudo = '' 
    for chave in dicionario:
        conteudo += chave
        for chave2 in dicionario[chave]:
            conteudo += ';' + dicionario[chave][chave2]
        conteudo += '\n'
    arquivo.write(conteudo)
    arquivo.close()

   
#==================================================================== 
# - cria uma chave para uma consulta 
# - recebe como o parâmetro "index_banco_de_dados" seleciona um banco de dados específico
# de acordo com o nome do submenu que está sendo acessado (neste caso tem que ser 2)
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
def geraChave(cpf_paciente, crm_medico):
    #fazer uma função que gera a chave
    data = input('Entre com uma data (formato dd/mm/aaaa): ')
    print('\n')
    while validaData(data) == False:
        print('\n')
        print('-----------------------Atenção!---------------------------')
        print('             O valor digitado não é válido!')
        print('----------------------------------------------------------')
        print('\n')
        data = input('Entre com uma data (formato dd/mm/aaaa): ')
    print('\n')
    horario = input('Entre com um horário (formato hh:mm): ')
    while validaHorario(horario) == False:
        print('\n')
        print('-----------------------Atenção!---------------------------')
        print('             O valor digitado não é válido!')
        print('----------------------------------------------------------')
        print('\n')
        horario = input('Entre com um horário (formato hh:mm): ')
    return cpf_paciente + ',' + crm_medico + ',' + data + ',' + horario
            

#==================================================================== 
# - retorna uma chave criada para uma consulta 
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
def retornaChaveConsulta(dados):
    cpf = input('Entre com o CPF do paciente: ')
    while cpf.isdigit() == False:
        print('\n')
        print('-----------------------Atenção!---------------------------')
        print('    O valor digitado não é válido, use apenas números!')
        print('----------------------------------------------------------')
        print('\n')
        cpf = input('Entre com o CPF do paciente: ')
    # função busca item funciona para o banco de dados de pacientes e médicos
    # buscando por um paciente
    if buscaItem(1, dados, cpf) == False:
        # se paciente não está cadastrado retorna para o submenu
        print('\n')
        print('-----------------------Atenção!---------------------------')
        print('              Paciente não cadastrado!')
        print('----------------------------------------------------------')
        print('\n')
        print(cpf)
        submenu('3', dados)
    else:
        index_paciente = retornaIndice(1, dados, cpf)
        paciente = dados[1][index_paciente][1] # nome = índice 1
        print(f'Paciente: {paciente}')
        print('\n')
        crm = input('Entre com o CRM do médico: ')
        while crm.isdigit() == False:
            print('\n')
            print('-----------------------Atenção!---------------------------')
            print('   O valor digitado não é válido, use apenas números!')
            print('----------------------------------------------------------')
            print('\n')
            crm = input('Entre com o CRM do médico: ')
        if buscaItem(0, dados, crm) == False:
            # se o médico não está cadastrado retorna para o submenu
            print('\n')
            print('-----------------------Atenção!---------------------------')
            print('               Médico não cadastrado!')
            print('----------------------------------------------------------')
            print('\n')
            submenu('3', dados)
        else:
            index_medico = retornaIndice(0, dados, crm)
            medico = dados[0][index_medico][1] # nome = índice 1
            print(f'Médico: {medico}')
            print('\n')
            chave = geraChave(cpf, crm)
            while buscaChave(chave, dados[2]):
                print('\n')
                print('-----------------------Atenção!---------------------------')
                print('   A data e horário escolhido já estão registrados!')
                print('----------------------------------------------------------')
                print('\n')
                opcao = input('Digite 1 para tentar nova data e horário, ou 2 para retornar ao submenu: ')
                while validarEscolha(comando, 2) == False:
                    print('\n')
                    print('-----------------------Atenção!---------------------------')
                    print('          O valor digitado não é válido!')
                    print('----------------------------------------------------------')
                    print('\n')
                    opcao = input('Digite 1 para tentar nova data e horário, ou 2 para retornar ao submenu: ')
                if opcao == '1':
                    chave = geraChave(cpf, crm)
                elif opcao == '2':
                    submenu('3', dados)
            return  chave

#==================================================================== 
# - busca por um registro de uma consulta específicapresente no banco de dados,
# a partir de informações fornecidas pelo usuário
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
# - o parâmetro "operação" é uma string que determina o retorno da função, onde os valores
# permitos são:
# "n" - função não retorna nada
# "c" - função retorna uma chave de um dicionário, que é uma string
# "d" - função retorna a referência para um dicionário
def consultaEspecifica(dados, operacao):
    if len(dados[2]) == 0:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('          Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')
        submenu('3', dados)
    else:
        # criando  a chave da consulta
        cpf = input('Entre com o CPF do paciente: ')
        print('\n')
        crm = input('Entre com o CRM do médico: ')
        print('\n')
        chave_busca = geraChave(cpf, crm)
        check = False
        for chave in dados[2]:
            if chave_busca == chave:
                check = True   
        if check:
            print('\n')
            print('-------------------------------------------------------------------------------')
            print('Consulta procurada:')
            print('-------------------------------------------------------------------------------')
            print(f'Chave da consulta (CPF,CRM,data,horário): {chave}')
            for chave2 in dados[2][chave_busca]:
                print(f'{chave2} {dados[2][chave_busca][chave2]}')
            print('--------------------------------------------------------------------------------')
                # retorna a referência para o dicionário (dados[2][chave] = consultas {"chave":consulta}, onde consulta = {})
                # onde será alterado o diagnostico e os medicamentos
            if operacao == 'c':
                return chave_busca
            elif operacao == 'd':
                return dados[2][chave_busca]
        else:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('           Consulta não encontrada !')
            print('-----------------------------------------------------')
            print('\n')
            if operacao == 'c':
                return '' # retorna string vazia
            elif operacao == 'd':
                return {} # retorna um dicionário vazio

            
#==================================================================== 
# - lista o registro de todas as consulta presentes no banco de dados
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
def listarConsultas(dados):
    if len(dados[2]) == 0:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('          Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')
        submenu('3', dados)
    else:
        print('\n')
        print('-------------------------------------------------------------------------------')
        print('Consultas Registradas')
        print('-------------------------------------------------------------------------------')
        for chave in dados[2]:
            print(f'Chave da consulta (CPF,CRM,data,horário): {chave}')
            for chave2 in dados[2][chave]:
                print(f'{chave2} {dados[2][chave][chave2]}')
            print('-------------------------------------------------------------------------------')
        submenu('3', dados)
    

#====================================================================  
# dispara a consulta específica no menu de consultas
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
def listarConsultaEspecifica(dados):
    consultaEspecifica(dados, 'n')
    submenu('3', dados)

#==================================================================== 
# - inclui o registro de uma consulta no banco de dados
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
def incluirConsulta(dados):
    # criando e retornando a chave da consulta
    chave = retornaChaveConsulta(dados)
    diagnostico = input('Entre com o diagnóstico do paciente: ')
    medicamentos = input('Entre com os medicamentos receitados: ')
    consulta = {}
    consulta['Diagnóstico:'] = diagnostico
    consulta['Medicamentos:'] = medicamentos
    dados[2][chave] = consulta # "dados[2]" é o dicionário consultas
    conteudo = chave + ';' + diagnostico + ';' + medicamentos + '\n'
    adicionaAoArquivo2('consultas.txt', conteudo)
    submenu('3', dados)
           
#==================================================================== 
# - altera o registro de uma consulta no banco de dados
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)
def alterarConsulta(dados):
    dicionario = consultaEspecifica(dados, 'd')
    if len(dicionario) != 0:
        opcao = input('Entre com 1 para alterar o elemento e 2 para não alterar: ')
        while validarEscolha(opcao, 2) == False:
            print('\n')
            print('-----------------------Atenção!---------------------------')
            print('          O valor digitado não é válido!')
            print('----------------------------------------------------------')
            print('\n')
            opcao = input('Entre com 1 para alterar o elemento e 2 para não alterar: ')
        if opcao == '1':
            for chave in dicionario:
                print(f'{chave} {dicionario[chave]}')
                opcao2 = input(f'Entre com 1 para alterar e 2 para não alterar o campo {chave} ')
                while validarEscolha(opcao2, 2) == False:
                    print('\n')
                    print('-----------------------Atenção!---------------------------')
                    print('          O valor digitado não é válido!')
                    print('----------------------------------------------------------')
                    print('\n')
                    opcao2 = input(f'Entre com 1 para alterar e 2 para não alterar o campo {chave} ')
                if opcao2 == '1':
                    entrada = input(f'Entre com o novo valor para o campo {chave} ')
                    dicionario[chave] = entrada
            atualizaArquivo2('consultas.txt',dados[2])
            submenu('3', dados) 
        elif opcao == '2':
            submenu('3', dados)
    else:
        submenu('3', dados)

#==================================================================== 
# - deleta o registro de uma consulta no banco de dados
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa (dentro desta lista, no índice 2 esta o dicionário para as consultas)        
def deletaConsulta(dados):
    chave = consultaEspecifica(dados, 'c')
    if chave != '':
        opcao = input(f'Digite 1 para deletar este registro ou 2 para não deletar: ')
        while validarEscolha(opcao, 2) == False:
            print('\n')
            print('-----------------------Atenção!---------------------------')
            print('          O valor digitado não é válido!')
            print('----------------------------------------------------------')
            print('\n')
            opcao = input(f'Digite 1 para deletar este registro ou 2 para não deletar: ')
        if opcao == '1':
            # o dados[2] = dicionario consultas
            del dados[2][chave]
            atualizaArquivo2('consultas.txt',dados[2])
            submenu('3', dados)
        elif opcao == '2':
            submenu('3', dados)
    else:
        submenu('3', dados)
    
##########################################################################
## Definindo as funções secundárias implementadas geração de relatórios ##
##########################################################################
# funções para o menu de relatórios

#==================================================================== 
# lista médicos de um determinada especialidade de acordo com
# entrada do usuário
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
def medicosPorEspecialidade(dados):
    # se a lista de médico não está vazia executa o código abaixo
    if len(dados[0]) != 0: # indíce 0 corresponde a lista de médicos
        # variável usada para confirmar a existência do dado procurado
        # no banco de dados
        check = False
        entrada = input('Entre com uma especialidade médica :').upper()
        # checa se existe a especialidade médica no banco de dados
        for i in range(len(dados[0])):
            # indíce 0 corresponde a lista de médicos
            # índice 4 equivale a especialidade médica no banco de dados dos médicos
            # utiliza-se o método .upper() na "entrada" e aqui para evitar problemas
            # com caractéres maiscúlos e minúsculos
            if entrada == dados[0][i][4].upper(): 
                check = True
        # se o termo existe executa está parte
        if check:
            titulos = titulosDados(0)
            print('\n')
            print('-----------------------------------------------------')
            print('Listando Médicos por especialidade')
            print('-----------------------------------------------------')
            print('\n')
            for i in range(len(dados[0])):
                if entrada == dados[0][i][4].upper():
                    for j in range(len(dados[0][i])):
                        imprimeItens(0, dados, titulos, i, j)
        # se o termo não existe no banco de dados executa este
        else:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('          Não há dados a serem listados!')
            print('-----------------------------------------------------')
            print('\n')
    # se a lista de médico está vazia executa o código abaixo
    else:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('          Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')
        
#==================================================================== 
# lista pacientes de acordo com a idade fornecida pelo usuário
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
def pacientesPorIdades(dados):
    # se a lista de pacientes não está vazia executa o código abaixo
    if len(dados[1]) != 0: # indíce 1 corresponde a lista de pacientes
        # trecho de código que manipula data
        import datetime # inporta biblioteca que manipula data
        data = datetime.datetime.now() # retorna a data completa (ano, mês, dia, hora, minuto, segundo) de hoje
        ano = data.strftime("%Y") # extraia o valor do ano para uma string
        # variável de checagem que indica a existencia do dado procurado no banco de dados
        check = False
        entrada = input('Procurando por pacientes com idade menor que: ')
        # validando a entrada fornecida pelo usuário (precisa ser um número)
        while entrada.isdigit() == False:
            print('\n')
            print('-----------------------Atenção!---------------------------')
            print('          O valor digitado não é válido!')
            print('----------------------------------------------------------')
            print('\n')
            entrada = input('Procurando por pacientes com idade menor que: ')
        # checando se os dados procurados existem no banco de dados e atualizando a variável "check"
        for i in range(len(dados[1])):
            # indíce 1 corresponde a lista de pacientes
            # índice 2 equivale a data de nascimento dos pacientes
            data_paciente = dados[1][i][2]
            # extraindo apenas os ano de nascimento do paciente, que é uma string
            ano_paciente = data_paciente[6:]
            # calculando a idade do paciente
            # tanto "ano" e "ano_paciente" são strings, portanto precisam ser convertidadas para
            # inteiro antes do cálculo
            idade = int(ano) - int(ano_paciente)
            # "entrada" também é uma string, então precisa ser convertida em inteiro antes de
            # comparada com "idade"
            if idade < int(entrada):
                check = True
                print(check)
        # se o dado existe executa este trecho
        if check:
            titulos = titulosDados(1)
            print('\n')
            print('-----------------------------------------------------')
            print(f'Listando pacientes com idade menor que {entrada} anos')
            print('-----------------------------------------------------')
            print('\n')
            for i in range(len(dados[1])):
                data_paciente = dados[1][i][2]
                ano_paciente = data_paciente[6:]
                idade = int(ano) - int(ano_paciente)
                if idade < int(entrada):
                    for j in range(len(dados[1][i])):
                        imprimeItens(1, dados, titulos, i, j)
                print('-----------------------------------------------------')
        # se os dados buscados não existem no banco de dados executa este trecho de código
        else:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('          Não há dados a serem listados!')
            print('-----------------------------------------------------')
            print('\n')
    # se a lista de paciente está vazia executa o código abaixo
    else:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('          Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')

#==================================================================== 
# função busca por nome de paciente/médico de acordo com parâmetros utilizado,
# se "chave_busca" = cpf e "lista" = lista de pacientes a função retorna o nome de
# um paciente; se "chave_busca" = crm e "lista" = lista de médicos a função retorna
# o nome de médico
def buscaNomePacienteOuMedico(chave_busca,lista):
    tamanho_lista = len(lista)
    for index in range(tamanho_lista):
        if chave_busca == lista[index][0]:
            return lista[index][1]

#==================================================================== 
# busca por consultas realizadas em datas posteriores a uma data calculada no passado
# e imprime os resultados encontrados
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
def consultasPorData(dados):
    # se o dicionário de consultas estiver vazio executa o código abaixo
    if len(dados[2]) != 0: # o dicionário contendo informações sobre as consultas esta em dado[2]
        # trecho de código que manipula data
        import datetime # importa biblioteca que manipula data
        # retorna a data completa (ano, mês, dia, hora, minuto, segundo,
        # microsegundos) de hoje
        data_hoje = datetime.datetime.now() 
        ano_hoje = data_hoje.strftime("%Y") # extraia o valor do ano corrente para uma string
        mes_hoje = data_hoje.strftime("%m") # extraia o valor do mês corrente  para uma string
        dia_hoje = data_hoje.strftime("%d") # extraia o valor do dia de hoje para uma string
        print('\n')
        entrada = input('Entre com a quantidade de dias passados para gerar relatório de consultas: ')
        while entrada.isdigit() == False:
            print('\n')
            print('-----------------------Atenção!---------------------------')
            print('          O valor digitado não é válido!')
            print('----------------------------------------------------------')
            print('\n')
            entrada = input('Entre com a quantidade de dias passados para gerar relatório de consultas: ')
        # calculando uma data no passado
        data_passado = calculaDataPassada(dia_hoje,mes_hoje,ano_hoje, entrada)
        # separa os componentes da data calculada em uma lista
        lista_data_passado = data_passado.split('/')
        dia_passado = lista_data_passado[0]
        mes_passado = lista_data_passado[1]
        ano_passado = lista_data_passado[2]
        # define variável de checagem que confirma se há dados a serem impressos
        check1 = False
        # o dicionário contendo as informações sobre consultas estão em "dados[2]"
        for chave in dados[2]:
            # define uma lista com os termos presentes na chave do dicionário
            lista = chave.split(',')
            # a data da consulta é o item de índice 2 na lista com os dados da chave do dicionário
            data = lista[2]
            # o horário da consulta é o item de índice 3 na lista com os dados da chave do dicionário
            horario = lista[3]
            # separando os componentes da data da consulta em uma lista
            lista_data = data.split('/')
            dia = lista_data[0]
            mes = lista_data[1]
            ano = lista_data[2]
            # variável de checagem que indica se item do dicionário passa na checagem das
            # condicionais envolvendo a data calculada
            check2 = False
            if int(ano) > int(ano_passado):
                check1 = True
                check2 = True
            elif int(ano) == int(ano_passado):
                if int(mes) > int(mes_passado):
                    check1 = True
                    check2 = True
                elif int(mes) == int(mes_passado):
                    if int(dia) > int(dia_passado):
                        check1 = True
                        check2 = True
            # se "check2" é verdadeira o item do dicionário passou no teste das condicionais
            # e o mesmo será impresso
            if check2:
                # a primeira variável da lista contendo os dados da chave do dicionário
                # é o CRM do médido
                CRM = lista[0]
                # a segunda variável da lista contendo os dados da chave do dicionário
                # é o CPF do paciente
                CPF = lista[1]
                # imprimindo do dados filtrados do dicionário
                print('\n')
                # busca o nome do médico usando a função "buscaNomePacienteOuMedico"
                print(f'Médico: {buscaNomePacienteOuMedico(CRM,dados[0])}')
                print(f'CRM: {CRM}')
                # busca o nome do paciente usando a função "buscaNomePacienteOuMedico"
                print(f'Paciente: {buscaNomePacienteOuMedico(CPF,dados[1])}')
                print(f'CPF: {CPF}')
                print(f'Data: {data} - Horário: {horario}')
                # percorre o dicionário que contém diagnótico e medicação e imprime os termos,
                # onde o mesmo é definido como "dados[2][chave]"
                for chave2 in dados[2][chave]:
                    print(f'{chave2} {dados[2][chave][chave2]}')
                print('-------------------------------------------------------------------------------')
            # se "check1" for falso, não há nada a ser impresso
        if check1 == False:
            print('\n')
            print('--------------------Atenção!-------------------------')
            print('          Não há dados a serem listados!')
            print('-----------------------------------------------------')
            print('\n') 
    # se o dicionário de consultas estiver vazio executa este trecho de código
    else:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('          Não há dados a serem listados!')
        print('-----------------------------------------------------')
        print('\n')

##########################################################################
################## Iniciando execução do programa ########################
##########################################################################
main()
