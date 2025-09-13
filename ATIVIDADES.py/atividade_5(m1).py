#crie uma função recursiva chamada fatorial (n) que receba 
# um numero inteiro positivo e retorne o fatorial de n
import os
os.system("cls||clear")

numero = int(input('digite um número: '))
n = numero
def fatorial(n):
   
    if n < 0:
        return 
    
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fatorial(n - 1)
print(f"O FATORIAL DE {n} É: {fatorial(n)}")