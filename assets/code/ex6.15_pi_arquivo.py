# Gera pontos aleatórios para cálculo de pi e salva em arquivo

import random as r
import math as m

def gera_coordenadas_aleatorias():
    x = r.random()
    y = r.random()
    return x, y

def coordenadas_dentro_circulo(x, y):
    """Testa se coordenadas estão dentro do círculo de raio 1."""
    return m.hypot(x, y) < 1

def calcula_pi(n, arquivo):
    """Calcula pi, salva pontos no arquivo e retorna pi e erro."""
    conta_circulo = 0
    for i in range(n):
        x, y = gera_coordenadas_aleatorias()
        arquivo.write(f'{x:.6f} {y:.6f}\n')
        if coordenadas_dentro_circulo(x, y):
            conta_circulo += 1
    pi = 4 * conta_circulo / n
    erro = m.fabs(pi - m.pi)
    return pi, erro

num = int(input('Quantos pontos devem ser sorteados? '))
with open('pontos_pi.txt', 'w') as arq:
    pi, erro = calcula_pi(num, arq)
    arq.write(f'\nResultado: pi = {pi}, erro = {erro}\n')

print(f'Com {num} pontos, o valor de pi é {pi} com erro {erro}')
print('Pontos salvos em pontos_pi.txt')
