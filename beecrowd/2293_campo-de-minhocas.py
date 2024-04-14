n, m = list(map(int,input().split()))
matriz = []
for i in range(n):
    matriz.append(list(map(int,input().split())))

maior = 0
for i in range(n):
    soma = 0
    for j in range(m):
        soma = matriz[i][j] + soma
        if soma > maior:
            maior = soma

for i in range(m):
    soma = 0
    for j in range(n):
        soma = matriz[j][i] + soma
        if soma > maior:
            maior = soma
print(maior)