'''
Ex2. Faça uma função recursiva para encontrar a potência positiva (n>=0) de um número X.
Considere:
x^n = 1 se n=0
x^n = x * x^(n-1) se n>0
'''

def potencia(n, x):
    if n == 0:
        return 1
    else:
        return x * potencia(n-1, x)

print('----------------------------------------------------------------')
print('Calculando x^n:')
n = int(input('Entre com um número inteiro maior ou igual a zero para n: '))
x = float(input('Entre com um número real para x: '))
print(f'({x})^{n} = {potencia(n, x)}')
print('----------------------------------------------------------------')




        
