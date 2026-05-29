# Desafio 08 — Banco Digital
# Aluno: Robert Gonzaga
# Data:  29/05

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
class ContaBancaria:
  def __init__(self, titular, saldo_inicial):
    self.titular = titular
    self.saldo = saldo_inicial

  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
      print("Valor inválido para depósito.")

  def sacar(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor
      print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
      print("Saldo insuficiente para saque.")

  def exibir_extrato(self):
    print("\n=== EXTRATO BANCÁRIO ===")
    print(f"Titular: {self.titular}")
    print(f"Saldo atual: R$ {self.saldo:.2f}")

conta = ContaBancaria("Carlos", 1000)

conta.depositar(500)
conta.sacar(300)
conta.sacar(1500)

conta.exibir_extrato()