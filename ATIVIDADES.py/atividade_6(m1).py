# Crie uma função recursiva soma_n(n)
#  que retorne a soma de todos os números de 1 até n
import os
os.system("cls||clear")

numero = int(input("DIGITE UM NÚMERO: "))
n = numero
def soma_n(n):
  
    if n <= 0:
        return 
    
    if n == 1:
        return 1
    
    else:
        return n + soma_n(n + 1)

print(f"soma dos números: {soma_n}")