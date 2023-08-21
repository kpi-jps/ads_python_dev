'''
Exercícios - Aula de funções
Ex3 - Elabore a função Real(n) que verifica se o valor de entrada é um número real
(positivo ou negativo) e retorna TRUE em caso afirmativo e FALSE caso
contrário.
'''
#função principal
def main():
    n = input('Entre com um número inteiro: ')
    print(Real(n))

#funções secundárias
def Real(n): # confirma se o número digitado pertence ao conjunto dos reais
    try:
        num = float(n)
    except:
        print('Valor de entrada não válido!')
        print('- entre com valores numéricos apenas;')
        print('- se for usar separador decimal, use "." e não ",";')
        print('- sinais de "+" ou "-" também são permitidos;')
        print('- usar o "e" para valores exponenciais também é permitido.')
        return False
    else:
        return True
        
   
#########################################################
# iniciando execução do programa
#########################################################
main()
