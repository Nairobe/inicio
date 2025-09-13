import os 
os.system("cls||clear")

def fibinacci(n):
#caso base
    if n == 0:
        return 0
    if n == 1:
        return 1
   
# caso recursivo
    return fibinacci(n -1) + fibinacci(n - 2)
#resultado
n = int(input("DIGITE UM NUMERO: "))
print(f"fibonacci({n}) = {fibinacci(n)}")