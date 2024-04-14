n = int(input())
pesos = []
for i in range(n):
    pesos.append(int(input()))
total_pesos = sum(pesos)
peso_justo = total_pesos // n
for i in range(n):
    print(peso_justo-pesos[i])
