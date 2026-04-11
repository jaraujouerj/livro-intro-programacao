# Dada [0,1,2,3,4,5,6,7,8,9] gera [5,6,7,8,9,0,1,2,3,4]

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = lista[5:] + lista[:5]
print(resultado)
