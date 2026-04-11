# Ordenação por inserção recursiva

def insercao_recursiva(lista, n):
    if n <= 1:
        return
    insercao_recursiva(lista, n - 1)
    chave = lista[n - 1]
    i = n - 2
    while i >= 0 and lista[i] > chave:
        lista[i + 1] = lista[i]
        i -= 1
    lista[i + 1] = chave

lista = [64, 34, 25, 12, 22, 11, 90]
print('Lista original:', lista)
insercao_recursiva(lista, len(lista))
print('Lista ordenada:', lista)
