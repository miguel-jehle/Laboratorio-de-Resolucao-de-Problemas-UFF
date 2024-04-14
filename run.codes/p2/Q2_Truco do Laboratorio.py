n = int(input())
ordem = [4,5,6,7,10,11,12,13,1,2,3]
tim = 0
maia = 0
Tim = 0
Maia = 0
for i in range(n):
    cartas = list(map(int,input().split()))
    for i in range(3):
        if ordem.index(cartas[i]) >= ordem.index(cartas[i+3]):
            maia += 1
        else:
            tim +=1
    if tim > maia:
        Tim += 1
    else:
        Maia += 1
print(f"{Tim} {Maia}")