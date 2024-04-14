rodada = 0
n = int(input())
while n > 0:
    ganhadores = []
    rodada += 1
    print('Teste', rodada)
    pessoa_par = input()
    pessoa_impar = input()
    for i in range (n):
        num0, num1 = map(int,input().split())
        if (num0 + num1) % 2 == 0:
            ganhadores.append(pessoa_par)
        else:
            ganhadores.append(pessoa_impar)
    for j in range (n):
        print(ganhadores[j])
    print()
    n = int(input())