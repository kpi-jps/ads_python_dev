#Ex. 6 - Aula Semana 1
#Faça um programa que receba o salário de um funcionário, reajusta o
#salário em 25% e apresenta o valor do reajuste e o novo salário após o
#aumento.
salario = float(input('Digite o valor do salário do funcionário R$ = '))
reajuste = salario * 0.25
novo_salario = salario + reajuste
print(f'O valor do reajuste salarial R$ =  {reajuste}' )
print(f'O valor do novo salário é R$ =  {novo_salario}')

#outra maneira de imprimir na tela os resultados:
#print('O valor do reajuste salarial R$ = ', reajuste)
#print('O valor do novo salário é R$ = ', novo_salario)

#nota: o 'f' antes da mensagem do comando 'print' é relacionado a impressão
#formatada. Usando esta sintaxe é necessário usar '{}' entre as variaveis
