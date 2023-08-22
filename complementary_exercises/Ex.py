'''
Exercício:

Considere a base disponível no site do Data Rio(1) com dados individuais dos
casos confirmados de COVID-19 no município do Rio de Janeiro. Esta base
de dados reflete os dados de óbitos da base do Ministério da Saúde e omite
informações pessoais como idade e sexo, para que não seja possível a
identificação pessoal dos casos. Cada registro nessa base contém as
seguintes informações separadas por ponto e vírgula (;):
- dt_notific: data em que foi feita a notificação do caso.
- dt_inicio_sintomas: data relatada do início dos sintomas.
- bairro_resid__estadia: bairro de residência ou estadia do paciente
usando a lista oficial de bairros do município do Rio de Janeiro.
- ap_residencia_estadia: Área de Planejamento em Saúde
correspondente ao bairro de residência ou estadia do paciente.
- evolução: evolução do caso, podendo ser ativo, óbito ou recuperado.
- dt_óbito: data do óbito
- cep: CEP do endereço informado na notificação.
- Data_atualização: data de atualização do registro
Implemente em Python um programa que leia essa base de dados (arquivo
texto). Em seguida, o programa deve apresentar para o usuário o seguinte
menu de opções e deve implementar cada operação usando funções:

Menu:
1 – Mostrar o total e a porcentagem de óbitos por bairro
2 – Mostrar a data em que foi notificado o primeiro caso de Covid-19
3 – Mostrar o bairro onde ocorreu a primeira notificação de Covid-19
4 – Mostrar o total de óbitos no município do Rio de Janeiro
5 – Mostrar o total e a porcentagem de óbitos por CEP


Além de apresentar as saídas para o usuário no monitor, o programa
deverá imprimir também os dados em um arquivo texto, gerando um
relatório que conterá todas as informações solicitadas pelo usuário através
do menu.
Atenção: Não use variáveis globais dentro das funções. Utilize
parâmetros para fazer a transferência de valores de uma função a outra

(1)Fonte: https://www.data.rio/datasets/cep-dos-casos-confirmados-decovid-19-no-munic%C3%ADpio-do-rio-de-janeiro (acesso em 21/08/2020).
'''

# definindo função principal
#--------------------------------------------------
def main():
    menuVisivel = True
    # carregando dados do arquivo para a lista "dados"
    arquivo = open('dados.csv', 'r')
    # em "dados" cada linha do arquivo será armazenada como uma outra lista
    dados = [] 
    for linha in arquivo:
        linha = linha.strip() # retira "\n" contido no final de cada linha do arquivo
        lista = linha.split(';') # armazena os dados em uma lista usando como separador ";"
        dados.append(lista) # adiciona a lista "dados" as listas contendo as informações de cada linha
    arquivo.close()
    while menuVisivel:
        menu()
        opc = input('\n Escolha uma opção: ')
        if opc == '1':
            nome_arquivo = input('\n Dê um nome ao arquivo de relatório: ') + '.txt'
            geraRelatorio(nome_arquivo,'Óbitos por Bairro', obitosPorBairro(dados))
        elif opc == '2':
            nome_arquivo = input('\n Dê um nome ao arquivo de relatório: ') + '.txt'
            geraRelatorio(nome_arquivo,'Data Primeira Notificação', primeiraNotificacao(dados))
        elif opc == '3':
            nome_arquivo = input('\n Dê um nome ao arquivo de relatório: ') + '.txt'
            geraRelatorio(nome_arquivo,'Bairro(s) com ocorrência(s) na data da primeira notificação', primeiraNotificacaoEmBairros(dados))
            
            
        elif opc == '4':
            nome_arquivo = input('\n Dê um nome ao arquivo de relatório: ') + '.txt'
            geraRelatorio(nome_arquivo,'Total de Óbitos', totalObitos(dados))
        elif opc == '5':
            nome_arquivo = input('\n Dê um nome ao arquivo de relatório: ') + '.txt'
            geraRelatorio(nome_arquivo,'Óbitos por CEP', obitosPorCEP(dados))
        elif opc == '6':
            menuVisivel = False 
        
    
# definindo demais funções
#--------------------------------------------------

# constrói o menu
def menu():
    print('Menu:')
    print('1 – Mostrar o total e a porcentagem de óbitos por bairro')
    print('2 – Mostrar a data em que foi notificado o primeiro caso de Covid-19')
    print('3 – Mostrar o bairro onde ocorreu a primeira notificação de Covid-19')
    print('4 – Mostrar o total de óbitos no município do Rio de Janeiro')
    print('5 – Mostrar o total e a porcentagem de óbitos por CEP')
    print('6 – Finalizar aplicação')
          

# salva relatório em arquivo
# parâmetros:
# referencia_arquivo - refrência ao nome do arquivo onde será salvo o relatório
# titulo - string com o título do relatório
# conteudo_arquivo - string com o conteúdo do arquivo
def geraRelatorio(referencia_arquivo, titulo, conteudo_arquivo):
    arquivo = open(referencia_arquivo, 'w')
    conteudo = 'Relatório Covid Rio de Janeiro - ' + titulo + ' \n'
    conteudo += conteudo_arquivo
    arquivo.write(conteudo)
    arquivo.close()
    
# mostra o total e a porcentagem de óbitos por bairro
# parâmetros:
# lista_dados - lista de listas contendo os dados carregados do arquivo
def obitosPorBairro(lista_dados):
    # organizando os dados com auxílio de dicionários
    # obitos = {'BAIRRO 1':numero_obitos, ..., 'BAIRRO N':numero_obitos}
    obitos = {}
    total_obitos = 0
    for i in range(len(lista_dados)):
        # informação sobre óbitos estão em "lista_dados[i][4]"
        if lista_dados[i][4].lower() == 'obito':
            # bairos estão em "lista_dados[i][2]"
            if lista_dados[i][2] in obitos:
                obitos[lista_dados[i][2]] += 1
            else:
                obitos[lista_dados[i][2]] = 1
    # calculando o total de óbitos
    for chave in obitos.keys():
        total_obitos += obitos[chave]
    # imprimindo os resultados e gerando conteúdo para arquivo relatório
    conteudo = '-----------------------------------------------------------------' + '\n'
    conteudo += 'BAIRRO | número de óbitos | percentual de óbitos' + '\n'
    conteudo += '-----------------------------------------------------------------' + '\n'
    print(conteudo)
    for chave in obitos.keys():
        percentual = (obitos[chave] / total_obitos)*100
        # os número precisam ser convertidos para string para serem concatenados ao conteúdo
        conteudo += chave + '|' + str(obitos[chave]) + '|' + str(percentual) + '%' + '\n'
        print(f'{chave} | {obitos[chave]} óbitos | {percentual}%')
    print('-----------------------------------------------------------------')
    print('Informação processada e relatório salvo com sucesso!')
    conteudo += '-----------------------------------------------------------------' + '\n'
    return conteudo


# mostra data da primeira notificação de COVID
# parâmetros:
# lista_dados - lista de listas contendo os dados carregados do arquivo
def primeiraNotificacaoEmBairros(lista_dados):
    data = primeiraNotificacao(lista_dados)
    bairros = {}
    for i in range(len(lista_dados)):
        # datas de notificação estão em "lista_dados[i][0]"
        if data == lista_dados[i][0]:
            if lista_dados[i][2] not in bairros:
                # bairros estão em "lista_dados[i][2]"
                bairros[lista_dados[i][2]] = 1
            else:
                bairros[lista_dados[i][2]] += 1
    conteudo = ''   
    print(f'Notificações ocorridas para a data {data} em cada bairro:')
    for chave in bairros.keys():
        conteudo += chave + ':' + str(bairros[chave]) +' ocorrências' + '\n'
        print(chave + ':' + str(bairros[chave]))
    print('\n')
    return conteudo
    

            
        

# encontra o a data da primeira notificação de COVID
# parâmetros:
# lista_dados - lista de listas contendo os dados carregados do arquivo
def primeiraNotificacao(lista_dados):
    # atribui inicialmente como primeira notificação a primeira data presente em "lista_dados"
    # que é "lista_dados[0][0]"
    data_not = lista_dados[0][0].split('/') # gera a lista data_not = [dia, mês, ano] todos como string
    # percore "lista_dados"
    for i in range(len(lista_dados)):
        # datas de notificação estão em "lista_dados[i][0]"
        data = lista_dados[i][0].split('/') # gera a lista data = [dia, mês, ano] todos como string
        # o arquivo com os dados apresenta algumas datas de notificação em branco, ou seja, igual ''
        # assim, é necessaŕio a inserção da condicional "lista_dados[i][0] !=''"
        if lista_dados[i][0] !='' and lista_dados[0][0] != lista_dados[i][0]:
            # como os dados nas listas "data" e "data_not" são strings, eles presisam ser convertidos
            # em inteiros para serem comparados
            if int(data_not[2]) >= int(data[2]): # comparando ano
                if int(data_not[1]) >= int(data[1]): # comparando mês
                    if int(data_not[0]) > int(data[0]): # comparando dia
                        data_not = data # atualizando a data da primeira notficação
    print(data_not[0] + '/' + data_not[1] + '/' + data_not[2])
    return data_not[0] + '/' + data_not[1] + '/' + data_not[2] # retornando conteúdo para colocar em arquivo
                       
                
    
    
# mostra total de óbitos
# parâmetros:
# lista_dados - lista de listas contendo os dados carregados do arquivo
def totalObitos(lista_dados):
    total_obitos = 0
    # informação sobre óbitos estão em "lista_dados[i][4]"
    for i in range(len(lista_dados)):
        if lista_dados[i][4].lower() == 'obito':
            total_obitos += 1
    print(f'Total de óbitos: {total_obitos}')
    return str(total_obitos) + ' óbitos'

# mostra o total e a porcentagem de óbitos por CEP
# parâmetros:
# lista_dados - lista de listas contendo os dados carregados do arquivo
def obitosPorCEP(lista_dados):
    # organizando os dados com auxílio de dicionários
    # obitos = {'CEP 1':numero_obitos, ..., 'CEP N':numero_obitos}
    obitos = {}
    total_obitos = 0
    for i in range(len(lista_dados)):
        # informação sobre óbitos estão em "lista_dados[i][4]"
        if lista_dados[i][4].lower() == 'obito':
            # CEPs estão em "lista_dados[i][6]"
            if lista_dados[i][6] in obitos:
                obitos[lista_dados[i][6]] += 1
            else:
                obitos[lista_dados[i][6]] = 1
    # calculando o total de óbitos
    for chave in obitos.keys():
        total_obitos += obitos[chave]
    # imprimindo os resultados e gerando conteúdo para arquivo relatório
    conteudo = '-----------------------------------------------------------------' + '\n'
    conteudo += 'CEP | número de óbitos | percentual de óbitos' + '\n'
    conteudo += '-----------------------------------------------------------------' + '\n'
    print(conteudo)
    for chave in obitos.keys():
        percentual = (obitos[chave] / total_obitos)*100
        # os número precisam ser convertidos para string para serem concatenados ao conteúdo
        conteudo += chave + '|' + str(obitos[chave]) + '|' + str(percentual) + '%' + '\n'
        print(f'{chave} | {obitos[chave]} óbitos | {percentual}%')
    print('-----------------------------------------------------------------')
    print('Informação processada e relatório salvo com sucesso!')
    conteudo += '-----------------------------------------------------------------' + '\n'
    return conteudo
    
    

#iniciando execução
#--------------------------------------------------
main()
