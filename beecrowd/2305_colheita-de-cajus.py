# Receber a entrada
num_linhas, num_col, linha_lote, col_lote = map(int, input().split())
valores = [list(map(int, input().split())) for _ in range(num_linhas)]

# Criar a sat
sat = [[None] * num_colunas for _ in range(num_linhas)]

# Calcular a primeira linha sa imagem integral por ser um caso especial
sat[0][0] = valores[0][0]
for col in range(1, num_col):
    sat[0][col] = sat[0][col - 1] + valores[0][col]
#Calcular o restante da sat
for lin in range(1, num_linhas):
    sat[lin][0] = sat[lin-1][0] + valores[lin][0]
    for col in range(1,num_col):
        sat[lin][col] = sat[lin-1][col] + sat[lin][col-1] - sat[lin-1][col-1] + valores[lin][col]

#criamos a variavel sentinela
maior = 0
#Agora com a sat formada vamos percorrela para encontrar os valores dos lotes
for lin in num_linhas(linha_lote,num_linhas - (linha_lote-1),1):
    for col in num_col(col_lote,num_col - (col_lote-1),1):
        if sat[lin][col] > maior:
            maior = sat[lin][col]


