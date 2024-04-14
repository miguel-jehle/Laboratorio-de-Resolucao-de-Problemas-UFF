n ,m = map(int,input().split())
postos = list(map(int,input().split()))
postos.append(int(42195))
verificador = True
for i in range(1,n+1,1):
    if postos[i]-postos[i-1] > m:
        verificador = False
        break
if verificador == True:
    print('S')
else:
    print('N')