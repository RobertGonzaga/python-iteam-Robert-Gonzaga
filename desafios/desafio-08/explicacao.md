# Explicação — Desafio 08 — Banco Digital

**Aluno:** Robert Gonzaga
**Data:** 29/05

---

## O que meu programa faz

O programa cria uma classe chamada ContaBancaria, que representa uma conta de banco.
No construtor (__init__), o programa recebe o nome do titular da conta e o saldo inicial. Esses dados são armazenados nos atributos self.titular e self.saldo.
O método depositar(valor) adiciona dinheiro ao saldo da conta, verificando antes se o valor informado é positivo.
O método sacar(valor) retira dinheiro da conta somente se houver saldo suficiente. Caso contrário, o programa exibe uma mensagem informando que o saldo é insuficiente.
O método exibir_extrato() mostra na tela o nome do titular e o saldo atual da conta.
Depois da criação da conta, o programa usa input() para receber os dados do usuário e exibe um menu com opções para depositar, sacar, mostrar o extrato ou sair do sistema.

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

É preciso usar self.saldo para que o valor da variavel nao seja perdido durante a execucao do programa, dessa forma ele pode ser atualizado
se fosse uma variavel comum ela deixaria de existir depois da execucao

---

## Dificuldades encontradas

A parte do construtor e de POO
