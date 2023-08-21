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
    saida = 'Entre com um valor numérico válido!'
    if n.isdigit():
        if n == '0':
            saida = '0'
        else:
            saida = '1'
    else:
        if n[0] == '-':
            n1 = n[1:] # gera nova string excluíndo o sinal "-"
            if n1.isdigit():
                saida = "-1"
    return saida
        
#########################################################
# iniciando execução do programa
#########################################################
main()
