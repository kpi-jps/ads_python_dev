'''
Exercícios - Aula de funções
Ex12 - Faça uma função que receba 2 listas de valores inteiros e retorne a lista
DIFERENÇA (se l1-l2 a nova lista será formadas pelos elementos de l1 menos os
que se repetem em l2, ou seja, menos a intersecção - definição usada em conjuntos)
'''
# função principal
def main():
    print('Entre com os valores para a LISTA 1!')
    l1 = criaLista()
    print('Entre com os valores para a LISTA 2!')
    l2 = criaLista()
    print(diferecaListas(l1, l2))
    
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


# checa se o número n é um número inteiro e retorna True se sim e False se não
def inteiro(n):
    try:
        num = int(n)
    except:
        return False 
    else:
        return True

# faz o conjunto diferença entre duas lista (lista1 - lista2)
def diferecaListas(lista1, lista2):
    lista_diferenca = []
    for i in lista1:
        if i not in lista2:
            lista_diferenca.append(i)
    return lista_diferenca
    
    
     


###############################################
# iniciando execução
###############################################
main()
