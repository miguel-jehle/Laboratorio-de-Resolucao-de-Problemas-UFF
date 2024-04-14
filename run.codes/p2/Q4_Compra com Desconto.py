n = int(input())
produtos = []
for i in range(n):
    produtos.append(int(input()))
ordenado = sorted(produtos,reverse=True)
valor = 0
for i in range(n):
    if (i+1) % 3 != 0:
        valor += ordenado[i]
print(valor)
