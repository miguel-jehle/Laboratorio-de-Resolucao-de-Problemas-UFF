p, r = map(int, input().split())
teste = 0
while p and r != 0:
    teste += 1
    jogadores = list(map(int, input().split()))
    aux = jogadores
    rodadas = []
    for i in range(r):
        rodadas.append(list(map(int, input().split())))
    for i in range(len(rodadas)):
        rodadas_novas = []
        for j in range(2,len(rodadas[i])):
            if rodadas[i][j] == rodadas[i][1]:
                rodadas_novas.append(rodadas[i][j])
    print(f"Teste {teste}")
    print(rodadas_novas[0])
    print()
    p, r = map(int, input().split())
