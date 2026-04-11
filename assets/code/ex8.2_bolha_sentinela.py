# Ordenação por borbulhamento com sentinela e posição da última troca

lista = [64, 34, 25, 12, 22, 11, 90]

print('Lista original:', lista)

n = len(lista)
limite = n - 1
ultimo = limite

while limite != 0:
    limite = 0
    for i in range(ultimo):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            limite = i
    ultimo = limite

print('Lista ordenada:', lista)
