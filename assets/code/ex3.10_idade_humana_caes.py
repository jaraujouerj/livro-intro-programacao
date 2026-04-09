peso = float(input("Peso do cão (kg): "))
idade = float(input("Idade do cão (anos): "))

# Classificação do porte com condições compostas
if peso <= 10:
    porte = "pequeno"
elif peso > 10 and peso <= 23:
    porte = "medio"
else:
    porte = "grande"

# Definição dos coeficientes
if porte == "pequeno":
    fator_inicial = 12.5
    fator_adicional = 5.2
elif porte == "medio":
    fator_inicial = 10.5
    fator_adicional = 5.7
else:
    fator_inicial = 9.0
    fator_adicional = 7.8

# Cálculo da idade humana
if idade <= 2:
    idade_humana = idade * fator_inicial
else:
    idade_humana = (2 * fator_inicial) + ((idade - 2) * fator_adicional)

print(f"Porte: {porte}")
print(f"Idade humana equivalente: {idade_humana:.1f} anos")
