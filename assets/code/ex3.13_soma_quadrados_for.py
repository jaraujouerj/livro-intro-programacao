# lê o valor de n
n = int(input("Digite o valor de n: "))

# calcula a soma dos quadrados
soma = 0
for i in range(1, n):
    soma += i**2

# imprime o resultado
print("Soma dos quadrados:", soma)