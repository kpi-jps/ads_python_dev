#Ex.3 - Semana 3 - Estrutura de repetição
#Faça um programa para mostrar as tabuadas de todos os números
#de 1 a 10.

x = 1
while x <= 10:
    print('------------------------')
    print('Tabuada do ',x)
    print('------------------------')
    y = 1
    while y <= 10:
        res = x * y
        print(x,' x ', y, ' = ', res)
        y = y + 1
    x = x + 1
      
