nome = input()
fixo = float(input())
venda = float(input())
comissao = 0.15*venda
total = fixo + comissao
print('TOTAL = R$ {:.2f}'.format(total))