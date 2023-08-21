'''
Exercícios - Aula de funções
Ex5 - Faça uma função que receba quatro valores reais (faça a consistência),
referentes as notas que um aluno obteve nos bimestres. A função deve
retornar a média final desse aluno. Pesquise como arredondar a nota.
'''
###############################################
# função principal
def main():
    notas = entradaDeNotas()
    media = calcMedia(notas).replace('.', ',') # .replace('.', ',') substitui "." por ","
    print(f'Média do aluno: {media}')
    
###############################################
# funções secundárias

# cacula a média do aluno
def calcMedia(notas):
    i = 0
    soma = 0
    while i < len(notas):
        soma += notas[i]
        i += 1
    media = soma/len(notas)
    saida = '{:.2f}' # formata a saida para 2 algarismos decimais
    return saida.format(media)

# aceita a entrada de notas
def entradaDeNotas():
    print('Entre com as quatro notas do aluno:')
    notas = []
    cont_notas = 1
    while len(notas) < 4:
        nota = input(f'Entre com a nota {cont_notas} do aluno: ')
        
        if real(nota): # checa a saida da função real(n), se for True ele aceita o valor
            nota = nota.replace(',', '.') # substitui "," por ".", caso exista
            num = float(nota) # converte a string em um float
            if num >= 0 and num <= 10: # restringe valores entre 0 e 10 para as notas
                notas.append(num)
                cont_notas += 1
            else:
                print('Entre com um valor entre 0 e 10 como nota para aluno:')
        else:
           print('Entre com um valor válido como nota para aluno:')
    return notas


# confirma se o número digitado pertence ao conjunto dos reais  
def real(n): 
    if n.isdigit(): # método isdigit() checa se o a variável corresponde a digitos de 0 a 9
        check = True
    else:
        check = False
        # checando se o primeiro caracter da string é o sinal de "-"
        if n[0] == '-':
            n1 = n[1:] # define um nova string sem o sinal "-"
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
        
                
    return check
#########################################################
# iniciando execução do programa
#########################################################
main()
