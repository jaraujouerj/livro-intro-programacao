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

# Calcula pi a partir de um número de pontos sorteados. 
# O número de pontos é lido do usuário.
# Repete o processo até o usuário escolher 0 pontos. 
# Imprime o valor de pi e o erro associado a cada cálculo.
while True:
    num = int(input('Quantos pontos devem ser sorteados? '))
    if num == 0:
        break
    pi, erro = calcula_pi(num)
    print(f'Com {num} pontos, o valor de pi é {pi} com erro {erro}')