# Programa que imprime uma figura usando asteriscos

# número de linhas da figura
n = 5

# imprime a figura
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print() 
    