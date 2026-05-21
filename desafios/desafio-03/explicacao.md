# Explicação — Desafio 03 — Sistema de Multas

**Aluno:** Robert Gonzaga
**Data:** 20/05

---

## O que meu programa faz

Meu programa pergunta a velocidade atual de um carro, com essa informacao e usando a estrutura condicional "if" "else" faz a verificacao se está acima ou dentro do limite de velocidade, se estiver acima ele calcula o valor da multa que é 7$ por km/h acima

---

## Resposta à Pergunta Obrigatória

> Por que usamos `elif` e não múltiplos `if` separados? Dê um exemplo concreto onde a diferença causaria um resultado errado.

"elif" funciona para fazer uma checagem em forma de escada, separando as condicoes e fazendo uma por vez até encontrar uma verdadeira;
se usarmos vários "if" isso pode causar entrada multipla em varios blocos de codigo, perdendo o controle sobre o mesmo.

se eu quisesse checar se a idade de alguem é maior que 18 ou maior que 60;
usando 2 "if", se a idade fosse 70 ela entraria nos 2 blocos pois satisfaz as 2 condicoes, o correto seria usar elif para verificar uma por vez.

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
nada
