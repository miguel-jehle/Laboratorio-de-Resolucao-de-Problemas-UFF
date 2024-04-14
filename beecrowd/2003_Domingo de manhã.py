while True:
    try:
        h, m = map(int,input().split(':'))
        tempo = (h*60) + m + 60
        atraso = tempo - 480
        if atraso < 0:
            print(f"Atraso maximo: 0")
        else:
            print(f"Atraso maximo: {atraso}")
    except EOFError:
        break