n = int(input())
while n != 0:
    #Criar os verificadores
    ver_valor = True
    ver_dig = True
    #Criar o cont
    div = 0
    #Transformar em string para ser percorrido
    digitos = str(n)
    #Verificar se o valor dado é primo
    for i in range(1,n+1,1):
        if n % i == 0:
            div += 1
            if div == 3:
                ver_valor = False
                break
    for i in range(len(digitos)):
        div = 0
        if ver_dig:
            for j in range(1,int(digitos[i])+1,1):
                if int(digitos[i]) % j == 0:
                    div += 1
                    if div > 2:
                        ver_dig = False
                        break
        else:
            break
    if ver_dig and ver_valor:
        print('Super')
    else:
        print('Normal')
    n = int(input())