salario_atual = float(input())
if salario_atual <= 400.00:
    porc = '15 %'
    novo_salario = salario_atual * 1.15
elif 400.00 < salario_atual <= 800.00:
    porc = '12 %'
    novo_salario = salario_atual * 1.12
elif 800.00 < salario_atual <= 1200.00:
    porc = '10 %'
    novo_salario = salario_atual * 1.10
elif 1200.00 < salario_atual <= 2000.00:
    porc = '7 %'
    novo_salario = salario_atual * 1.07
else:
    porc = '4 %'
    novo_salario = salario_atual * 1.04
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {novo_salario-salario_atual:.2f}")
print(f"Em percentual: {porc}")