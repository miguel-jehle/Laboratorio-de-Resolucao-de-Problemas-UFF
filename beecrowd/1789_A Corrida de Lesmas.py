while True:
    try:
        n = int(input())
        lesmas = list(map(int,input().split()))
        lesmas_ordenadas = sorted(lesmas)
        if lesmas_ordenadas[-1] < 10:
            print('1')
        elif 10 <= lesmas_ordenadas[-1] < 20:
            print('2')
        else:
            print('3')
    except EOFError:
        break