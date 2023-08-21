'''
Exercícios - Aula de funções
Ex10 - Faça uma função que receba 2 listas de valores inteiros e retorne a lista
UNIÃO. (uma nova lista contendo os elementos das duas listas sem repetição - 
definição de união de conjuntos)
'''
# função principal
def main():
    print('Entre com os valores para a LISTA 1!')
    l1 = criaLista()
    print('Entre com os valores para a LISTA 2!')
    l2 = criaLista()
    print(unindoListas(l1, l2))
    
# funções secundárias
# cria a lista com valores numéricos
def criaLista():
    entrada = input('Entre com valores númericos ou precione ENTER para cessar a inserção de dados: ')
    lista = []
    while entrada != '':
        if inteiro(entrada) == True:
            lista.append(int(entrada))
        else:
            print('O valor digitado não é válido, utilize apenas números inteiros!')
        entrada = input('Entre com valores númericos ou precione ENTER para cessar a inserção de dados: ')
    return lista


# checa se o número n é um número real e retorna True se sim e False se não
def inteiro(n):
    try:
        num = int(n)
    except:
        return False 
    else:
        return True

# une duas listas
def unindoListas(lista1, lista2):
    return lista1 + lista2
     


###############################################
# iniciando execução
###############################################
main()
