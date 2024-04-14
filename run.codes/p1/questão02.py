#Crio um while para rodar o código enquanto a entrada não for -1 e um contador para contabilizar qual o teste.py sendo feito
n = 1
contador = 0
while n != -1:
 #Recebo o valor de entrada
 n = int(input())
 if n != -1:
    #Calculo de acordo com a formula obtida
    partes = ((2**n)+1)**2
    #Somo 1 ao contador a cada rodada
    contador += 1
    #Imprimo conforme solicitado
    print(f"Teste {contador}")
    print(partes)
    print()