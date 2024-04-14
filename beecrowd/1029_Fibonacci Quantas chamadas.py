k = int(input())
for j in range(k):
    chamadas = [1,1]
    valor = [0, 1]
    n = int(input())
    for i in range(2,41):
        chamadas.append(chamadas[i-2]+ chamadas[i-1] + 1)
        valor.append(valor[i-2]+valor[i-1])

    print(f"fib({n}) = {chamadas[n]-1} calls = {valor[n]}")
