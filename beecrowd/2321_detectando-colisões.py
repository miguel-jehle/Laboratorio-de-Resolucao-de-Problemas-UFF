lista1  = list(input())
lista2  = list(input())
if len(lista1) >= len(lista2):
    maior = lista1
    for i in range(len(lista1)-len(lista2)):
        lista2.append('')
else:
    maior = lista2
    for i in range(len(lista2) - len(lista1)):
        lista1.append('')
verificador = 'nao_colide'
for i in range(len(maior)):
    if (lista1[i] != '' or lista1[i] != '0') and (lista2[i] != '' or lista2[i] != '0'):
        verificador = 'colide'
if verificador == 'não_colide':
    print('0')
else:
    print('1')

