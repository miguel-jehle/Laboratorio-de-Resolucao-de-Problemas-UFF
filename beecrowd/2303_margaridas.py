#Receber a matriz
l, c, m, n = map(int,input().split())
plantacao = []
for _ in range(l):
    plantacao.append(list(map(int,input().split())))

maior = 0
#Percorrer os lotes da matriz
for i in range(0,l,m):
    for j in range(0,c,n):
        margaridas = 0
        for k in range(i,m+i):
            for p in range(j,n+j):
                margaridas += plantacao[k][p]
        if margaridas > maior:
            maior = margaridas
print(maior)