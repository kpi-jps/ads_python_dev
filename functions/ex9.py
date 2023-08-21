'''
Exercícios - Aula de funções
Ex9 - Faça uma função que receba uma lista como parâmetro e retorne sua
soma.
'''
# função principal
def main():
    print('A soma dos valores digitados é:', somaLista(criaLista()))
    
# funções secundárias
# cria a lista com valores numéricos
def criaLista():
    entrada = input('Entre com valores númericos ou precione ENTER para cessar a inserção de dados: ')
    lista = []
    while entrada != '':
        if real(entrada) == True:
            lista.append(float(entrada))
        else:
            print('O valor digitado não é válido, utilize apenas números!')
        entrada = input('Entre com valores númericos ou precione ENTER para cessar a inserção de dados: ')
    return lista


# checa se o número n é um número real e retorna True se sim e False se não
def real(n):
    try:
        num = float(n)
    except:
        return False 
    else:
        return True

# soma os elementos da lista
def somaLista(lista):
    soma = 0
    for i in range(len(lista)):
        soma = soma + lista[i]
    return soma
        


###############################################
# iniciando execução
###############################################
main()
