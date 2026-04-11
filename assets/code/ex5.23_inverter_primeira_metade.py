# Inverter os elementos da primeira metade de uma lista

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
metade = len(lista) // 2
lista[:metade] = lista[:metade][::-1]
print(lista)
