# Programa que recebe uma lista de temperaturas em Celsius e escreve
# na tela o resultado da conversão dessas temperaturas em Fahrenheit.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_celsius = [0, 20, 37, 100]
temperaturas_fahrenheit = [celsius_para_fahrenheit(temp) for temp in temperaturas_celsius]

print("Temperaturas em Fahrenheit:")
for i in range(len(temperaturas_celsius)):
    print(f"{temperaturas_celsius[i]}°C = {temperaturas_fahrenheit[i]}°F")
print()