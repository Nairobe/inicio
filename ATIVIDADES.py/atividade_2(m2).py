import os
os.system('clear||cls')

nota = int(input("DIGITE SUA NOTA:"))

if nota > 7:
  print("aprovado")
elif nota < 6.9 or nota <= 4:
  print("recuperação")
else:
  print("reprovado")
