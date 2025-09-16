# 1. Fatorial recursivo
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

# 2. Soma de 1 até n recursiva
def soma_n(n):
    if n == 1:
        return 1
    return n + soma_n(n - 1)

# 3. Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 4. Imprimir a sequência de Fibonacci até o n-ésimo termo
def imprimir_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=' ')
    print()

# 5. Fibonacci com rastreamento de chamadas (com indentação)
def fibonacci_rastreamento(n, nivel=0):
    print('  ' * nivel + f'chamada: fibonacci({n})')
    if n == 0:
        print('  ' * nivel + 'retorna 0')
        return 0
    if n == 1:
        print('  ' * nivel + 'retorna 1')
        return 1
    res = fibonacci_rastreamento(n - 1, nivel + 1) + fibonacci_rastreamento(n - 2, nivel + 1)
    print('  ' * nivel + f'retorna {res}')
    return res

# Exemplos de uso:
print("Fatorial de 5:", fatorial(5))
print("Soma de 1 até 5:", soma_n(5))
print("6 primeiros termos de Fibonacci:")
imprimir_fibonacci(6)
print("Rastreamento de chamadas de fibonacci(4):")
fibonacci_rastreamento(4)