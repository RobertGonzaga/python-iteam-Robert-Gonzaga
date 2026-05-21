# Desafio 03 — Sistema de Multas
# Aluno: Robert Gonzaga
# Data:  20/05

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

velocidade_atual = int(input("Qual a velocidade atual do carro? "))

if velocidade_atual > 80 :
  print("Multado! Você excedeu o limite de 80km/h")
  multa = (velocidade_atual - 80) * 7
  print(f"Sua multa é de {multa}$")
else :
  print("Boa viagem! Dirija com segurança")