# Função distancia(x1, y1, x2, y2) que devolve a
# distância entre dois pontos cujas coordenadas cartesianas são 
# (x1, y1) e (x2, y2).
import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Testando a função com alguns pontos
print(f"Distância entre ({0}, {0}) e ({3}, {4}): {distancia(0, 0, 3, 4):.2f}")
print(f"Distância entre ({1}, {2}) e ({4}, {6}): {distancia(1, 2, 4, 6):.2f}")
print(f"Distância entre ({-1}, {-1}) e ({2}, {3}): {distancia(-1, -1, 2, 3):.2f}")
print()