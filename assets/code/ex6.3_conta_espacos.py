# Conta a quantidade de espaços em branco de uma string

def conta_espacos(texto):
    contador = 0
    for caractere in texto:
        if caractere == ' ':
            contador += 1
    return contador

texto = input('Digite uma string: ')
print(f'A string possui {conta_espacos(texto)} espaço(s) em branco.')
