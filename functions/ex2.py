'''
Exercícios - Aula de funções
Ex2 - Elabore a função Inteiro(n) que verifica se o valor de entrada é um número
inteiro (positivo ou negativo) e retorna Verdadeiro em caso afirmativo e Falso
caso contrário.
'''
# função principal
def main():
    n = input('Entre com um número inteiro: ')
    print(inteiro(n))

# funções secundárias
def inteiro(n):
    if n.isdigit(): # método isdigit() checa se o a variável corresponde a digitos de 0 a 9
        check = True
    else:
        check = False
        if n[0] == '-' and n[1] != '0': # esta condição exclui -0 e - seguido de letras
            n1 = n[1:]
            if n1.isdigit():
                check = True
    return check

###############################################
# iniciando execução
###############################################
main()
