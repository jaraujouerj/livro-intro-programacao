# Ordenação mergesort

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

def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a0 = merge_sort(a[:m])
    a1 = merge_sort(a[m:])
    return intercala(a0, a1)

lista = [64, 34, 25, 12, 22, 11, 90]
print('Lista original:', lista)
lista = merge_sort(lista)
print('Lista ordenada:', lista)
