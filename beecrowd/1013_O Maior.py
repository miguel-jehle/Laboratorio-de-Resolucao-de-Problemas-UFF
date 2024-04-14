a, b, c = map(int,input().split())
d = (a+b+abs(a-b))//2
maior_total = (d+c+abs(d-c))//2
print(maior_total,'eh o maior')