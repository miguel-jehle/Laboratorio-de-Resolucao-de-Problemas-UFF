n = int(input())
p = input().split()
p0 = int(p[0])
p2 = int(p[2])
if p[1] == '+' and p0 + p2 <= n:
    print('OK')
elif p[1] == '*' and p0 * p2 <= n:
    print('OK')
else:
    print('OVERFLOW')