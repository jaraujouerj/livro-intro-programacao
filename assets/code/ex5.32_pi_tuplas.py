# Cálculo de pi com coordenadas como lista de tuplas

import random as r
import math as m

def gera_coordenadas_aleatorias(n):
    """Gera lista de n pares de coordenadas aleatórias como tuplas."""
    return [(r.random(), r.random()) for _ in range(n)]

def coordenadas_dentro_circulo(x, y):
    """Testa se coordenadas estão dentro do círculo de raio 1."""
    return m.hypot(x, y) < 1

def calcula_pi(n):
    """Calcula pi e o erro associado a partir de n pontos."""
    coordenadas = gera_coordenadas_aleatorias(n)
    conta_circulo = 0
    for x, y in coordenadas:
        if coordenadas_dentro_circulo(x, y):
            conta_circulo += 1
    pi = 4 * conta_circulo / n
    erro = m.fabs(pi - m.pi)
    return pi, erro

num = int(input('Quantos pontos devem ser sorteados? '))
pi, erro = calcula_pi(num)
print(f'Com {num} pontos, o valor de pi é {pi} com erro {erro}')
