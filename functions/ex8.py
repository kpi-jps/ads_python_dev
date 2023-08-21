'''
Exercícios - Aula de funções
Ex8 - Faça uma função que retorne a sequencia de Fibonacci recebendo
como parâmetro o número (faça a consistência) de termos desejado.
'''
# função principal
def main():
    n = input('Entre com um número inteiro: ')
    fibonacci(inteiroPositivo(n), n)
    
    
# funções secundárias
# checa se o número n é um inteiro positivo e retorna True se sim e False se não
def inteiroPositivo(n):
    try:
        num = int(n)
    except:
        return False 
    else:
        if num >= 0:
            return True
        else:
            return False

# gera a sequência de Fibonacci com "n" número de termos
# o parâmetro n é o número de termos 
# o parâmetro "check" é uma variável boolena
def fibonacci(check, n):
    if check == True:
        num = int(n)
        fn_2 = 0 # equivale a f(n-2)
        fn_1 = 1 # equivale a f(n-1)
        i = 0
        while i <= num:
            if i == 0:
                print(fn_2)
            elif i == 1:
                print(fn_1) 
            else:
                fn = fn_1 + fn_2
                fn_2 = fn_1
                fn_1 = fn
                print(fn)
            i += 1
            
    else:
        print('O valor de entrada não é válido!')


    
    
###############################################
# iniciando execução
###############################################
main()
