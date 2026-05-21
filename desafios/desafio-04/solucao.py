# Desafio 04 — Tabuada Personalizada
# Aluno: Robert Gonzaga
# Data:  21/05

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
stop = False

while stop != True :
  num = int(input("Digite um número de 1 a 10\nDigite 0 para sair\n"))

  if num > 0 and num <= 10 :
    print(f"Tabuada do {num}")
    for i in range(1, 11) :
      print(f"{num} x {i} = {num * i}")
  
  elif num == 0 :
    print("Programa finalizado")
    stop = True
  
  else :
    print("Número Inválido!")