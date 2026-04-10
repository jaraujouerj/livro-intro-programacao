# Programa que imprime uma tabela das raízes quadradas dos números
# entre 10 e 100, com incrementos de 10.
import math

print("Número\tRaiz Quadrada")

for numero in range(10, 101, 10):
    raiz_quadrada = math.sqrt(numero)
    print(f"{numero}\t{raiz_quadrada:.2f}")