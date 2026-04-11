# Operações com fatiamento sobre lista de planetas

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Saturno', 'Júpiter', 'Urano', 'Netuno']
print('Original:', planetas)

# 1. Inserir ['Fobos', 'Deimos'] na posição 4
planetas[4:4] = ['Fobos', 'Deimos']
print('Após inserir Fobos e Deimos:', planetas)

# 2. Inserir ['Sol'] na posição 0
planetas[0:0] = ['Sol']
print('Após inserir Sol:', planetas)

# 3. Fatiamento para ['Urano', 'Júpiter', 'Saturno', 'Deimos', 'Fobos', 'Marte', 'Terra', 'Vênus']
print('Invertido do índice 3 ao 10:', planetas[10:2:-1])
