# Cria uma tabela com os valores de seno e cosseno e tangente 
# de ângulos entre 0 e 360 graus, a cada 30 graus.
import math

print("Ângulo\tSeno\tCosseno\tTangente")

for angulo in range(0, 361, 30):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    # Verificamos se o ângulo é 90 ou 270 (onde a tangente é indefinida)
    # Usamos o resto da divisão por 180 para pegar 90, 270, 450...
    if angulo % 180 == 90:
        # Definimos como inf ou -inf baseado no sinal do seno
        tangente = float('inf') if seno > 0 else float('-inf')
    else:
        tangente = math.tan(math.radians(angulo))
    print(f"{angulo:>3}\t{seno:>5.2f}\t{cosseno:>5.2f}\t{tangente:>5.2f}")
