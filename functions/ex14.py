'''
Exercícios - Aula de funções
Ex14 - Faça uma função que receba 2 strings e retorne Verdadeiro se a
segunda string é um anagrama da primeira, ou Falso caso contrário.
'''
# função principal
def main():
    str1 = input('Entre com uma palavra: ')
    str2 = input('Entre com uma outra palavra: ')
    if confirmaAnagrama(str1, str2):
        print('As palavras digitadas são ANAGRAMAS!')
    else:
        print('As palavras digitadas não são ANAGRAMAS!')
    
def normatizaStrings(string):
    s = string.upper()
    for i in range(len(s)):
        caracter = s[i]
        #desconsiderando acentuação
        if caracter == 'Á' or caracter == 'À' or caracter == 'Ã' or caracter == 'Â':
            s = s.replace(caracter, 'A')
        elif caracter == 'É' or caracter == 'È' or caracter == 'Ê':
            s = s.replace(caracter, 'E')
        elif caracter == 'Í' or caracter == 'Ì' or caracter == 'Î':
            s = s.replace(caracter, 'I')
        elif caracter == 'Ó' or caracter == 'Ò' or caracter == 'Ô':
            s = s.replace(caracter, 'O')
        elif caracter == 'Ú' or caracter == 'Ù':
            s = s.replace(caracter, 'U')
    return s
    
    
# funções secundárias
# cria a lista com valores numéricos
def confirmaAnagrama(string1, string2):
    str1 = normatizaStrings(string1)
    str2 = normatizaStrings(string2)
    
    if len(str1) == len(str2):
        i = 0
        j = len(str1) - 1
        cont = 0
        while i < len(str1):
            if str1[i] == str2[j]:
                cont += 1
            i += 1
            j -= 1
        if cont == len(str1):
            return True
        else:
            return False
    else:
        return False   
    
      

###############################################
# iniciando execução
###############################################
main()
