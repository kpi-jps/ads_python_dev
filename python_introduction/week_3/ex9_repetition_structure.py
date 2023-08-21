#Ex.9 - Semana 3 - Estrutura de repetição
#Faça um programa que receba um número N fornecido pelo
#usuário e mostre os N termos da série a seguir. Depois, imprima a
#soma total da série:

#s = 1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + N/M

#analisando a série é possível concluir que a relação entre N e M é dada por:
#N(n)/M(n) = N(n)/(N(n-1) + n)
#além disso, N(n) = N(n-1) + n

#N 
N = int(input('Entre com um valor de número inteiro maior que 0: '))
Sn = 1 #variável que representa N(n)
Sn1 = 1 #variável que representa N(n-1)
M = 0 #variável que representa M
n = 1 #variável de controle para o laço
soma = 1#variável que soma os termos da série
if N <= 0:
    print('O número digitado precisa ser maior que 0')
else:
    print('Termos da série:')
    print('S(n) = 1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + N/M para, n =',N)
    print('-----------------------------------------------------------')
    while n <= N:
        if n == 1:
            print(f'S({n}) = {Sn}')
        else:
            Sn = Sn1 + 1
            M = Sn1 + n
            soma = soma + (Sn/M)
            print(f'S({n}) = {Sn}/{M}')
            Sn1 = Sn
        n = n + 1
print(f'S = {soma}')    
        
