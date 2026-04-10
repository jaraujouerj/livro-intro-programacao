# Use o módulo random para simular o lançamento de um dado de 6 lados. 
# Use a função randint().
import random as r

def lancar_dado():
    """Simula o lançamento de um dado de 6 lados."""
    return r.randint(1, 6)

# Lança o dado 10 vezes e imprime os resultados.
for i in range(10):
    resultado = lancar_dado()
    print(f"Lançamento {i + 1}: {resultado}")
print()