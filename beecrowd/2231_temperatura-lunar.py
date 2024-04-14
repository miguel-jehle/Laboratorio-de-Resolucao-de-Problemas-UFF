#Recebo os valores de n e m
n, m = map(int,input().split())
#Criei um contador para printar o teste.py
contador = 0
#Criei um while para o codigo rodar enquanto as primeiras entradas forem diferentes de 0
while n != 0 and m != 0:
    contador += 1
    temp = []

    #Criei um for para receber os valores das temperaturas inseridos e já colocalos na lista de temperaturas
    for i in range(n):
        temp.append(int(input()))

    #Criei uma lista vazia para a soma acumulada das temperaturas e uma variável para auxiliar no processo, salvando a soma anterior realizada
    lista_soma = []
    aux = 0

    #Realizo outro for para criar a lista de soma acumulada das temperaturas como solicitado em sala
    for i in range(0,n,1):
        soma = temp[i] + aux
        aux = soma
        lista_soma.append(soma)

    #Crio um for para analisar intervalo por intervalo e realizar a media dele, usando as somas acumuladas para evitar um timelimit error
    for i in range(m-1,len(lista_soma),1):

        #Assumo a primeira média como menor e maior, para funcionar como sentinela
        if i == m-1:
            menor = (lista_soma[i])/m
            maior = (lista_soma[i])/m

        #Analiso se as medias seguintes são maiores ou menores que as sentinelas e caso sim, substituo
        else:
            if (lista_soma[i] - lista_soma[i-m])/m > maior:
                maior = (lista_soma[i] - lista_soma[i-m])/m
            if (lista_soma[i] - lista_soma[i-m])/m < menor:
               menor = (lista_soma[i] - lista_soma[i-m])/m
    #Imprimo conforme solicitado
    print(f"Teste {contador}")
    print(int(menor),int(maior))
    print()
    #Recebo novamente para reiniciar o loop ou para finaliza-lo
    n, m = map(int, input().split())
