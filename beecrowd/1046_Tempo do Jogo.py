a, b = map(int,input().split())
if a > b:
    tempo = (24-a)+b
elif a == b:
    tempo = 24
else:
    tempo = b - a
print(f"O JOGO DUROU {tempo} HORA(S)")