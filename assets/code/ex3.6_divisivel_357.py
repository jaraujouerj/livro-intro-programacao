# lê o número
numero = int(input("Digite um número: "))

# verifica se é divisível por 3, 5 ou 7
if numero % 3 == 0:
    print(numero, "é divisível por 3")
elif numero % 5 == 0:
    print(numero, "é divisível por 5")
elif numero % 7 == 0:
    print(numero, "é divisível por 7")
else:
    print(numero, "não é divisível por 3, 5 ou 7")