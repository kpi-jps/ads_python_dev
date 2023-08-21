#Ex.5 - Crie um programa que leia inicialmente uma sequencia de N números
#inteiros. Depois, o programa deve gerar e mostre 2 novas listas a
#partir da primeira: uma sem repetição de elementos e outra com os
#elementos que se repetem na lista original.

N = int(input('Entre com a quantidades de número para a sequencia: '))
seq = []
l1 = [] #lista de números não repetidos
l2 = [] #lista de números repetidos
for i in range(0, N, 1):
    num = int(input('Digite um número inteiro: '))
    seq.append(num)

for j in range(0, len(seq), 1):
    
    cont = 0 #variável que conta a repetição do elemento, iniciada em 0
    
    
        
    for k in range(0, len(seq), 1):        
        if seq[j] == seq[k]:
            cont += 1
        
    if cont >= 2:
        #para que o elemento se repita a variável "cont" tem que ser
        #maior ou igual a 2, pois pelo menos uma vez o elemento que não
        #se repete é contado pela estrutura de repetição
        l2.append(seq[j])
    else:
        l1.append(seq[j])
    
            
print('A sequência de números digitados é ',seq)
print('A sequência de números que não se repetem é ',l1)
print('A sequência com os números que se repetem é ',l2)

#Nota, refazer o exercício usando o operador de pertinência 'in'


