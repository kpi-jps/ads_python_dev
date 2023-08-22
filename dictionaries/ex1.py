'''
Exercícios sobre Dicionário
Ex1.A seguinte tabela contém tradução de algumas palavras
em inglês para a língua dos piratas. Escreva um programa
que pergunta ao usuário uma frase em inglês e imprime a
tradução da frase para a língua dos piratas.

------------------------------
Tabela de palavras
------------------------------
sir - matey
hotel - fleabag inn
student - swabbie
boy - matey
madam - proud beauty
professor - foul blaggart
restaurant - galley
your - yer
excuse - arr
students - swabbies
are - be
lawyer - foul blaggart
the - th'
restroom - head
my - me
hello - avast
is - be
man - matey
------------------------------

'''
# definindo a função principal
def main():
    dic_ing_pir = {
        'sir':'matey',
        'hotel':'fleabag inn',
        'student':'swabbie',
        'boy':'matey',
        'madam':'proud beauty',
        'professor':'foul blaggart',
        'restaurant':'galley',
        'your':'yer',
        'excuse':'arr',
        'students':'swabbies',
        'are':'be',
        'lawyer':'foul blaggart',
        'the':"th'",
        'restroom':'head',
        'my':'me',
        'hello':'avast',
        'is':'be',
        'man':'matey'
        }
    
    menu(dic_ing_pir)

    

# definindo funções secundárias

# cria menu com opções
def menu(dicionario):
    print('\n')
    print('#####################################')
    print('###### Tradutor inglês/Pirata #######')
    print('############## Opções ###############')
    print('\n')
    print('[1] - Lista termos com tradução')
    print('[2] - Traduz termo ou frase')
    print('\n')
    print('#####################################')
    print('\n')
    opcao = input('Entre com o valor da opção desejada: ')
    while opcao != '1' and opcao != '2':
        print('\n')
        print('O valor digitado como opção não é válido!')
        print('\n')
        opcao = input('Entre com o valor da opção desejada: ')
        print('\n')
    if opcao == '1':
        imprimePalavras(dicionario)
    elif opcao == '2':
        traduzir(dicionario)

# imprime as chaves dos dicionários
# como parâmetro usa o dicionário
def imprimePalavras(dicionario):
    string = '|'
    for chave in dicionario.keys():
        string = string + chave + '|'
    print('\n')
    print('As palavras em inglês do dicionário são:')
    print('\n')
    print(string)
    menu(dicionario)
    
# checa se a chave (palavra em inglês) existe no dicionário
# os parâmetro são o prórpio "dicionário" e um valor de "entrada" que é uma string
# função retorna um booleano (True se o termo estiver contido no dicionário e False se não)
def checaChave(dicionario,string_de_entrada):
    check = False
    for chave in dicionario.keys():
        if chave == string_de_entrada:
            check = True
    return check

# cria uma lista com os termos a serem traduzidos
# o parâmetro "entrada" corresponde a uma string
def listaTermos(entrada):
    lista_termos = []
    termo = ''
    for caracter in range(len(entrada)):
        # caracteres que definem o final de um termo
        if entrada[caracter] == ' ' or entrada[caracter] == ',' or entrada[caracter] == '.' or entrada[caracter] == '!' or entrada[caracter] == '?':
            lista_termos.append(termo)
            lista_termos.append(entrada[caracter])
            termo = '' # deixa como vazio o termo para receber novos caracteres
        # consideração necessária para identificar apenas um termo ou termo final de uma frase
        elif caracter == (len(entrada) - 1):
            termo = termo = termo + entrada[caracter]
            lista_termos.append(termo)
        else:
            termo = termo + entrada[caracter]
    return lista_termos      

        
# traduz os termos usando como banco de dados o dicionário, usado como parâmetro da função
def traduzir(dicionario):
    print('\n')
    frase = input('Entre com uma frase ou termo para ser traduzido: ').lower()
    lista_termos = listaTermos(frase)
    termos_traduzido = ''
    for termo in range(len(lista_termos)):
        if checaChave(dicionario,lista_termos[termo]):
            termos_traduzido +=  dicionario.get(lista_termos[termo])
        # caracteres que definem o final de um termo precisam seer adiconados a termo traduzido
        elif lista_termos[termo] == ' ' or lista_termos[termo] == ',' or lista_termos[termo] == '.' or lista_termos[termo] == '!' or lista_termos[termo] == '?':
            termos_traduzido += lista_termos[termo]
        else:
            termos_traduzido += '*' + lista_termos[termo] + '*' 
    print('\n')
    print(termos_traduzido)
    print('\n')
    print('Obs: Termos marcados com * não apresentam tradução!')
    menu(dicionario)

            

# execução do programa
main()
