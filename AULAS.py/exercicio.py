def exercicio1():
    pilha = []
    for i in range(5):
        num = int(input(f"Digite o {i+1}º número: "))
        pilha.append(num)
    print("Pilha final:", pilha)

def exercicio2():
    pilha = [10, 20, 30, 40, 50]
    print("Pilha original:", pilha)
    pilha.pop()
    pilha.pop()
    print("Pilha após remover 2 elementos:", pilha)

def exercicio3():
    def topo_pilha(pilha):
        if len(pilha) > 0:
            return pilha[-1]
        return None

    pilha = [1, 2, 3, 4, 5]
    print("Topo da pilha:", topo_pilha(pilha))

def exercicio4():
    palavra = input("Digite uma palavra: ")
    pilha = list(palavra)
    palavra_invertida = ""
    while pilha:
        palavra_invertida += pilha.pop()
    print("Palavra invertida:", palavra_invertida)

def exercicio5():
    numero = int(input("Digite um número decimal: "))
    pilha = []
    if numero == 0:
        pilha.append(0)
    else:
        while numero > 0:
            pilha.append(numero % 2)
            numero //= 2
    binario = ""
    while pilha:
        binario += str(pilha.pop())
    print("Número em binário:", binario)

def exercicio6():
    historico = []
    while True:
        acao = input("Digite uma página ou 'voltar' / 'sair': ").strip()
        if acao.lower() == "sair":
            print("Encerrando histórico.")
            break
        elif acao.lower() == "voltar":
            if historico:
                historico.pop()
            else:
                print("Histórico vazio!")
        else:
            historico.append(acao)

        if historico:
            print("Página atual:", historico[-1])
        else:
            print("Nenhuma página aberta.")


# -------------------------------
# MENU PRINCIPAL
# -------------------------------
while True:
    print("\n=== MENU DE EXERCÍCIOS ===")
    print("1 - Inserir 5 números em uma pilha")
    print("2 - Remover 2 últimos elementos de uma pilha")
    print("3 - Mostrar topo da pilha")
    print("4 - Inverter palavra")
    print("5 - Converter decimal para binário")
    print("6 - Simular histórico do navegador")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        exercicio1()
    elif opcao == "2":
        exercicio2()
    elif opcao == "3":
        exercicio3()
    elif opcao == "4":
        exercicio4()
    elif opcao == "5":
        exercicio5()
    elif opcao == "6":
        exercicio6()
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")