n = int(input())
while n != 0:
    original = []
    alunos = []
    falsos = 0
    for k in range(n):
        erros = 0
        original.append(list(input().split()))
    m = int(input())
    for k in range(m):
        alunos.append(list(input().split()))
    for i in range(n):
        for j in range(len(alunos[i][1])):
            if alunos[i][1][j] != original[i][1][j]:
                erros += 1
        if erros > 1:
            falsos += 1
    print(falsos)