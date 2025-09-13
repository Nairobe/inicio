import os 
os.system("cls || clear")

#atividade  de fixação
print("atividade 1")
matriz = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]
for algarismo in matriz:
    print(algarismo) 

for algarismo in matriz:
    soma = 0
    for elemento in algarismo:
        soma += elemento
print("soma dos algarismos ", soma)
print("======================================")
#===============================================
# matriz para armazenar as notas 
print("atividade 2")
notas = []
for i in range(3):
    nt = float(input(f"Digite a {i +1}ª nota:"))
    notas.append(nt)

media = sum(notas ) / len(notas)
print(f'media : {media}')


#===============================================
# funcao para calcular media dos valores da matriz
print("======================================")
print("atividade 3")

matriz = [
    [2 , 2, 2,],
    [2 , 2, 2,],
    [2 , 2, 2,]
]

def calcular(matriz):
    for algarismo in matriz:
        print(algarismo) 

    for algarismo in matriz:
        soma = 0
        for elemento in algarismo:
            soma += elemento
        return soma

print("soma dos algarismos ", soma)


