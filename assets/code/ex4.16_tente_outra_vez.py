# Escreva um programa que crie uma lista com 3 elementos e peça ao usuário um
# índice de um elemento a ser impresso. Se o usuário pedir um índice fora da faixa
# de valores permitidos (abaixo de zero ou acima de 2), o programa deve emitir
# uma mensagem de erro (Use a exceção IndexError).

# Criando uma lista com 3 elementos
minha_lista = ["Banana", "Maçã", "Goiaba"]

# Pedindo ao usuário um índice
indice = int(input("Digite o índice do elemento a ser impresso (0-2): "))

# Tentando acessar o elemento na posição especificada
try:
    print(minha_lista[indice])
except IndexError:
    print("Erro: Índice fora da faixa permitida.")
print()
#