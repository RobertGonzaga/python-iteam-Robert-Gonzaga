# Desafio 06 — Bio-Cadastro
# Aluno: Robert Gonzaga
# Data:  29/05

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

equipe = []
stop = False

while stop == False :
  print("Digite 'sair' para sair")
  nome = input("Digite o nome do funcinario: ")
  if nome == "sair":
    stop = True
  else :
    cargo = input("Digite o cargo do funcionario: ")

    colaborador = {
      "nome": nome,
      "cargo": cargo
    }

    equipe.append(colaborador)

for funcionario in equipe :
  print(f"Funcionário: {funcionario["nome"]} | Cargo: {funcionario["cargo"]}")