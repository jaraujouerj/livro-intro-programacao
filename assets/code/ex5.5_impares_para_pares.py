# Lista de ímpares entre 0 e 100, transformando cada um no par subsequente

impares = list(range(1, 100, 2))
print('Ímpares originais:', impares)

for i, valor in enumerate(impares):
    impares[i] = valor + 1

print('Pares subsequentes:', impares)
