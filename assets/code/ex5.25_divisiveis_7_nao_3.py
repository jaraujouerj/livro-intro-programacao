# Números entre 100 e 1000 divisíveis por 7 mas não múltiplos de 3

lista = [x for x in range(100, 1001) if x % 7 == 0 and x % 3 != 0]
print(lista)
