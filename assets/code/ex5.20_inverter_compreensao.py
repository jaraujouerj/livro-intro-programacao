# Inverter uma lista usando lista por compreensão

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
invertida = [lista[i] for i in range(len(lista) - 1, -1, -1)]
print(invertida)
