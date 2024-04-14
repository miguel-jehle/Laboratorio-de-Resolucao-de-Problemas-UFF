n = int(input())
for i in range(n):
    frase = list(input().split())
    letras = []
    mensagem = ''
    for j in range(len(frase)):
        letras.append(frase[j][0])
        mensagem += letras[j]
    if mensagem == '':
        print()
    else:
        print(mensagem)
