'''
Exercícios - Aula de funções
Ex1 - Elabore a função InteiroPositivo(n) que verifica se o valor de entrada é um
número inteiro positivo e retorna Verdadeiro em caso afirmativo e Falso caso
contrário.
'''
# função principal
def main():
    n = input('Entre com um número inteiro: ')
    print(inteiroPositivo(n))

# funções secundárias
def inteiroPositivo(n):
    if n.isdigit(): # método isdigit() checa se o a variável corresponde a digitos entre 0 a 9
        check = True
    else:
        check = False
    return check
###############################################
# iniciando execução
###############################################
main()
