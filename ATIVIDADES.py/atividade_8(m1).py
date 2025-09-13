#Crie uma função que use fibonacci(n) para imprimir
#  a sequência inteira até o n-ésimo termo. 

def fibonacci(n):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci de forma recursiva.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def imprimir_sequencia_fibonacci(n):
    """
    Imprime a sequência inteira de Fibonacci até o n-ésimo termo.

    Args:
      n: Um número inteiro não negativo que define o último termo da sequência a ser impresso.
    """
    if n < 0:
        print("Erro: O índice deve ser um número inteiro não negativo.")
        return []

    sequencia = []
    for i in range(n + 1):  # O loop vai de 0 até n
        sequencia.append(fibonacci(i))
    
    return sequencia

# Exemplo de uso:
termo_limite = 10
sequencia_completa = imprimir_sequencia_fibonacci(termo_limite)
print(f"A sequência de Fibonacci até o {termo_limite}º termo é:")
print(sequencia_completa)

# Resultado:
# A sequência de Fibonacci até o 10º termo é:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]