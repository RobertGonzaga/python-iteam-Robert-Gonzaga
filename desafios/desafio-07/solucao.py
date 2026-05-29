# Desafio 07 — Bio-Calculadora
# Aluno: Robert Gonzaga
# Data:  29/05

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
from funcoes_mat import area_circulo, volume_esfera, hipotenusa

print("Escolha uma opcao:")
print("1 - Área do círculo")
print("2 - Volume da esfera")
print("3 - Hipotenusa")

resposta = int(input("Digite a opcao desejada: "))

if resposta == 1 :
  raio = float(input("Digite o valor do raio: "))
  resultado = area_circulo(raio)
  print(f"Área do círculo = {resultado}")

elif resposta == 2 :
  raio = float(input("Digite o valor do raio: "))
  resultado = volume_esfera(raio)
  print(f"Volume da esfera = {resultado}")

elif resposta == 3 :
  cateto1 = float(input("Digite o valor do cateto 1: "))
  cateto2 = float(input("Digite o valor do cateto 2: "))
  resultado = hipotenusa(cateto1, cateto2)
  print(f"Hipotenusa = {resultado}")

else :
  print("Opcao Inválida!")
