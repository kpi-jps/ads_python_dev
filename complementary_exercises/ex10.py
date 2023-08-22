'''
Exercícios Estrutura de Repetição - Extra
Ex10.Faça um programa que calcule e escreva a soma dos 20 primeiros
termos da série:
100/0! - 99/1! + 98/2! + 97/3! + ...
'''

i = 1
soma = 0
while i <= 20:
    j = i - 1
    
    if i == 1:
        termo = 100
        
        dividendo = 100
        divisor = 1
        
    else:
        dividendo -= 1
        divisor = j
        while j > 0:
            if j > 1:
                divisor = divisor * (divisor-1)
            j -= 1
        termo = dividendo / divisor
        
    
    print('termo', i, ':',termo)
    
    soma += termo
    i += 1
print('Soma dos termos:', soma)
