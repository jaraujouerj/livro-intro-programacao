# lê os números
soma = 0
contador = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    soma += numero
    contador += 1
    numero = int(input("Digite um número (0 para sair): "))

# calcula a média
if contador > 0:
    media = soma/ contador
    print("Média dos números:", media)
else:
    print("Nenhum número foi digitado.")
