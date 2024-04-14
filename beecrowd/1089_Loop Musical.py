n = int(input())
while n != 0:
    notas = list(map(int,input().split()))
    notas.append(notas[0])
    notas.append(notas[1])
    cont = 0
    for i in range(1, n+1):
        if notas[i] > notas[i+1] and notas[i] > notas[i-1]:
            cont += 1
        elif  notas[i] < notas[i+1] and notas[i] < notas[i-1]:
            cont += 1
    print(f"{cont}")
    n = int(input())