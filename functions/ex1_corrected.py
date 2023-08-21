'''
Exercícios - Aula de funções
Ex1 - Elabore a função InteiroPositivo(n) que verifica se o valor de entrada é um
número inteiro positivo e retorna Verdadeiro em caso afirmativo e Falso caso
contrário.
'''
# função principal
def main():
    n = input('Entre com um número inteiro: ')
    check = inteiroPositivo(n)
    if check:
        print('É um número inteiro positivo!')
    else:
        print('Não é um número inteiro positivo!')

# funções secundárias
def inteiroPositivo(n):
    if n.isdigit(): # método isdigit() checa se o a variável corresponde a digitos entre 0 a 9
        num = int(n) # converte n para inteiro para checagem se n > 0
        if num > 0:
            return True
    return False
###############################################
# iniciando execução
###############################################
main()
