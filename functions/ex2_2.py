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
    try:
        num = int(n)
    except:
        print('Valor de entrada não válido!')
        print('- entre com valores numéricos apenas;')
        print('- sinais de "+" ou "-" também são permitidos;')
                return False
    else:
        return True
    
###############################################
# iniciando execução
###############################################
main()
