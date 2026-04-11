# Intercalação de duas listas ordenadas

def intercala(lista1, lista2):
    resultado = []
    i = 0
    j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado

lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8, 10]
print('Lista 1:', lista1)
print('Lista 2:', lista2)
print('Intercalada:', intercala(lista1, lista2))
