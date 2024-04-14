n = int(input())
predios = list(map(int,input().split()))
maior = 0
for i in range(0,n,1):
    for j in range(i+1,n,1):
        if predios[i] + predios[j] + (j-i) > maior:
            maior = predios[i] + predios[j] + (j-i)
print(maior)
