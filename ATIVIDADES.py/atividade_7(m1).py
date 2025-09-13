#Crie uma função recursiva fibonacci(n) que calcule o 
# n-ésimo termo da sequência de Fibonacc

def fibonacci(n):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci de forma recursiva.

    Args:
      n: Um número inteiro não negativo.

    Returns:
      O n-ésimo termo da sequência de Fibonacci.
      Retorna uma mensagem de erro se n for negativo.
    """
    # Verifica se a entrada é válida (número não negativo)
    if n < 0:
        return "Erro: O índice deve ser um número inteiro não negativo."
    
    # Caso base: a condição de parada da recursão
    if n <= 1:
        return n
    
    # Passo recursivo: a função chama a si mesma
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)