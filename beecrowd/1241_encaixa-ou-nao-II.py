n = int(input())
for i in range(n):
    a, b = input().split()
    if len(a) >= len(b):
        ver = True
        for j in range(len(b)):
            if b[j] == a[-len(b)+j]:
                ver = True
            else:
                ver = False
                break
    else:
        ver = False
    if ver:
        print('encaixa')
    else:
        print('nao encaixa')