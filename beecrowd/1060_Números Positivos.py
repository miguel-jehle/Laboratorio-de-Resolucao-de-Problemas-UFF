numeros = []
cont = 0
for i in range(6):
    numeros.append(input())
for i in range(6):
    if float(numeros[i]) > 0:
        cont += 1
print(f"{cont} valores positivos")