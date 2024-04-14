#Receber a quantidade de jogadores e de rodadas
n, t = map(int,input().split())
#Receber as cartas em forma de lista
cartas = list(map(int,input().split()))
#Criei uma lista vazia para colocar o somatório dos pontos
pontos = []
#Criei um laço de repetição para determinar a pontuação de cada jogador e coloca-la na lista de pontos
for i in range(n):
    soma = 0
    for j in range(i,len(cartas),n):
        soma += cartas[j]
    pontos.append(soma)
#Criei duas variáveis sentinelas para serem substituidas na primeira análise e guardar os valores da maior pontuação e seu indice respectivo
maior = 0
index_vencedor = 0

for i in range(len(pontos)):
    if pontos[i] >= maior:
       maior = pontos[i]
       index_vencedor = i
#Imprimo o indice da maior pontuação +1 para compensar o fato de que a lista começava em 0 e os jogadores em 1
print(index_vencedor+1)