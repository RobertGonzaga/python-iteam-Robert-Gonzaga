# Desafio 01 — Seu Primeiro Script
# Aluno: Robert Gonzaga
# Data:  20/05

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

nome = input("Digite seu nome: ")
ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
hobbies = input("Digite seus hobbies: ")

idade = 2026 - ano_de_nascimento

print(f"{nome} tem {idade} anos")
print(f"Hobbies: {hobbies}")