# Testa se uma frase é palíndromo, ignorando espaços e maiúsculas/minúsculas

def eh_palindromo(texto):
    texto = texto.lower().replace(' ', '')
    return texto == texto[::-1]

frase = input('Digite uma frase: ')
if eh_palindromo(frase):
    print(f'"{frase}" é um palíndromo.')
else:
    print(f'"{frase}" não é um palíndromo.')
