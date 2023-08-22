def FAT(n):
    if n == 0:
        return 1
    else:
        return n * FAT(n-1)

n = int(input('Informe um valor inteiro positivo:'))
print(f'Fatorial de {n} = {FAT(n)}')
