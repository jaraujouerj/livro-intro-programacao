# Testa se uma palavra é palíndromo usando fatiamento

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

palavra = input('Digite uma palavra: ')
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')
