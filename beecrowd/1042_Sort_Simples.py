a, b, c = map(int,input().split())
if a > b and a > c:
    d = a
    if b > c:
        e = b
        f = c
    else:
        e = c
        f = b
elif b > a and b > c:
    d = b
    if a > c:
        e = a
        f = c
    else:
        e = c
        f = a
else:
    d = c
    if a > b:
        e = a
        f = b
    else:
        e = b
        f = a
print(f)
print(e)
print(d)
print()
print(a)
print(b)
print(c)