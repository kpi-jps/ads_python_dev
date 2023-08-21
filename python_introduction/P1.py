# PROVA PRÁTICA ONLINE DE AP1S1 - II SEM/2020 - 21/12/2020

# JOÃO PEDRO DA SILVA - SC3012964

#DESCRIÇÃO DA PROVA

#Escreva um código Python modularizado seguindo a estrutura do programa principal e das funções,
#conforme o código a seguir, respeitando as passagens de parâmetros nas funções inclusive.
#O objetivo do programa proposto é gerenciar os filmes de uma locadora virtual. As prinicipais funções
#a serem implementadas estão definidas na função mostrarMenu().
#O programa inicializará com uma lista de Filmes (definida na função main()), que tem a seguinte estrutura:
#Filmes = [[Código, Nome, AnoLançamento, Gênero, [Ator1, Ator2,...,Atorn], PreçoLocação], 
#       ...,[Código, Nome, AnoLançamento, Gênero, [Ator1, Ator2,..., Atorn], PreçoLocação]]

#=====================================================================
#Esta função está pronta e apresenta o menu de opções para o usuário fazer a sua escolha
def mostrarMenu():
    print("\n\nLocadora de Filmes:\n")
    print("1 - Inserir novo filme")
    print("2 - Buscar um filme")
    print("3 - Remover filme")
    print("4 – Gerar relatório de filmes")
    print("5 – Buscar filmes de um ator específico")
    print("6 - Sair")

#=====================================================================
# defini esta função para buscar por código no cadastro de filmes. Ela retorna True se o código existe e False se não.
def checaCodigo(filmes, cod):
    check = False
    for i in range(len(filmes)):
        if int(cod) == filmes[i][0]:
            check = True
    return check

#=====================================================================
# defini aqui uma função para imprimir as informações sobre o filme, que usa como parâmetro o index do filme
# na lista filme, que representa o cadastro
def imprimeFilmeInfo(filmes, index):
    print(f'Código do filme: {filmes[index][0]}')
    print(f'Nome: {filmes[index][1]}')
    print(f'Ano de lançamento: {filmes[index][2]}')
    print(f'Gênero: {filmes[index][3]}')
    print(f'Atores: {filmes[index][4][0]}')
    for i in range(1,len(filmes[index][4])):
        print (f'        {filmes[index][4][i]}')
    preco = 'Preço de locação: R${:.2f}'
    print(preco.format(filmes[index][5]))
    


#=====================================================================
#QUESTÃO 1 (1.5) - Implemente aqui o código da função inserir_filme(), que receberá como parâmetro uma referência para
# a lista Filmes (definida na main()) e deverá solicitar e incluir os dados de um filme nessa lista.    
def inserir_filme(filmes):
    print("\n1 - Cadastro de novo filme\n")
    cod = input('Entre com o código do filme: ')
    while cod.isdigit() == False:
        print('O valor digitado não é válido, utilize apenas número')
        cod = input('Entre com o código do filme: ')
    if checaCodigo(filmes, cod):
        print('O cógigo digitado já esta sendo usado. Você será redirecionado ao menu para realizar a operação novamente usando outro código!')
        main() # chama a função principal para mostrar o menu novamente
    else:
        filme = []
        filme.append(int(cod))
        nome = input('Entre com o nome do filme: ')
        filme.append(nome)
        anoLancamento = input('Entre com o ano de lançamento: ')
        while anoLancamento.isdigit() == False:
            print('O ano de lançamento precisa ser um número!')
            anoLancamento = input('Entre com o ano de lançamento: ')
        filme.append(int(anoLancamento))
        genero = input('Entre com o Gênero do filme: ')
        lista_atores = []
        ator = input('Entre com o nome de um ator do filme: ')
        lista_atores.append(ator)
        check = 0
        while check == 0:
            ator = input('Continue entrando com nome de atores ou digite 0 para parar a inserção de nomes: ')
            if ator == '0':
                check = 1 # váriavel finaliza a inserção de nomes
        filme.append(lista_atores)
        check = True
        # este bloco ignora quando for digitado valores invalidos para a variavel preço
        while check:
            try:
                preco = float(input('Entre com o preço para a locação do filme: '))
            except:
                print('Entre com um valor válido para o preço')
            else:
                check = False
        filme.append(preco)
        filmes.append(filme) # adiciona a o novo filme ao cadastro
        
                       
        
#=====================================================================
#QUESTÃO 2 (1.5) - Implemente o código da função buscar_filme(), que receberá como parâmetro uma referência para
# a lista Filmes e o código do filme a ser procurado. A função deverá retornar o índice da posição
# do filme na lista, se ele estiver cadastrado. Caso o filme não seja encontrado, a função deverá retornar -1.
#Os dados do filme procurado deverão ser impressos na função main(). Caso o filme não tenha sido localizado,
# a função main() deverá imprimir a mensagem informando que o filme não está cadastrado.
def buscar_filme(filmes, codigo_filme):    
    if checaCodigo(filmes, codigo_filme):
        for i in range(len(filmes)):
            if filmes[i][0] == codigo_filme:
                return i
    else:
         return -1
    
#=====================================================================
#QUESTÃO 3 (1.5) - Implemente o código da função remover_filme(), que receberá como parâmetro uma referência para
# a lista Filmes e o código do filme a ser removido. Essa função deverá chamar a função buscar_filme(), para
# verificar se o mesmo existe na lista e recuperar a sua posição para remoção.
#A função deverá imprimir uma mensagem informando que o filme foi removido com sucesso.
#Caso o filme não tenha sido encontrado, deverá imprimir a mensagem informando que o filme não está cadastrado.
def remover_filme(filmes, codigo_filme):    
    print("\n3 - Remoção de um filme com todas suas informações\n")
    index = buscar_filme(filmes, codigo_filme)
    if index == -1:
        print('O filme procurado não está cadastrado')
    else:
        del filmes[index]
        print('Filme removido com sucesso!')
        
        
    
#=====================================================================
#QUESTÃO 4 (2.0) - Implemente o código da função relatorio_filmes(), que receberá como parâmetro uma referência para
# a lista Filmes e imprimirá os dados de cada filme de acordo com o formato a seguir:
    
#**************************Relatório de Filmes**************************
    #Código do filme: 1
    #Nome: Homem Aranha: Longe de Casa
    #Ano de lançamento: 2019
    #Gênero: Ação
    #Autores: Tom Holland
    #         Jake Gyllenhaal
    #         Zendaya
    #Preço de locação: R$20.00

    #+++++++++++++++++++++++++++++++++++++
    #Código do filme: 2
    #Nome: Vingadores: Ultimato
    #...
    
def relatorio_filmes(filmes):
    print("\n*************************Relatório de Filmes**************************\n")
    for index in range(len(filmes)):
        imprimeFilmeInfo(filmes, index)
        print('+++++++++++++++++++++++++++++++++++++')

    
#=====================================================================
#QUESTÃO 5 (2.0) - Implemente o código da função buscar_filmes_ator_especifico(), que receberá como parâmetro uma referência para
# a lista Filmes e o nome de um ator. Essa função deverá buscar e apresentar o nome e o ano de lançamento de todos os filmes
#que tenham a participação de um ator específico fornecido pelo usuário.
#Caso não exista filmes com a participação do ator desejado, a função deverá imprimir uma mensagem informando que não há
#filmes com esse ator cadastrado.
def buscar_filmes_ator_especifico(filmes, nome_ator):    
    print("\n5 - Busca por filmes de um ator específico\n")
    lista_filmes = []
    
    for i in range(len(filmes)):
        check = False
        for j in range(len(filmes[i][4])):
            
            if nome_ator == filmes[i][4][j]:
                check = True
        if check:
            lista_filmes.append((filmes[i][1] + ' (' + str(filmes[i][2]) + ')'))
            
    if len(lista_filmes) == 0:
        print('Não há filmes com esse ator no cadastro!')
    else:
        print(f'Filmes estrelados por {nome_ator}')
        for i in range(len(lista_filmes)):
            print(lista_filmes[i])
                
       

        
    
#=====================================================================

#Função principal que usa as funções definidas anteriormente
# QUESTÃO 6 (1.5) - Inclua aqui as chamadas das funções respeitando os parâmetros e tratando corretamente
# o valor de retorno (quando houver).
def main():
    Filmes = [[1,"Homem Aranha: Longe de Casa", 2019, "Ação", ["Tom Holland", "Jake Gyllenhaal", "Zendaya"], 20.00],[2,"Vingadores: Ultimato", 2019, "Ação", ["Mark Ruffalo", "Robert Downey Jr.", "Tom Holland", "Scarlett Johansson"], 25.00 ], 
[3,"Capitão América: guerra civil", 2016, "Ação", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson"],15.00]]
     
    menu=True
    while menu:
        mostrarMenu()
        opc=input("\nEscolha uma opção: ")

        # em algumas opções fiz algumas alterações para lidar com o erro de entrada para algumas variáveis
        # eu usei um try. Espero que não se importe!
        if opc == '1':
            inserir_filme(Filmes)
            
        elif opc == '2':
            check = True
            while check:
                try:
                    codigo = int(input("Digite o código do filme que deseja consultar: "))
                except:
                    print('Entre com um valor válido!')
                else:
                    check = False		
            busca = buscar_filme(Filmes, codigo)
            if busca == -1:
                print('O filme procurado não está cadastrado')
            else:
                imprimeFilmeInfo(Filmes, busca)
                
           
        elif opc == '3':
            check = True
            while check:
                try:
                    codigo = int(input("Digite o código do filme que deseja remover: "))
                except:
                    print('Entre com um valor válido!')
                else:
                    check = False
            remover_filme(Filmes, codigo)
                      
                      
        elif opc == '4':
            relatorio_filmes(Filmes)

        elif opc == '5':
            ator = input("Digite o nome do ator que deseja recuperar os filmes do qual ele participou: ")
            buscar_filmes_ator_especifico(Filmes, ator)
            
            
        else:
            print("\nTerminando a execução do programa!!!")
            menu=False

#===================================================================================	

########################## PROGRAMA PRINCIPAL ######################################
main()
