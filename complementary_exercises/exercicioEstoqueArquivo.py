def exibirMenu():
    print("Menu")
    print("1 - cadastrar produto novo")
    print("2 - listar produtos cadastrados")
    print("3 - exibir o nome e fornecedor do produto mais caro")
    print("4 - o preço médio dos produtos de cada fornecedor")
    print("5 - informar o valor total do estoque")
    print("6 - criar a Lista de fornecedores.")
#essa lista de fornecedores deve conter todos os fornecedores de produtos
# caso um novo produto seja inserido, deve-se verificar se ele está
# nesta lista. Caso esteja, o cadastro deve prosseguir. Do contrário,
# o cadastro é cancelado
    print("7 - informar a quantidade em estoque de produtos de cada fornecedor")
    print("8 - exibir a quantidade em estoque do produto mais barato")
    print("9 - Atualizar preço dos produtos")
#deve ser solicitado ao usuário o valor de desconto ou acrescimo nos preços.
#a partir do valor fornecido, o preço de todos os produtos deve ser atualizado
    print("10 - Excluir um produto do estoque a partir do nome. Excluir no arquivo e em memória. ")

#funcao para carregar dados da memoria
def carregarDados(nomeArq,mat):
    arquivo = open(nomeArq,'r')
    arquivo.readline()
    contador = 0
    for linha in arquivo:
        linha.replace("\n", "")
        lista = linha.split(";")
        #print(lista)
        mat.append(lista)
        contador = contador + 1
    arquivo.close()
    return contador

def cadastrarProduto(nomeArq):
#produto;preco;fornecedor;qddEstoque
    produto = input("Digite o nome do produto: ")
    preco = input("Digite o preco : ")
    fornecedor = input("digite o fornecedor: ")
    qtddEstoque = input("digite a qtdd em estoque: ")
    linha = produto+";"+preco+";"+fornecedor+";"+qtddEstoque+"\n"
    arquivo = open(nomeArq,'a')
    arquivo.write(linha)
    arquivo.close()
    
    
#principal
opcao  = -1
matriz = []
qtddProdutos = 0
nomeArquivo = 'estoque.csv'
qtddProdutos = carregarDados(nomeArquivo,matriz)
if qtddProdutos == 0:
    print("Nenhum produto cadastrado em arquivo!")
else:
    print("Qtdd de Produtos Cadastrados: " + str(qtddProdutos))
while opcao !=0:
    exibirMenu()
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        cadastrarProduto(nomeArquivo)
