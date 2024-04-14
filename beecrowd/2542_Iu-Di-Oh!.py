while True:
    try:
        n = int(input())
        marcos, leo = map(int,input().split())
        cartas_m = []
        for _ in range(marcos):
            cartas_m.append(list(map(int,input().split())))
        cartas_l = []
        for _ in range(leo):
            cartas_l.append(list(map(int,input().split())))
        Cm, Cl = map(int,input().split())
        A = int(input())
        if cartas_m[Cm-1][A-1] > cartas_l[Cl-1][A-1]:
            print('Marcos')
        elif cartas_m[Cm-1][A-1] < cartas_l[Cl-1][A-1]:
            print('Leonardo')
        else:
            print('Empate')
    except EOFError:
        break