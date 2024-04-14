A, B, C, D = map(int,input().split())
n = A
while n < C:
    res = False
    if n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
        res = True
        break
    n += 1
if res:
    print(n)
else:
    print(-1)