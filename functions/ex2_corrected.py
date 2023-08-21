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
        num = int(n)
        if num != 0:
            return True
        else:
            return False
    else:
        if n[0] == '-' or n[0] == '+':
            n1 = n[1:]
            if n1.isdigit():
                num = int(n1)
                if num != 0:
                    return True
                else:
                    return False
        return False
###############################################
# iniciando execução
###############################################
main()
