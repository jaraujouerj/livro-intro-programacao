# Função recursiva que soma os n primeiros números

def soma(n):
    if n == 0:
        return 0
    return n + soma(n - 1)

num = int(input('Digite um número: '))
print(f'A soma dos {num} primeiros números é {soma(num)}')
