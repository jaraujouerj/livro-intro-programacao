# lê os números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# verifica se é múltiplo
if numero2 % numero1 == 0:
    print(numero2, "é múltiplo de", numero1)
else:
    print(numero2, "não é múltiplo de", numero1)