n = int(input())
valor = n
nota100 = n//100
resto = n % 100
nota50 = resto//50
resto = resto % 50
nota20 = resto // 20
resto = resto % 20
nota10 = resto // 10
resto = resto % 10
nota5 = resto//5
resto = resto % 5
nota2 = resto//2
resto = resto % 2
nota1 = resto//1
resto = resto % 1
print(valor)
print(nota100,'nota(s) de R$ 100,00')
print(nota50,'nota(s) de R$ 50,00')
print(nota20,'nota(s) de R$ 20,00')
print(nota10,'nota(s) de R$ 10,00')
print(nota5,'nota(s) de R$ 5,00')
print(nota2,'nota(s) de R$ 2,00')
print(nota1,'nota(s) de R$ 1,00')