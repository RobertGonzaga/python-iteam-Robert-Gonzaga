# Explicação — Desafio 01

**Aluno:** Robert Gonzaga  
**Data:** 20/05

---

## O que meu programa faz

Meu programa pergunta ao usuario seu nome, ano de nascimento e hobbies;
depois ele subtrai 2026 (ano atual) menos o ano de nascimento, assim obtemos a idade da pessoa;
depois ele imprime na tela essas informacoes

---

## Resposta à Pergunta Obrigatória

> Por que é necessário converter o resultado do `input()` antes de calcular a idade? O que acontece se não converter?

é preciso converter pois a funcao "input()" recebe por padrao string;
logo, mesmo que o usuario digite numeros, eles não serão tratados como tal, impossibilitando fazer calculos, nesse caso eu utilizei a funcao "int()", convertendo o input em inteiro

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
pesquisei a sintaxe de conversao para inteiro em python
