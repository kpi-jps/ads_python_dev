lista = []
i = 0
while i < 5:
    nome = str(input('Digite um nome de usuário ')) #não precisa usar str
    # por definição o input já define o valor de entrada como string
    # nome = input('Digite um nome de usuário')
    lista.append(nome)
    i+=1
for x in range(0,len(lista),1):
    print(lista[x])
