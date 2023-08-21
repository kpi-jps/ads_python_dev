'''
Exercícios - Aula de funções
Ex3 - Elabore a função Real(n) que verifica se o valor de entrada é um número real
(positivo ou negativo) e retorna TRUE em caso afirmativo e FALSE caso
contrário.
'''
#função principal
def main():
    n = input('Entre com um número inteiro: ')
    print(real(n))

#funções secundárias
def real(n): # confirma se o número digitado pertence ao conjunto dos reais
    if n.isdigit(): # método isdigit() checa se o a variável corresponde a digitos de 0 a 9
        check = True
    else:
        check = False
        # checando se o primeiro caracter da string é o sinal de "-" ou "+"
        if n[0] == '-' or n[0] == '+':
            n1 = n[1:] # define um nova string sem o sinal "-" ou "+"
            if n1.isdigit():
                check = True
            else:
                cont = 0
                for i in range(len(n1)):
                    #trecho do código que conta o ocorrência de "." ou "," na string
                    if n1[i] == '.' or n1[i] == ',':
                        cont += 1
                    # se a contagem de "." ou "," é igual a 1, uma nova string será
                    # definida e construída com a ausencia de "." ou ","
                    if cont == 1:
                        n2 = '' # definindo string vazia
                        for i in range(len(n1)):
                            if n1[i] == '.' or n1[i] == ',':
                                # construíndo nova string sem a presença de "." ou ","
                                n2 = n2 + n1[:i]
                                n2 = n2 + n1[i+1:]
                        if n2.isdigit():
                            # checando se a nova string apresenta apenas dígitos
                            # se sim a variavem de checagem é alterada para True
                            check = True
                            print(n2)
                            print(cont)
        # checando se o primeiro caracter da string digitada é um número
        elif n[0].isdigit():
            cont = 0
            # procurando pela ocorrência de "." ou "," e contando a ocorrência
            # destes caracteres
            for i in range(len(n)):
                if n[i] == '.' or n[i] == ',':
                   cont += 1
            # se a contagem de "." ou "," é igual a 1, uma nova string será
            # definida e construída com a ausencia de "." ou ","
            if cont == 1:
                n1 = '' # definindo string vazia
                for i in range(len(n)):
                    # construíndo nova string sem a presença de "." ou ","
                    if n[i] == '.' or n[i] == ',':
                        n1 = n1 + n[:i]
                        n1 = n1 + n[i+1:]
                if n1.isdigit():
                    # checando se a nova string apresenta apenas dígitos
                    # se sim a variavem de checagem é alterada para True
                    check = True
                    print(n1)
                    print(cont)
                
    return check
#########################################################
# iniciando execução do programa
#########################################################
main()
