n = int(input())
valores = list(map(int,input().split()))
cont = 1
maior_cont = 0
for i in range(n-1):
    if valores[i] == valores [i+1]:
        cont += 1
        if cont > maior_cont:
            maior_cont = cont
    else:
        cont = 1
print(maior_cont)