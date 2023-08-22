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
# verifica se uma entrada do usuário é um determinado tipo de número,
# retornando "True" se sim e "False" se não.
# parâmetros:
# num = número a ser validado (string)
# tipo = tipo de número (string; valores: "int", "float")
# intervalo = intervalo coberto pelo tipo de número (string;
# valores:
# "-0+" para número positivos, 0 e números negativos;
# "0+" para número positivos e zero;
# "+" para número positivos;
# "-" para números negativos.
# msg = mensagem passado pela função quando erro ocorrer (string)
def validaNumero(num, tipo, intervalo, msg):
    check = False
    if tipo == 'int':
        try:
            n = int(num)
        except:
            print(msg)
        else:
            if intervalo == '-0+':
                check = True
            elif intervalo == '0+':
                if n >= 0:
                    check = True
                else:
                    print(msg)
            elif intervalo == '+':
                if n > 0:
                    check = True
                else:
                    print(msg)
            elif intervalo == '-0':
                if n <= 0:
                    check = True
                else:
                    print(msg)
            elif intervalo == '-':
                if n < 0:
                    check = True
                else:
                    print(msg)
            
    elif tipo == 'float':
        try:
            n = float(num)
        except:
            print(msg)
        else:
            if intervalo == '-0+':
                check = True
            elif intervalo == '0+':
                if n >= 0:
                    check = True
                else:
                    print(msg)
            elif intervalo == '+':
                if n > 0:
                    check = True
                else:
                    print(msg)
            elif intervalo == '-0':
                if n <= 0:
                    check = True
                else:
                    print(msg)
            elif intervalo == '-':
                if n < 0:
                    check = True
                else:
                    print(msg)
            else:
                print(msg)
    return check


entrada = input('Entre com um número inteiro maior ou igual a zero: ')
while validaNumero(entrada ,'int' ,'0+', 'Valor digitado inválido!') == False:
    entrada = input('Entre com um número inteiro maior ou igual a zero: ')
n = int(entrada)

entrada = input('Entre com um número real: ')
while validaNumero(entrada ,'float' ,'-0+', 'Valor digitado inválido!') == False:
    entrada = input('Entre com um número real: ')
x = float(entrada)

print(f'({x})^{n} = {potencia(n, x)}')




        
