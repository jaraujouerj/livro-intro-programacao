# Matriz tridimensional usando lista por compreensão

x, y, z = 3, 4, 5
matriz = [[[0 for k in range(z)] for j in range(y)] for i in range(x)]
print(matriz)
