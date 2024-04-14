n = int(input())
lista = list(map(int, input().split()))

lista_soma = []
aux = 0
for i in range(n):
    soma = lista[i] + aux
    aux = soma
    lista_soma.append(soma)

for i in range(0, n, 1):
    if lista_soma[i] == (lista_soma[-1] - lista_soma[i]):
        print(i + 1)
