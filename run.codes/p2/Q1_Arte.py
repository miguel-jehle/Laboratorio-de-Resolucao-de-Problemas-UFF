n = int(input())
metricas = list(map(int,input().split()))
ver = True
soma = metricas[0] + metricas[-1]
for i in range((n+1)//2):
    if  metricas[i] + metricas[-(i+1)] != soma:
        ver = False
        break
if ver:
    print('S')
else:
    print('N')