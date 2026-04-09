# lê o valor de n
n = int(input("Digite o valor de n: "))

# calcula a soma dos quadrados
soma = 0
n -= 1
while n > 0:
    soma += n**2
    n -= 1

# imprime o resultado
print("Soma dos quadrados:", soma)