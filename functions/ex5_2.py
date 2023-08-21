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
    try:
        num = float(n)
    except:
        return False
    else:
        return True
    
#########################################################
# iniciando execução do programa
#########################################################
main()
