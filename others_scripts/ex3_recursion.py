'''
Faça uma função recursiva para calcular o MDC entre dois números x e y.
Considere:
mdc(x; y) = y, se x >= y e x mod y = 0
mdc(x; y) = mdc(y; x), se x < y
mdc(x; y) = mdc(y; x mod y), caso
contrário
'''


def mdc(x, y):
    if x >= y and  x % y == 0:
        return y
    elif x < y:
        return mdc (y,x)
    else:
        return mdc(y, x % y)
    
print('--------------------------------------------')    
print('Calculando mdc(x,y):')
a = int(input('Entre com o valor inteiro para x: '))
b = int(input('Entre com o valor inteiro para y: '))
print(f'mdc(x,y) = {mdc(a,b)}')
print('--------------------------------------------')
