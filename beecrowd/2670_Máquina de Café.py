#Importo sys para usar maxsize
import sys
#Recebo os valores de entrada
a = int(input())
b = int(input())
c = int(input())
#Crio uma variável sentinela para ser substituida conforme um menor valor aparecer
menor = sys.maxsize
#Calculo as 3 possibilidades de locação do reeitório, e caso seja menor, a variável menor assumirá seu valor
if a*2 + c*2 < menor:
    menor = a*2 + c*2
if a*4 + b*2 < menor:
    menor = a*4 + b*2
if b*2 + c*4 < menor:
    menor = b*2 + c*4
#Imprimo a variável menor
print(menor)