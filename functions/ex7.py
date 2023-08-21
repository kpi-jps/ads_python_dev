'''
Exercícios - Aula de funções
Ex7 - Faça uma função que calcule o fatorial de um número inteiro positivo
(faça a consistência). Transforme seus programas de consistência de
número já implementados para funções.
'''
# função principal
def main():
    n = input('Entre com um número inteiro: ')
    fatorial(inteiroPositivo(n), n)
    
# funções secundárias
# checa se o número n é um inteiro positivo e retorna True se sim e False se não
def inteiroPositivo(n):
    if n.isdigit(): # método isdigit() checa se o a variável corresponde a digitos de 0 a 9
        num = int(n)
        if num != 0:
            return True
        else:
            return False
    else:
         if n[0] == '+':
            n1 = n[1:]
            if n1.isdigit():
                num = int(n1)
                if num != 0:
                    return True
                else:
                    return False
            return False

# calcula o fatorial de um número se ele for um inteiro positivo
# imprime o resultado
# o parâmetro n é o número
# o parâmetro check é um variável boolena
def fatorial(check, n):
    if check == True:
        num = int(n)
        fatorial = 1
        i = num
        while i > 0:
            fatorial = fatorial * i 
            i -= 1
        print(f'{num}! = {fatorial}')
    else:
        print('O número dígitado não correponde a um número inteiro positivo!')

    
###############################################
# iniciando execução
###############################################
main()
