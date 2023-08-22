def FIB(n):
    if n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return FIB(n-1) + FIB(n-2)

n = int(input('Informe um valor inteiro positivo:'))
print(f'Fibonacci de {n} = {FIB(n)}')
