N = int(input())
menor = float('inf')
for i in range(N):
    P, G = input().split()
    P = float(P)
    G = int(G)
    valorgrama = P / G
    if valorgrama < menor:
        menor = valorgrama
print("{:.2f}" .format(menor * 1000))