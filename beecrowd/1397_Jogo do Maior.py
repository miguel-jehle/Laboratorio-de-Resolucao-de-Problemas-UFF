n = int(input())
while n != 0:
    A = B = 0
    for i in range(n):
        a, b = map(int,input().split())
        if a > b:
            A += 1
        elif b > a:
            B += 1
    print(f"{A} {B}")
    n = int(input())