n = int(input())
for i in range(n):
    palavra = input()
    num = int(input())
    cifra = ''
    for j in range(len(palavra)):
        if ord(palavra[j]) - num < 65:
           cifra += chr(90 - (num - (ord(palavra[j]) - 64)))
        else:
            cifra += chr(ord(palavra[j]) - num)
    print(cifra)