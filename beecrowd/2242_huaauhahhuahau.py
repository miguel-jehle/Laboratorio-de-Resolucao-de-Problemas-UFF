risada = input()
vogais = []
for i in range(len(risada)):
    if risada[i] == 'a' or risada[i] == 'e' or risada[i] == 'i' or risada[i] == 'o' or risada[i] == 'u':
        vogais.append(risada[i])
vogais_inv = list(reversed(vogais))
if vogais == vogais_inv:
    print('S')
else:
    print('N')
