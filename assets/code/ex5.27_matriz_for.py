# Matriz bidimensional usando 2 for encaixados

linhas = 3
colunas = 4

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(0)
    matriz.append(linha)

print(matriz)
