#Ex.2 - Gere uma lista de contendo os múltiplos de 3 entre 1 e 150.
num = 1
lista = []
while num <= 150:
    if num % 3 == 0: #checa se num é múltiplo de 3
       lista.append(num)
    num += 1

print('A lista dos multiplos de 3 entre 1 e 150 é ',lista)

