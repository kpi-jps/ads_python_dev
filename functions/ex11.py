'''
Exercícios - Aula de funções
Ex11 - Faça uma função que receba 2 listas de valores inteiros e retorne a lista
INTERSECÇÃO (elementos idênticos que pertencem a ambas as listas - definição
usada em conjuntos)
'''
# função principal
def main():
    print('Entre com os valores para a LISTA 1!')
    l1 = criaLista()
    print('Entre com os valores para a LISTA 2!')
    l2 = criaLista()
    print(interseccaoListas(l1, l2))
    
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

# faz o conjunto intersecção de duas listas
def interseccaoListas(lista1, lista2):
    lista_interseccao = []
    for i in lista1:
        if i in lista2 and i not in lista_interseccao:
            lista_interseccao.append(i)
    for i in lista2:
        if i in lista1 and i not in lista_interseccao:
            lista_interseccao.append(i)
    return lista_interseccao   
     


###############################################
# iniciando execução
###############################################
main()
