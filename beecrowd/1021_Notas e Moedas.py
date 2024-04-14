n = float(input())
nota100 = n // 100
resto = n % 100
nota50 = resto // 50
resto = resto % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota5 = resto // 5
resto = resto % 5
nota2 = resto // 2
resto = resto % 2
moeda1 = resto // 1
resto = resto % 1
moeda50 = resto // 0.5
resto = resto % 0.5
moeda25 = resto // 0.25
resto = resto % 0.25
moeda10 = resto // 0.1
resto = resto % 0.1
moeda5 = resto // 0.05
resto = resto % 0.05
moeda01 = resto / 0.01
print('NOTAS:')
print(f"{int(nota100):d} nota(s) de R$ 100.00")
print(f"{int(nota50):d} nota(s) de R$ 50.00")
print(f"{int(nota20):d} nota(s) de R$ 20.00")
print(f"{int(nota10):d} nota(s) de R$ 10.00")
print(f"{int(nota5):d} nota(s) de R$ 5.00")
print(f"{int(nota2):d} nota(s) de R$ 2.00")
print('MOEDAS:')
print(f"{int(moeda1):d} moeda(s) de R$ 1.00")
print(f"{int(moeda50):d} moeda(s) de R$ 0.50")
print(f"{int(moeda25):d} moeda(s) de R$ 0.25")
print(f"{int(moeda10):d} moeda(s) de R$ 0.10")
print(f"{int(moeda5):d} moeda(s) de R$ 0.05")
print(f"{moeda01:.0f} moeda(s) de R$ 0.01")
