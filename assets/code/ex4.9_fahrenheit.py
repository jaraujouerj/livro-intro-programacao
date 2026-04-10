# Função que recebe valor em Celsius e devolve em Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Imprime tabela de conversão de Celsius para Fahrenheit entre 
# 0 e 100 com intervalos de 10 graus
print("Celsius\tFahrenheit")
for celsius in range(0, 101, 10):
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}\t{fahrenheit:.1f}")
print()