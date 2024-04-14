x0 ,y0 ,x1 ,y1 = list(map(int,input().split()))
x2 ,y2 ,x3 ,y3 = list(map(int,input().split()))
if x0 >= x3 >= x1 and y0 >= y3 >= y1:
    print('1')
else:
    print('0')