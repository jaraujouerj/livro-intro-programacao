# Tabela com 10 valores de pi calculados com diferentes números de pontos

import random as r
import math as m

def gera_coordenadas_aleatorias():
    """Gera par de coordenadas aleatórias."""
    x = r.random()
    y = r.random()
    return x, y

def coordenadas_dentro_circulo(x, y):
    """Testa se coordenadas estão dentro do círculo de raio 1."""
    return m.hypot(x, y) < 1

def calcula_pi(n):
    """Calcula pi e o erro associado a partir de n pontos."""
    conta_circulo = 0
    for i in range(n):
        x, y = gera_coordenadas_aleatorias()
        if coordenadas_dentro_circulo(x, y):
            conta_circulo += 1
    pi = 4 * conta_circulo / n
    erro = m.fabs(pi - m.pi)
    return pi, erro

print(f'{"Pontos":>10} {"Pi":>12} {"Erro":>12}')
print('-' * 36)
for n in range(100, 1100, 100):
    pi, erro = calcula_pi(n)
    print(f'{n:>10} {pi:>12.6f} {erro:>12.6f}')
