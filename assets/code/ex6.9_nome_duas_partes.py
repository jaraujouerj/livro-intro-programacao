# Reformata nome com duas ou mais partes:
# "João Ribeiro" → "Ribeiro, João"
# "João Araujo Ribeiro" → "Ribeiro, João A."

nome = input('Digite o nome completo: ')
lista = nome.split(' ')

if len(lista) < 2:
    print(nome)
elif len(lista) == 2:
    nome_formatado = lista[1] + ', ' + lista[0]
    print(nome_formatado)
else:
    for i in range(1, len(lista) - 1):
        lista[i] = lista[i][0] + '.'
    sobrenome = lista[-1] + ','
    lista.pop()
    lista.insert(0, sobrenome)
    nome_formatado = ' '.join(lista)
    print(nome_formatado)
