# Função que converte Fahrenheit para Celsius
def celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Lê os valores do usuário
inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o passo: "))

# Imprime a tabela de conversão
print("Fahrenheit\tCelsius")
for fahrenheit in range(inicio, fim + 1, passo):
    celsius_value = celsius(fahrenheit)
    print(f"{fahrenheit}\t{celsius_value:.1f}")
print()