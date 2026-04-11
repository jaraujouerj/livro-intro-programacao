# Fatiamento com valores negativos em lista de 0 a 99

lista = list(range(100))

print('1. Último elemento e decrescendo de 3 em 3:', lista[-1::-3])
print('2. Índice 87 até 34 (exclusive), decrescente:', lista[87:34:-1])
print('3. Todos exceto os dois últimos:', lista[:-2])
