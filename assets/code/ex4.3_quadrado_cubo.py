# Programa em Python que lê um número e imprime a si mesmo, 
# o seu quadrado e o seu cubo.

import math
# lê o número
numero = float(input("Digite um número: "))
# calcula o quadrado e o cubo
quadrado = numero ** 2
cubo = numero ** 3

# imprime o resultado
print("Número:", numero)
print("Quadrado:", math.pow(numero, 2))
print("Cubo:", math.pow(numero, 3))