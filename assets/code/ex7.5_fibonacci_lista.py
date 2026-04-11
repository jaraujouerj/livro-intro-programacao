# Fibonacci com memoização usando lista em vez de dicionário

fibonacci = [0, 1]

def fib(n):
    """Calcula n-ésimo termo da série de Fibonacci."""
    if n >= len(fibonacci):
        fibonacci.append(fib(n - 2) + fib(n - 1))
    return fibonacci[n]

for i in range(100):
    print(f'fib({i}): {fib(i)}')
