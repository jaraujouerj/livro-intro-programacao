# Programa que imprime padrão de asteriscos
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# lê o número de linhas
n = int(input("Digite o número de linhas: "))

# imprime o padrão 
for i in range(1, n//2 + 2):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(n//2, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

