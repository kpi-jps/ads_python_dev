contatos=[]
nome = input("Nome do contato:")
while nome!="":
    pessoa =[]
    pessoa.append(nome)
    tel = input("Número de telefone ou celular:")
    pessoa.append(tel)
    contatos.append(pessoa)
    nome = input("Informe o nome de um novo contato ou digite enter para encerrar:")
print('Agenda de contatos')
for i in range(0, len(contatos), 1):
    print(contatos[i][0], ': ', contatos[i][1])
