# Programa que imprime  árvore de natal com comandos for in range() 
# em vez de escrever explicitamente cada linha. 
# Usa 5 laços com for para desenhar a árvore.

def imprime_linha(n1, carac1, n2, carac2):
    print(carac1 * n1 + carac2 * n2)

def imprime_arvore():
    # 1. Topo (@) e primeira camada de folhas (1, 3, 5)
    for i in range(1, 6, 2):
        char = '@' if i == 1 else '*'
        imprime_linha((11 - i) // 2, ' ', i, char)

    # 2. Segunda camada de folhas (3, 5, 7, 9)
    for i in range(3, 10, 2):
        imprime_linha((11 - i) // 2, ' ', i, '*')

    # 3. Terceira camada  de folhas(5, 7, 9)
    for i in range(5, 10, 2):
        imprime_linha((11 - i) // 2, ' ', i, '*')
    
    # 4. Quarta camada - a base mais larga (7, 9, 11)
    for i in range(7, 12, 2):
        imprime_linha((11 - i) // 2, ' ', i, '*')

    # 5. O tronco da árvore (3, 5)
    for i in range(3, 6, 2):
        imprime_linha((11 - i) // 2, ' ', i, '|')

imprime_arvore()