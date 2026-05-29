# Desafio 05 — Gerenciador de Compras
# Aluno: (Robert Gonzaga)
# Data:  (28/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

stop = False
produtos = []

while stop != True :
  resposta = input("Digite o produto que quer adicionar à lista\nDigite 'fim' para sair\n")

  if resposta == "fim" :
    stop = True
  else :
    produtos.append(resposta)

print("Lista de produtos:")
for item in produtos :
  print(item)
print(f"Total de produtos: {len(produtos)}")