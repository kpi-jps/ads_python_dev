'''
Exercícios - Aula de funções
Ex4 - Crie uma função que receba como parâmetro um número inteiro. A função
deve retornar um número inteiro, conforme a seguir:
a) Retornar 1 se o número recebido é positivo
b) Retornar -1 se o número recebido é negativo
c) Retornar 0 se o número recebido é zero
'''
#função principal
def main():
    n = input('Entre com um número inteiro: ')
    print(inteiro(n))

#funções secundárias
def inteiro(n):
    try:
        num = int(n)
    except:
        print('Valor de entrada não válido!')
        print('- entre com valores numéricos apenas;')
        print('- sinais de "+" ou "-" também são permitidos;') 
    else:
        if num > 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1
              
        
#########################################################
# iniciando execução do programa
#########################################################
main()
