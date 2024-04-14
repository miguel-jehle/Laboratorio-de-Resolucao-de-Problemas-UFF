n = int(input())
for i in range(n):
    sonares = 0
    n, m = map(int,input().split())
    linhas = n-2
    colunas = m-2
    if linhas % 3  == 0:
        sonares += linhas % 3
    else:
        sonares += (linhas % 3) + 1
    if colunas % 3  == 0:
        sonares += colunas % 3
    else:
        sonares += (colunas % 3) + 1
    print(sonares)