import sys
n = int(input())
trilhas = []
for i in range(n):
    trilhas.append(list(map(int,input().split()[1:])))
menor = sys.maxsize
ind_menor = 0
for i in range(n):
    ida = 0
    volta = 0
    for j in range(len(trilhas[i])-1):
        if trilhas[i][j] < trilhas[i][j+1]:
          ida += trilhas[i][j+1] - trilhas[i][j]
        elif trilhas[i][j] > trilhas[i][j+1]:
          volta += trilhas[i][j] - trilhas[i][j+1]
    if ida < volta:
        custo = ida
    else:
        custo = volta
    if custo < menor:
        menor = custo
        ind_menor = i
print(ind_menor+1)