#Ex.7 - Semana 3 - Estrutura de repetição
#Faça um programa que mostre os 8 primeiros termos da
#sequência de Fibonacci. Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

#Em Fibonacci o termo F(n) = F(n-1) + F(n-2)


fn = 0 #corresponde ao termo F(n), para n > 3
fn1 = 1 #corresponde ao termo F(n-1), para n > 3
fn2 = 1 #corresponde ao termo F(n-2), para n > 3
f = 0 #corresponde ao termo F(n), para n <= 3
for x in range(1, 9, 1):
    if x == 1:
        print (f)
        f += 1
    elif x <= 3:
        print (f)   
    else:
        fn = fn1 + fn2
        print(fn)
        fn2 = fn1
        fn1 = fn
        
        
    
