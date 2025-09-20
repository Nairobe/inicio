import os
os.system('cls||clear')
pilha = []

#push
pilha.append('Senai')
pilha.append('Dendezeiros')
pilha.append('Salvador')
pilha.append('32')
print("Elementos da pilha: " , pilha)

#=========================================

#pop( remover)
if len(pilha) > 0:
    p = pilha.pop()
    print("elemento removido:" , p )
    print("pilha apos pop:", pilha)
else:
    print("a pilha está vazia, não é possivel remover: ")

#==========================================

#peek (consulte o topo sm remover)
if len(pilha) > 0:
    print("topo da pilha:" , pilha [-1])
else:
    print("a pilha está vazia, não exite topo.")

#==============================================

#isEmpty (verifica se está vazia)
print("a pilha está vazia? " , len(pilha))

    
#============================================== 



