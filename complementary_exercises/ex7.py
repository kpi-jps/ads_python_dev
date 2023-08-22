'''
Exercícios Estrutura de Repetição - Extra
Ex7.Escreva um programa que apresente os 5 primeiros números perfeitos. Um
número perfeito é aquele que é igual a soma dos seus divisores (por exemplo, 6 =
1+2+3 e 28= 1+2+4+7+14).
'''
#esta rotina demora muito para resolver o problema, usando fórmula é mais rápido

num = 1
i = 0
while i < 4:
    soma = 0
    div = 1
    cont = 0
    while div < num:
        if num % div == 0:
            soma += div
            
        div += 1
        
    if soma == num:
        print(soma)
        num += 1
        i += 1
    else:
        num += 1
        
print('Fim do programa')   

#Usando formula: Para um número perfeito (2^(n-1)*(2^n - 1)

'''
i = 1
while i <= 5:
    num = (2**(i-1))*(2**i-1)
    print(num)
    i += 1
'''

