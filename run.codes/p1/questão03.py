#Receber a quantidade de hastes e a altura desejada
n, h = map(int,input().split())
#Receber as alturas das hastes
hastes = list(map(int,input().split()))
#Criar um contador de passos
passos = 0
#Criamos um laço de repetição para passar por cada haste da lista
for i in range(0,len(hastes)-1,1):
    #Criamos uma estrutura de decisão para realizar a conta somente se a haste analisada for diferente da altura lida
    if hastes[i] != h:
        #Se for maior, subtrair 1 da analisada e da próxima
        if hastes[i] > h:
            #Repetir esse processo até ficar da altura estabelecida
            while hastes[i] != h:
                hastes[i] = hastes[i] - 1
                hastes[i+1] = hastes[i+1] - 1
                passos += 1
        #Se for menor, soma 1 da analisada e da próxima
        else:
            #Repetir esse processo até ficar da altura estabelicida
            while hastes[i] != h:
                hastes[i] = hastes[i] + 1
                hastes[i+1] = hastes[i+1] + 1
                passos += 1
print(passos)