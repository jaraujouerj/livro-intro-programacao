# Ordenação por inserção (insertion sort)

def ordenacao_insercao(lista):
    for j in range(1, len(lista)):
        chave = lista[j]
        i = j - 1
        while i >= 0 and lista[i] > chave:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = chave

lista = [64, 34, 25, 12, 22, 11, 90]
print('Lista original:', lista)
ordenacao_insercao(lista)
print('Lista ordenada:', lista)
