#Ex.6 - Aula semana 2 - Condicionais
#Uma determinada loja está fazendo promoções de vendas. Qualquer
#compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se
#a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto
#será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de
#20%.

valor = float(input('digite o valor da compra R$ '))
if valor <= 100:
    desconto = valor * 0.05
    novo_valor = valor - desconto
    print(f'valor da compra = R$ {valor}')
    print(f'desconto = R$ {desconto} (5%)')
    print(f'valor final = R$ {novo_valor}')
    print(f'Nota: Para compras de até R$ 100 o desconto é de 5%')
elif valor > 100 and valor <= 200:
    desconto = valor * 0.10
    novo_valor = valor - desconto
    print(f'valor da compra = R$ {valor}')
    print(f'desconto = R$ {desconto} (10%)')
    print(f'valor final = R$ {novo_valor}')
    print(f'Para compras de até R$ 100 o desconto é de 10%')
else:
    desconto = valor * 0.2
    novo_valor = valor - desconto
    print(f'valor da compra = R$ {valor}')
    print(f'desconto = R$ {desconto} (20%)')
    print(f'valor final = R$ {novo_valor}')
    print(f'Para compras de até R$ 100 o desconto é de 20%')
