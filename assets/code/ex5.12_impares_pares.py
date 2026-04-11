# Dada [0,1,2,3,4,5,6,7,8,9] gera [1,3,5,7,9,0,2,4,6,8]

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = lista[1::2] + lista[0::2]
print(resultado)
