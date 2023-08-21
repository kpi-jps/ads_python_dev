'''
Exercícios - Aula de funções
Ex13 - Faça uma função que receba 2 listas de valores inteiros, o modo de
saída (U:união, I:intersecção, D:diferença) e retorne a lista resultante.
'''
# função principal
def main():
    print('Entre com os valores para a LISTA 1!')
    l1 = criaLista()
    print('Entre com os valores para a LISTA 2!')
    l2 = criaLista()
    print(operacao(l1, l2))
    
    
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

# faz o conjunto união de duas listas
def uneListas(lista1, lista2):
    lista_concatenada = lista1 + lista2
    lista_uniao = []
    for i in lista_concatenada:
        if i not in lista_uniao:
            lista_uniao.append(i)
    return lista_uniao

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

# faz o conjunto diferença entre duas lista (lista1 - lista2)
def diferecaListas(lista1, lista2):
    lista_diferenca = []
    for i in lista1:
        if i not in lista2:
            lista_diferenca.append(i)
    return lista_diferenca

# executa uma operação de acordo com a escolha do usuário

def operacao(lista1, lista2):
    print('Digite um valor para operação desejada:')
    print('OP = U - (união entre LISTA 1 e LISTA 2)')
    print('OP = D - (diferença entre LISTA 1 e LISTA 2)')
    print('OP = I - (Intersecção entre LISTA 1 e LISTA 2)')
    print('\n')
    OP = input('Digite comando para operação desejada: ').upper()
    # OP = D, para diferença; OP = U, para união e OP = I, para intersecção)
    while OP != 'U' and OP != 'D' and OP != 'I':
        print('O valor digitado para a seleção da operação é inválido!')
        print('Digite um valor para operação desejada:')
        print('OP = U - (união entre LISTA 1 e LISTA 2)')
        print('OP = D - (diferença entre LISTA 1 e LISTA 2)')
        print('OP = I - (Intersecção entre LISTA 1 e LISTA 2)')
        print('\n')
        OP = input('Digite comando para operação desejada: ').upper()
    if OP == 'U':
        return uneListas(lista1, lista2)
    elif OP == 'D':
        return diferecaListas(lista1, lista2)
    elif OP == 'I':
        return interseccaoListas(lista1, lista2)
      

###############################################
# iniciando execução
###############################################
main()
