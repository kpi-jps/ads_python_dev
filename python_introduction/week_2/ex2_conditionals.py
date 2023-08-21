#Ex.2 - Aula semana 2 - Condicionais
#Faça um programa que receba a idade de um eleitor e informa se o
#voto dele é facultativo (entre 16 e 17 anos), obrigatório (entre 18 a 65),
#se ele está dispensado de votar (acima de 65) ou ainda se ele não tem
#idade para votar.

idade = int(input('Digite sua idade: '))
if idade < 16:
    print('Você não tem idade para votar!')
else:
    if 16 <= idade <= 17:
        print('Seu voto é facultativo!')
    elif 18 <= idade <= 65:
        print('Seu voto é obrigatório!')
    else:
        print('Você é dispensado do voto obrigatório!')
