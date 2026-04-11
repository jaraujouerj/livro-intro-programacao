# Função recursiva que imprime uma string na ordem inversa

def inverte(texto):
    if len(texto) == 0:
        return ''
    return inverte(texto[1:]) + texto[0]

texto = input('Digite uma string: ')
print(inverte(texto))
