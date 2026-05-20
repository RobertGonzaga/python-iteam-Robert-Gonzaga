# Desafio 02 — Calculadora de IMC
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura**2)

print(f"Olá {nome}, seu IMC é {imc:.2f}")