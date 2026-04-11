# Reformata nome com número arbitrário de partes:
# "João Araujo de Souza Ribeiro" → "Ribeiro, João A. de S."

nome = input('Digite o nome completo: ')
lista = nome.split(' ')

# Abreviar partes intermediárias (exceto primeira e última)
for i in range(1, len(lista) - 1):
    lista[i] = lista[i][0] + '.'

# Mover sobrenome para o início
sobrenome = lista[-1] + ','
lista.pop()
lista.insert(0, sobrenome)

nome_formatado = ' '.join(lista)
print(nome_formatado)
