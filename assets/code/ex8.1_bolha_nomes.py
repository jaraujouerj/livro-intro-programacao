# Ordenação por borbulhamento (bubble sort) com lista de nomes

lista = ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']

print('Lista original:', lista)

n = len(lista)
for j in range(n - 1):
    for i in range(n - 1 - j):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print('Lista ordenada:', lista)
