# Modifique a função fibonacci(n) para mostrar no 
# console cada chamada recursiva (com indentação).
#Exemplo: ao calcular fibonacci(4), deve 
#aparecer o rastreamento de chamadas.

def fibonacci(n, nivel=0):
    """
    Calcula o n-ésimo termo da sequência de Fibonacci de forma recursiva,
    mostrando o rastreamento de cada chamada.

    Args:
      n: Um número inteiro não negativo.
      nivel: O nível de indentação para a exibição (usado para rastrear).

    Returns:
      O n-ésimo termo da sequência de Fibonacci.
    """
    indent = "  " * nivel  # Cria a indentação baseada no nível atual
    print(f"{indent}Chamada: fibonacci({n})")
    
    if n < 0:
        print(f"{indent}Erro: O índice deve ser um número inteiro não negativo.")
        return None
    
    # Caso base
    if n <= 1:
        print(f"{indent}Retornando {n}")
        return n
    
    # Passo recursivo
    else:
        # Chama as sub-funções para os termos anteriores
        resultado1 = fibonacci(n - 1, nivel + 1)
        resultado2 = fibonacci(n - 2, nivel + 1)
        
        soma = resultado1 + resultado2
        print(f"{indent}Somando {resultado1} + {resultado2} = {soma}")
        print(f"{indent}Retornando {soma}")
        return soma

# Exemplo de uso:
termo = 4
print(f"Calculando fibonacci({termo}) e rastreando as chamadas:\n")
fibonacci(termo)