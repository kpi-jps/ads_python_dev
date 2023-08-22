'''
2- O prefeito de uma pequena cidade solicitou um programa para apurar o
resultado de uma eleição para o novo prefeito do município. Suponha que
existam 5 candidatos cujos códigos de identificação são: 100, 200, 300, 400,
500. Considere a existência de um arquivo texto denominado “votos.txt” que
contém, em cada linha, o voto de um eleitor, representado pelo código de
identificação do candidato (veja no exemplo a seguir):
Arquivo votos.txt:
500
500
100
200
400
300
1050
100
12
300
57
...
 Faça um programa que leia o arquivo votos.txt, calcule e apresente:
- A quantidade de votos do candidato mais votado e o código de
identificação do candidato.
- A quantidade de votos do candidato menos votado e o código de
identificação do candidato.
- A quantidade de votos nulos (um voto nulo é um voto cujo código de
identificação é inválido).
OBS: o arquivo votos.txt pode ser gerado automaticamente ou manualmente. Se
optar por criá-lo manualmente, não esqueça de enviá-lo juntamente com o
código do programa. 

'''

######################################################################
# definindo a função principal

def main():
    print('---------------------------------------------------------')
    print('                 APURAÇÃO DE VOTOS                       ')
    print('---------------------------------------------------------')
    check = True
    while check:
        print('\n')
        entrada = input('Entre com o nome do arquivo com os votos a serem contados (digite apenas o nome sem a extensão): ')
        entrada += '.txt' # adiciona a extensão .txt ao arquivo
        if checaArquivo(entrada):
            # lista de códigos dos candidatos, onde os valores precisam ser strings
            codigos = ['100', '200', '300', '400', '500'] 
            estatisticas(codigos, entrada)
            check = selecionaOpcao()
        else:
            print('\n')
            print('O arquivo procurado não existe!')
            check = selecionaOpcao()
    
    

######################################################################
# definindo as demais funções 

# checa a existência do arquivo
# o parâmetro "arquivo" que corresponde a uma string contendo o nome
# do arquivo contendo todo o caminho e a extensão
def checaArquivo(nome_arquivo):
    # O módulo "os" fornece uma maneira simples de usar funcionalidades
    # que são dependentes de sistema operacional
    import os
    # "os.path.exists(arquivo)" checa se "arquivo" existe. Se
    # sim, a expressão retorna "True" e se não "False"
    if os.path.exists(nome_arquivo):  
        return True
    else:
        return False

def selecionaOpcao():
    print('\n')
    resposta = input('Digite "SIM" para buscar um novo arquivo ou "SAIR" para encerrar o programa: ').upper()
    # .upper já converte o valor da string resposta para "upper case". Assim tanto faz o usuário
    # digitar letras minúsculas ou maiúsculas
    while resposta != 'SIM' and resposta != 'SAIR':
        print('\n')
        print('O valor digitado é inválido!')
        print('\n')
        resposta = input('Digite "SIM" para buscar um novo arquivo ou "SAIR" para encerrar o programa: ').upper()
        print('\n')
    if resposta == 'SAIR':
        print('\n')
        print('Programa encerrado!')
        print('\n')
        return False
    else:
        return True

# calculo o total de votos, usando como parâmetro apenas
# o nome do arquivo que será lido
def totalDeVotos(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # abre o arquivo
    contador = 0 # inicia a variável de contagem de votos
    for linha in arquivo: # contando as linhas do arquivo
        # esta condição exclui a última linha que contém '\n'
        # ou até mesmo linhas com string vazias no que possam ocorrer pelo arquivo
        if linha != '' and linha != '\n': 
            contador += 1
    arquivo.close() #fechando o arquivo
    return contador

# contabiliza os votos relacionados com o código de um determinado candidato
# parâmetros: "codigo" = código de um determinado candidato
#             "nome_arquivo" = nome do arquivo que será lido
def contabilizaVotos(codigo, nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # abre o arquivo
    contador = 0 # inicia a variável de contagem de votos
    for linha in arquivo:
        linha = linha.strip() # o método ".strip()" retira o "\n" do conteúdo da linha do arquivo
        if linha == codigo: # como o conteúdo da linha é um string, ele precisa ser convertido para inteiro
            contador += 1
    arquivo.close() #fechando o arquivo
    return contador

# registra os votos contados em um dicionário, que é retornado pela função
# parâmetros: "lista_codigo" = uma lista contendo os códigos dos candidatos na forma de uma string
#             "nome_arquivo" = nome do arquivo que será lido
def registraVotos(lista_codigos, nome_arquivo):
    registro = {}
    for i in range(len(lista_codigos)):
        registro[lista_codigos[i]] = contabilizaVotos(lista_codigos[i], nome_arquivo)
    return registro
        
# calcula e apresenta o código do candidato mais votado, o do candidato menos votado e
# os votos nulos
# parâmetros: "lista_codigo" = uma lista contendo os códigos dos candidatos na forma de uma string
#             "nome_arquivo" = nome do arquivo que será lido
def estatisticas(lista_codigos, nome_arquivo):
    total_votos = totalDeVotos(nome_arquivo)
    votos_validos = 0
    registro_votos = registraVotos(lista_codigos, nome_arquivo)
    # repetição que determina a quantidade de votos válidos, que é a somatória dos votos
    # de todos os códigos válidos
    for valor in registro_votos.values():
        votos_validos += valor
    mais_votado = 0 # inicializa a número de votos do mais votado em 0
    menos_votado = votos_validos # inicializa a número de votos do menos votado igual ao número de votos válidos
    cod_mais_votado = '' # define o código mais votado como uma string vazia
    cod_menos_votado = '' # define o código menos votado como uma string vazia
    # repetição de determina o código mais votado 
    for chave in registro_votos.keys():
        if  registro_votos[chave] > mais_votado:
            mais_votado = registro_votos[chave]
            cod_mais_votado = chave   
    # repetição de determina o código menos votado
    for chave in registro_votos.keys():
        if  registro_votos[chave] < menos_votado:
            menos_votado = registro_votos[chave]
            cod_menos_votado = chave
    #calculando os votos nulo
    votos_nulos = total_votos - votos_validos
    # imprimindo os resultados
    print('\n')
    print(f'O candidato mais votado é o de código {cod_mais_votado}, com {mais_votado} votos!')
    print('\n')
    print(f'O candidato menos votado é o de código {cod_menos_votado}, com {menos_votado} votos!')
    print('\n')
    print(f'Os votos nulos somam {votos_nulos} votos!')
    print('\n')
       
######################################################################
# inicio da execução do programa

main()
    
