# Converte graus Fahrenheit para Celsius entre 0 e 100 com intervalos de 10 graus

print("Fahrenheit\tCelsius")

for fahrenheit in range(0, 101, 10):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}\t\t{celsius:.1f}")