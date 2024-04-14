n = int(input())
postes = []
for i in range(n):
    postes.append(int(input()))
postes.append(postes[0])
cont = 0
maior = 0
for i in range(n):
    if postes[i] + postes[i+1] < 1000:
        cont += 1
        if cont > maior:
            maior = cont
    else:
        cont = 0
print(maior)