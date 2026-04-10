# Função que recebe um número inteiro e devolve seu quadrado
def quadrado(numero):
    return numero * numero

# lê um número do usuário
num = int(input("Digite um número: "))

# imprime o quadrado do número
print("O quadrado de", num, "é", quadrado(num))
print()