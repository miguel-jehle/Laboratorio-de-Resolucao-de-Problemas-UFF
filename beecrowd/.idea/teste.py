#Q2
secreto = 57
n = int(input("Digite um número entre 1 e 100: "))
while(n != secreto):
    if (n > secreto):
        print("número alto!")
    if (n < secreto):
        print("número baixo!")
    n = int(input("Digite um número entre 1 e 100: "))

print("Parabéns. Você acertou o número secreto =", secreto,)
