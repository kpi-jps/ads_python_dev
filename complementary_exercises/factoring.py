num = int(input('Entre com um número inteiro para fatorá-lo: '))
res = num
x = 2
contador = 0
while res > 1:
    if res % x == 0:
        print(int(res), ' | ', x)
        res = res / x
        contador += 1
        
        
    else:
        #print(x, '^', contador)
        x += 1
        contador = 0
#print(x, '^', contador)        
print('-----------------')
print(res)
