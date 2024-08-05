# calcular um preço de um produto com 5% de desconto
n1 = float(input('digite o valor do produto: '))
desconto = n1 - 0.05 * n1
print('o produto de R${:.2f} com 5% de desconto seria R${:.2f}'.format(n1, desconto))
