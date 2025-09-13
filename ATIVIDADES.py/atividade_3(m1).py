import os
os.system('clear||cls')

print("1 2 3 4 5 6 7 ")
dia_da_semana = input("ESCOLHA UM DIA DA SEMANA: ")

match dia_da_semana:
     
    case "1":
        print("DOMINGO")
    case "2":
        print("SEGUNDA")
    case "3":
        print("TERÇA")
    case "4":
        print("QUARTA")
    case "5":
        print("QUINTA")
    case "6":
        print("SEXTA")
    case "7":
        print("SABADO")               
    case _:
        print("DIA INVALIDO")   
