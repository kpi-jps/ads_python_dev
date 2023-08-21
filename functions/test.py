def main():
    op=input("Escolha uma operação (+, -, *, /): ")
    nro1= leitura()
    nro2= leitura()
    if op == '+':
        print('O resultado é: ',soma(nro1,nro2))
    elif op == '-':
        print('O resultado é: ',subtraia(nro1,nro2))
    elif op == '*':
        print('O resultado é: ',multiplique(nro1,nro2))
    elif op == '/':
        print('O resultado é: ',divida(nro1,nro2))
    else:
        print('Operação Inválida')
        main()

def leitura():
    nro=int(input("Digite um numero inteiro: "))
    return(nro)

def soma(n1,n2):
    return n1+n2

def subtraia(n1,n2):
    return n1-n2

def multiplique(n1,n2):
    return n1*n2

def divida(n1,n2):
    return n1/n2

main()
