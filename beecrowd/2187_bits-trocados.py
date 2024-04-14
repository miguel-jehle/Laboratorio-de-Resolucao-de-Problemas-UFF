v = int(input())
cont = 0
while v >= 1:
    cont += 1

    bit_50 = v//50
    resto = v % 50

    bit_10 = resto//10
    resto = resto % 10

    bit_5 = resto//5
    resto = resto % 5

    bit_1 = resto//1

    print(f"Teste {cont}")
    print(f"{bit_50} {bit_10} {bit_5} {bit_1}")
    print()
    v = int(input())
