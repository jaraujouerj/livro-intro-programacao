# Lista com o quadrado dos números pares entre 10 e 20 (inclusive)

quadrados = [x**2 for x in range(10, 21) if x % 2 == 0]
print(quadrados)
