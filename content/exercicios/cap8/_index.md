---
title: "Capítulo 8 — Ordenação"
description: "Exercícios do capítulo 8 do livro (Ordenação), com soluções comentadas."
weight: 8
bookCollapseSection: true
---
# Capítulo 8 — Ordenação

[← Voltar](../)

---
## 8.1 Ordenando uma Lista
### Exercício 8.1 — Bolha com nomes
Python pode comparar strings diretamente com os operadores de comparação
usuais. Use o algoritmo da ordenação por borbulhamento para ordenar uma lista
de nomes. Para tanto, basta substituir a lista de números original por uma com
nomes, por exemplo:

`lista = ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']`

(como curiosidade, estes são os nomes dos atores do grupo Monty Python,
inspiração para o nome da linguagem Python)

Coloque mais palavras, e veja a diferença entre letras maiúsculas e
minúsculas. Qual palavra vem antes, 'Cleese', com c maiúsculo, ou 'cleese'?

{{< solucao >}}
### Exercício — Bolha com nomes
{{< codefile "assets/code/ex8.1_bolha_nomes.py" >}}

{{< /solucao >}}

---
### Exercício 8.2 — Bolha com sentinela
Uma melhoria pode ser feita no algoritmo da bolha com sentinela: note que a
cada passagem pela lista, a última troca de elementos deixa um elemento na sua
posição correta. Após esta posição, os elementos têm de estar ordenados e nos
próximos passos não é necessário ir além desta posição. Escreva um programa que
guarde esta posição e que a utilize como sentinela. O algoritmo a ser
implementado em Python é o seguinte:

```
Seja uma lista com n elementos
limite = tamanho da lista - 1
ultimo = limite
Enquanto limite != 0:
  limite = 0
  Para i variando entre 0 e ultimo - 1:
     Se lista[i] > lista[i+1]
         troque elementos de posição.
         limite = i
  ultimo = limite
```

Este algoritmo usa a variável `limite` para indicar qual elemento não
sabemos ainda estar na sua posição final. A variável `ultimo` indica o índice
no qual foi realizada a última troca entre posições de elementos. Se nenhuma
troca for realizada, `limite` permanece em zero e o algoritmo termina.

{{< solucao >}}
### Exercício — Bolha com sentinela
{{< codefile "assets/code/ex8.2_bolha_sentinela.py" >}}

{{< /solucao >}}

---
## 8.2 Ordenação por Inserção
### Exercício 8.3 — Ordenação por inserção
A partir da definição do algoritmo de ordenação, siga os mesmos passos de
desenvolvimento do algoritmo da bolha para chegar à sua própria versão do
algoritmo de ordenação por inserção.

{{< solucao >}}
### Exercício — Ordenação por inserção
{{< codefile "assets/code/ex8.3_insercao.py" >}}

{{< /solucao >}}

---
### Exercício 8.4 — Inserção recursiva
Um algoritmo recursivo para o ordenamento por inserção seria:

1. Se lista tem tamanho igual ou menor que 1, retorne
2. Recursivamente ordene os primeiros n−1 elementos
3. Insira o último elemento na parte já ordenada

Você poderia escrever a função desse algoritmo? Perceba que a inserção ainda
deve ser feita com um laço. Este algoritmo não ganha em ser implementado
recursivamente. O desempenho das duas versões é equivalente.

{{< solucao >}}
### Exercício — Inserção recursiva
{{< codefile "assets/code/ex8.4_insercao_recursiva.py" >}}

{{< /solucao >}}

---
### Exercício 8.5 — Intercalação de listas
Escreva uma função que intercale duas listas. O programa deve receber duas listas
já ordenadas e criar uma terceira lista que é o resultado da intercalação dos
elementos dos dois conjuntos de modo que a nova lista também esteja ordenada.

{{< solucao >}}
### Exercício — Intercalação de listas
{{< codefile "assets/code/ex8.5_intercala.py" >}}

{{< /solucao >}}

---
### Exercício 8.6 — Mergesort
Um algoritmo bem eficiente de ordenação é o mergesort. Seu princípio é a
divisão do conjunto a ser ordenado em duas partes, ordenar cada parte, e depois
fazer uma fusão (merge) entre os dois conjuntos ordenados. Cada vez
que for ordenar uma metade, o algoritmo é chamado recursivamente, dividindo à
metade cada parte que deveria ordenar. Quando a parte a ser ordenada contiver
apenas 1 elemento, o algoritmo retorna.

Escreva uma função mergesort que receba uma lista e ordene-a segundo esse
algoritmo. Para a função de intercalação, use a que você criou no exercício
anterior. O algoritmo é o seguinte:

```
merge_sort(a)
  se lista tem tamanho menor ou igual a 1 retorne a
  m = tamanho de a dividido por 2
  a0 = merge_sort(a[:m])
  a1 = merge_sort(a[m:])
  merge(a0, a1, a)
```

No algoritmo, `a0` é a primeira metade da lista; `a1` é a segunda metade e `a` é a
lista que guarda a intercalação das duas.

{{< solucao >}}
### Exercício — Mergesort
{{< codefile "assets/code/ex8.6_mergesort.py" >}}

{{< /solucao >}}

---

## Quer ir além?

Se você quiser se desafiar com novos problemas, sem solução disponível:

👉 [Exercícios extras do Capítulo 8](../../extras/cap8/)

e também:

👉 [Exercícios extras do Capítulo 9](../../extras/cap9/)