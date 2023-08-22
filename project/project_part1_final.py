''' 
Projeto AP1S1
Tema 1: Hospital
Alunos: João Pedro da Silva e Thiane Deprá Saravalle
Etapa 1
'''

##########################################################################
################### Definindo a função principal #########################
##########################################################################
def main():
    # os dados serão estruturados da seguinte maneira:
    # dados = [
    # [medicos](índice 0), [pacientes] (ínidice 1)
    # ]
    # medicos = [[medico1], [medico2], ... , [medicoN]]
    # medicoN = [
    # CRM (chave), Nome, Data de Nascimento, Sexo, Especialidade, Universidade em que
    # se formou, [E-mails] (uma lista com mais de um e-mail), [Telefones] (uma lista
    # com mais de um telefone)
    # ]
    # medicos = [[medico1], [medico2], ... , [medicoN]]
    # pacientes = [[paciente1], [paciente2], ... [pacienteN]]
    # pacienteN = [
    # CPF(chave), Nome, Data de Nascimento, Sexo, Plano de saúde,
    # [E-mails] (uma lista com mais de um e-mail), [Telefones] (uma lista
    # com mais de um telefone)
    # ]
    dados = []
    medicos = []
    pacientes = []
    dados.append(medicos)
    dados.append(pacientes)
    
    # variáveis para teste
    paciente1 = [
                '1',
                'João Pedro da Silva',
                '00/00/0000',
                'Masculino',
                'xxxx',
                ['jp@mail.com', 'jp2@mail.br'],
                ['111111111', '22222222']
            ]
    paciente2 = [
                '2',
                'Thiane Deprá Saravalle',
                '00/00/0000',
                'Feminino',
                'xxxxxx',
                ['xxxxxx@mail.com'],
                ['0000000000']
            ]
    medico1 = [
            '1',
            'José da Silva ',
            '00/00/0000',
            'Masculino',
            'Pediatra',
            'xxx',
            ['xxxxxx@mail.com'],
            ['0000000000']
            ]
    medico2 = [
            '2',
            'Roberta da Silva ',
            '00/00/0000',
            'Feminino',
            'Cirurgiã Geral',
            'xxx',
            ['xxxxxx@mail.com'],
            ['0000000000']
        ]
    
    pacientes.append(paciente1)
    pacientes.append(paciente2)
    medicos.append(medico1)
    medicos.append(medico2)
    criaCabecalho()
    menu(dados)
    
    
       
    
##########################################################################
################# Definindo as funções secundárias #######################
##########################################################################

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
    print('\n')
    print('---------------------------------------------------')
    print('\n')
    opcao = input('Entre com o valor numérico da opção desejada: ')
    while validarEscolha(opcao, 2) == False:
        print('\n')
        print('--------------------Atenção!-------------------------')
        print('O valor digitado não corresponde a um valor válido!')
        print('-----------------------------------------------------')
        print('\n')
        opcao = input('Entre com o valor numérico da opção desejada: ')
        print('\n')
    if opcao == '1':
        submenu(opcao, dados)
    elif opcao == '2':
        submenu(opcao, dados)
   
#====================================================================
# - cria o submenu
# - o parâmetro "cod_submenu" precisa ser uma string e
# corresponde ao valor númerico da opção selecionada no menu
# - o parâmetro "dado" é uma lista contendo os dados que serão manipulados
# pelo programa
def submenu(cod_submenu, dados):
    if cod_submenu == '1':
        nome_do_submenu = 'Médicos'
        index_dados = 0
    elif cod_submenu == '2':
        nome_do_submenu = 'Pacientes'
        index_dados = 1
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
def retornaIndice (index_banco_de_dados, dados, entrada):
    for i in range(len(dados[index_banco_de_dados])):
        # aqui o index é 0, pois o elemento chave é o primeiro da
        # lista "paciente" ou "medico"
        if entrada == dados[index_banco_de_dados][i][0]:
            return i
       
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
        if i == 0:
            print('\n')
            item = input(f'{titulos[i]}: ')
            while buscaItem(index_banco_de_dados, dados, item) == True:
                print('\n')
                print(f'O {titulos[i]} digitado já está cadastrado, digite outro!')
                item = input(f'{titulos[i]}: ')
            while item.isdigit() == False:
                print('\n')
                print(f'O {titulos[i]} digitado não é válido, use apenas números!')
                item = input(f'{titulos[i]}: ') 
            lista.append(item)

        elif titulos[i] == 'E-mail(s)' or titulos[i] == 'Telefone(s)':
            item = []
            num_itens = input(f'Entre com a quantidade de {titulos[i]} a registrar')
            while num_itens.isdigit() == False:
                print('\n')
                num_itens = input(f'Entre com a quantidade de {titulos[i]} a registrar')
                
            j = 0
            # como "num_itens" é uma string, a variável precisa ser convertida
            # para inteiro
            while j < int(num_itens):
                print('\n')
                itens = input(f'Entre com o {titulos[i]} {j+1}: ')
                item.append(itens)
                j += 1
           
            lista.append(item) 
        else:
            item = input(f'{titulos[i]}: ')
            lista.append(item)
    dados[index_banco_de_dados].append(lista)
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
                if i == 0: 
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
                    # altera os item existentes
                    elif comando == '2':
                        for j in range(len(dados[index_banco_de_dados][indice][i])):
                            entrada = input(f'Digite o novo valor de {titulos[i]}: ')
                            dados[index_banco_de_dados][indice][i][j] = entrada                
                        
                else:
                    entrada = input(f'Digite o novo valor de {titulos[i]}:')
                    dados[index_banco_de_dados][indice][i] = entrada
                
        
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

        
##########################################################################
################## Iniciando execução do programa ########################
##########################################################################
main()
