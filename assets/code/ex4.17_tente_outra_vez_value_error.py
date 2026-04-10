# Modifique o programa anterior para que o mesmo capture também a exceção
# ValueError da entrada de dados pelo usuário.
# Criando uma lista com 3 elementos
minha_lista = ["Banana", "Maçã", "Goiaba"]
# Pedindo ao usuário um índice
try:
    indice = int(input("Digite o índice do elemento a ser impresso (0-2): "))
    # Tentando acessar o elemento na posição especificada
    print(minha_lista[indice])
except IndexError:
    print("Erro: Índice fora da faixa permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
print()