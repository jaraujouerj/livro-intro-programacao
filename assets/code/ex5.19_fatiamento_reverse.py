# Fatiamento com passo -1 e diferença para reverse()

lista = [1, 2, 3, 4, 5]

# lista[::-1] cria uma NOVA lista invertida (a original não muda)
invertida = lista[::-1]
print('Original:', lista)
print('Fatiamento [::-1]:', invertida)

# reverse() modifica a lista original, sem criar nova lista
lista.reverse()
print('Após reverse():', lista)
