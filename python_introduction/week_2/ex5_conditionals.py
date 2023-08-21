#Ex.5 - Aula semana 2 - Condicionais
#Crie um algoritmo para resolver equações do 2º grau.
#Considere:
#ax² + bx + c = 0 (a deve ser diferente de 0)
#delta = b²- 4 * a * c
#Caso: delta < 0, não existe raiz real
#delta = 0, existe uma raiz real: x = (-b) / (2 * a)
#delta > 0, existem duas raízes reais:
#x1 = (- b + raiz quadrada de delta) / (2 * a)
#x2 = (- b - raiz quadrada de delta) / (2 * a)
print('Resolvendo equação do segundo grau: ax² + bx + c = 0')

a = float(input('Digite um valor para o termo "a" '))
b = float(input('Digite um valor para o termo "b" '))
c = float(input('Digite um valor para o termo "c" '))

if a != 0:
    delta = b**2 - 4 * a * c
    if delta == 0:
        x = (-b) / (2 * a)
        print(f'Como delta = {delta}; a equação apresenta apenas uma raiz real: x = {x}.')
    elif delta > 0:
        x1 = (- b + delta**0.5) / (2 * a)
        x2 = (- b - delta**0.5) / (2 * a)
        print(f'delta = {delta}. Como delta > 0 a equação apresenta duas raizes reais: x1 = {x1} e x2 = {x2}.')
    else:
        print(f'delta = {delta}. Como delta < 0; a equação não apresenta raizes reais.')
            
else:
    print('O valor do termo "a" precisa ser diferente de zero!')
