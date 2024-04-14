n = float(input())
if 0 <= n <= 2000.00:
    print('Insento')
elif 2000.01 <= n <= 3000.00:
    imposto = (n-2000.00)*0.08
    print(f"R$ {imposto:.2f}")
elif 3000.01 <= n <= 4500.00:
    imposto = ((n-3000)*0.18) + 80
    print(f"R$ {imposto:.2f}")
elif n > 4500.00:
    imposto = ((n-4500)*0.28) + 80 + 270
    print(f"R$ {imposto:.2f}")

    
    
    