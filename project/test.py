import datetime

x = datetime.datetime.now()

anoString = x.strftime("%Y")

def checaAnoBissexto(ano):
    # checa se o ano é divisível por 4
    if ano % 4 == 0:
        # se for divisível por 4 checa se é divisível por 100 
        if ano % 100 == 0:
            # se for divisível por 4 e 100, checa se é divisível por 400,
            # se sim é ano bissexto e retorna "True"
            if ano % 400 == 0:
                return True
            # se não for divisível por 400 não é bissexto e retorna "False"
            else:
                return False
        # se não for divisível por 100 é bissexto e retona "True" 
        else:
            return True
    # senão for divisível por 4 não é bissexto e retona "False"
    else:
        return False
    
# retorna a quantidade de dias que um mês possui, na forma de um inteiro,
# usando como parâmetros o ano e o mês também na forma de  inteiros
def quantidadeDiasMes(ano, mes):
    # para os meses de janeiro (1), março (3), maio (5), julho (7), agosto (8),
    # outubro (10) e dezembro (12) retorna 31 dias
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31 # retorn 31 dias
    # para o mes de fevereiro (2) checa se o ano é bissexto, se sim retorna 29 dias
    # e se não retorna 28 dias
    elif mes == 2:
        if checaAnoBissexto(ano):
            return 29 # retorna 29 dias
        else:
            return 28 # retorna 28 dias
    # para os demais meses, abril (4), junho (6), setembo (8) e novembro (11), retorna 30 dias.
    else:
        return 30 # retorna 30 dias   
        
def calculaDataPassada(dia,mes,ano,num_dias):
    d = int(dia)
    m = int(mes)
    a = int(ano)
    nd = int(num_dias)
    check = False
    while check == False:
        if d - nd < 0:
            if m-1 == 0:
                a = a - 1
                m = 12
            else:
                m = m-1
            nd = (d-nd)*(-1)
            d = quantidadeDiasMes(a, m)
        elif d - nd == 0:
            if m-1 == 0:
                a = a - 1
                m = 12
            else:
                m = m-1
                d = quantidadeDiasMes(a, m)
            check = True
        else:
            d = d - nd
            check = True
    data = ''
    if d < 10:
        data = '0' + str(d) + '/'
    else:
        data = str(d) + '/'
    if m < 10:
        data += '0' + str(m) + '/'
    else:
        data += str(m) + '/'
    data += str(a)
    return data
print(calculaDataPassada('25','01','2021','100'))
