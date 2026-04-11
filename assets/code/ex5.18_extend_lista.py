# extend() com outra lista

primos = [2, 3, 5, 7]
primos.extend([23, 29, 31])
print('Lista após extend:', primos)
print('primos[4]:', primos[4])
# primos[4] imprime 23, pois extend adiciona cada elemento
# individualmente à lista.
