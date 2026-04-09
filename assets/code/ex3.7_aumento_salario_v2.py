# lê o salário
salario = float(input("Digite o salário: "))

# calcula o aumento
if salario <= 1000:
    aumento = 0.2
elif salario <= 2000:
    aumento = 0.18
elif salario <= 4000:
    aumento = 0.15
else:
    aumento = 0.1

novo_salario = salario + salario * aumento

# imprime o resultado
print("Novo salário:", novo_salario)