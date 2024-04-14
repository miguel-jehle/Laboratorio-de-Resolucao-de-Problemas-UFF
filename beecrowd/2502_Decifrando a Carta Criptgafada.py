c, n = map(int,input().split())
cifra1_Up = input()
cifra2_Up = input()
cifra1_Lo = cifra1_Up.lower()
cifra2_Lo = cifra2_Up.lower()
cifra1_Up = list(cifra1_Up)
cifra2_Up = list(cifra2_Up)
cifra1_Lo = list(cifra1_Lo)
cifra2_Lo = list(cifra2_Lo)
texto = []
for i in range(n):
    texto.append(list(input()))
    texto = list(texto)
res = ''
for i in range(len(texto)):
    for j in range(len(texto[i])):
        if texto[i][j] in cifra1_Up:
            texto[i][j] == cifra2_Up[cifra1_Up.index(texto[i][j])]

        elif texto[i][j] in cifra2_Up:
            texto[i][j] == cifra1_Up[cifra2_Up.index(texto[i][j])]

        elif texto[i][j] in cifra1_Lo:
            texto[i][j] == cifra2_Lo[cifra1_Lo.index(texto[i][j])]

        elif texto[i][j] in cifra2_Lo:
            texto[i][j] == cifra1_Lo[cifra2_Lo.index(texto[i][j])]

        res += texto[i][j]
print(res)