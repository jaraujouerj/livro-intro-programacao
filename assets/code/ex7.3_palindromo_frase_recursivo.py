# Função recursiva que diz se uma frase é palíndromo (ignorando espaços)

def eh_palindromo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return eh_palindromo(texto[1:-1])

frase = input('Digite uma frase: ')
frase_limpa = frase.lower().replace(' ', '')
if eh_palindromo(frase_limpa):
    print(f'"{frase}" é um palíndromo.')
else:
    print(f'"{frase}" não é um palíndromo.')
