'''
Exercícios sobre Dicionário
Ex1.Elabore um programa para armazenar uma agenda de telefones em um
dicionário. Cada pessoa pode ter um ou mais telefones e a chave do
dicionário é o nome da pessoa. O programa deve ter as seguintes
funções:
a) incluirNovoNome() – essa função acrescenta um novo nome na
agenda, com um ou mais telefones. Ela deve receber como argumentos o
nome e os telefones;
b) incluirTelefone() – essa função acrescenta um telefone em um nome
existente na agenda. Caso o nome não exista na agenda, você deve
perguntar se a pessoa deseja incluí-lo. Caso a resposta seja afirmativa,
use a função anterior para incluir o novo nome;
c) excluirTelefone() – essa função exclui um telefone de uma pessoa que
já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser
excluída da agenda;
d)excluirNome() – essa função exclui uma pessoa da agenda.
consultarTelefone – essa função retorna os telefones de uma pessoa na
agenda.

'''

#####################################################################
# definindo a função principal
#####################################################################

def main():
    agenda = {
        # valores de exemplo
        'JOÃO PEDRO' : [
            '16988199007',
            '16988199006'
            ]
        }
    print('################################################')
    print('############ AGENDA DE TELEFONES ###############')
    print('################################################')
    menu(agenda)
    
#####################################################################    
# definindo funções secundárias
#####################################################################

# cria o menu do programa
# o parâmetro "dados" corresponde ao dicionário que contem os dados da agenda
def menu(dados):
    print('\n')
    print('############### MENU DE OPÇÔES #################')
    print('\n')
    print('------------ [1] INCLUIR NOVO NOME -------------')
    print('------------- [2] INCLUIR TELEFONE -------------')
    print('------------- [3] EXCLUIR TELEFONE -------------')
    print('------------ [4] CONSULTAR TELEFONE ------------')
    print('\n')
    print('#################################################')
    print('\n')
    opcao = input('Entre com o valor númerico da opção desejada: ')
    print('\n')
    while validarEscolha(opcao, 5) == False:
        opcao = input('Entre com o valor númerico da opção desejada: ')
        print('\n')
    contato = input('Entre com o nome para um contato: ').upper()
    print('\n')
    if opcao == '1':
        incluirNovoNome(contato, dados)
    elif opcao == '2':
        incluirTelefone(contato, dados)
    elif opcao == '3':
        excluirTelefone(contato, dados)
    elif opcao == '4':
        consultarTelefone(contato, dados)
    
# valida a entrada das escolhas do menu
# o parâmetro "entrada" é o dado a ser validado e deve ser uma string
# o prâmetro "limite" é um inteiro equivalente ao maior número
# correspondete as opções disponíveis no menu 
def validarEscolha(entrada, limite):
    if entrada.isdigit():
        num = int(entrada)
        if num > 0 and num <= limite:
            return True
        else:
            return False
    else:
        return False       

# inclui novo nome na agenda usando como parâmetro uma string que corresponde ao nome de uma pessoa
def incluirNovoNome(nome, dados):
    # condicional que checa se o nome do contato está presente no cadastro
    if nome in dados:
        print('O nome digitado já consta na agenda!')
        print('\n')
        menu(dados)
    else:
        num_telefones = input('Entre com a quantidade de números de telefone que serão armazenados ou com "0" para voltar ao menu: ')
        print('\n')
        while num_telefones.isdigit() == False:
            num_telefones = input('Entre com a quantidade de números de telefone que serão armazenados ou com "0" para voltar ao menu: ')
            print('\n')
        if num_telefones != '0':
            telefones = []
            for i in range(int(num_telefones)):
                telefone = input(f'Digite o número do telefone {i + 1} ou apenas "0" para retornar ao menu: ')
                print('\n')
                while telefone.isdigit() == False:
                    print('Apenas números são permitidos!')
                    print('\n')
                    telefone = input(f'Digite o número do telefone {i + 1} ou apenas "0" para retornar ao menu: ')
                    print('\n')
                if telefone != '0':
                    telefones.append(telefone)   
                else:
                    menu(dados)
            dados[nome] = telefones
            menu(dados)
            
        else:
            menu(dados)

# inclui número de telefone a um cadastro existente
# se o nome não consta no cadastro, permite a inclusão do mesmo e seus telefones
# parâmetro "nome" é uma string que corresponde a um nome para busca e inserção na agenda
def incluirTelefone(nome, dados):
    if nome in dados:
        telefone = input(f'Entre com um número de telefone pa o contato {nome}: ')
        print('\n')
        while telefone.isdigit() == False:
            telefone = input(f'Entre com um número de telefone pa o contato {nome}: ')
            print('\n')
        dados.get(nome).append(telefone)
        menu(dados)
    else:
        opcao = input(f'O nome {nome} não consta na lista, pressione "2" para adiconá-lo ou "1" para voltar ao menu! ')
        print('\n')
        while validarEscolha(opcao, 2) == False:
            opcao = input(f'O nome {nome} não consta na lista, pressione "2" para adiconá-lo ou "1" para voltar ao menu! ')
            print('\n')
        if opcao == '1':
            menu(dados)
        elif opcao == '2':
            incluirNovoNome(nome, dados)


# exclui número de telefone a um cadastro existente
def excluirTelefone(nome, dados): 
    if nome in dados:
        telefones = dados.get(nome)
        cont = len(telefones) # variável usada para checar o número de telefones de um nome cadastrado
        print(f'O contato {nome} tem {cont} telefone(s)')
        print('\n')
        i = cont - 1
        while i >= 0:
            opcao = input(f'Digite "2" para deletar o telefone {telefones[i]} ou "1" para não deletar: ')
            print('\n')
            while validarEscolha(opcao, 2) == False:
                opcao = input(f'Digite "2" para deletar o telefone {telefones[i]}  ou "1" para não deletar: ')
                print('\n')
            if opcao == '2':
                if cont == 1:
                    del dados[nome]   
                else:
                    del telefones[i] 
                cont -= 1   
                i -= 1
            elif opcao == '1':
                i -= 1  
        menu(dados)
                
# consulta os telefones de um nome cadastrado
def consultarTelefone(nome, dados):
    if nome in dados:
        print('\n')
        print('-----------------------------------')
        print(f'Contato: {nome}')
        print('-----------------------------------')
        for telefone in range(len(dados.get(nome))):
            print(f'Tel({telefone + 1}): {dados.get(nome)[telefone]}')
        print('-----------------------------------')
        menu(dados)
    else:
        print(f'O contato {nome} não consta na agenda')
        menu(dados)
            
#####################################################################
# execução do programa
#####################################################################

main()
