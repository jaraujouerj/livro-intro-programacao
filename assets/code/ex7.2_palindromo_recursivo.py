# Função recursiva que diz se uma palavra é palíndromo

def eh_palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return eh_palindromo(palavra[1:-1])

palavra = input('Digite uma palavra: ')
if eh_palindromo(palavra.lower()):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')
