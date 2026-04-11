# Obter [5,6,7,8,9,4,3,2,1,0] a partir de [0,1,2,3,4,5,6,7,8,9]

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
metade = len(lista) // 2
resultado = lista[metade:] + lista[:metade][::-1]
print(resultado)
