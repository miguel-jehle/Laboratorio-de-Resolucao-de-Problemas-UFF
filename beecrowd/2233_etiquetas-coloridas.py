R = int(input(),16)
G = int(input(),16)
B = int(input(),16)
quantG = R//G
quantB = G//B
resposta = ((quantG**2)*(quantB**2)) + (quantG**2) + 1
print(f"{resposta:x}")