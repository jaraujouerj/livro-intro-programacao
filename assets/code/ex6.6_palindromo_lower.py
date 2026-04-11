# Testa se uma palavra é palíndromo, ignorando maiúsculas/minúsculas

def eh_palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

palavra = input('Digite uma palavra: ')
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')
