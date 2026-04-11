# Função recursiva que calcula o fatorial de um número

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

num = int(input('Digite um número: '))
print(f'{num}! = {fatorial(num)}')
