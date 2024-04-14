n = int(input())
contador = 0
for i in range (n):
    bandeja = list(map(int,input().split()))
    if bandeja [0] > bandeja [1]:
        contador += bandeja [1]
    bandeja[0] = 0
    bandeja [1] = 0
print(contador)