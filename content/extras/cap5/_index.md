---
title: "Capítulo 5 — Organizando a Informação"
weight: 5
bookCollapseSection: true
---
{{< katex />}}

# 📘 Exercícios — Capítulo 5 
# Organizando a Informação

[← Voltar](../)

---
### Exercícios propostos sobre Listas e Processamento

**1.** Crie uma lista com os nomes dos sete dias da semana e utilize **índices negativos** para imprimir o último e o penúltimo dia.

**2.** Escreva um programa que receba 10 números inteiros, armazene-os em uma lista e, em seguida, utilize um laço `for` para imprimir a **soma apenas dos valores** que estão em posições (índices) ímpares.

**3.** Dada uma lista de números, utilize o comando `enumerate()` para percorrer a lista e imprimir uma mensagem no formato: "O elemento de índice X tem o valor Y".

**4.** Demonstre a diferença entre o uso de **atribuição compacta** (`i += 5`) e a forma tradicional (`i = i + 5`) em um programa que atualiza os valores de uma lista de preços.

**5.** Escreva uma função que receba uma lista de números e utilize o método `append()` para criar uma nova lista contendo apenas os números positivos da lista original.

### Exercícios sobre Listas por Compreensão e Operações

**6.** Utilize **listas por compreensão** para gerar uma lista contendo as potências de 3 (de \\(3^0\\) até \\(3^{10}\\)).

**7.** Crie uma lista de nomes e use a compreensão de listas com um **filtro (`if`)** para gerar uma nova lista contendo apenas os nomes que começam com a letra "A".

**8.** Dada a lista `[1,2,3]`, utilize a **multiplicação de listas** para gerar o resultado `[1,2,3,1,2,3,1,2,3]`.

**9.** Escreva um código que encontre a **diferença entre duas listas** (elementos que estão na lista A mas não na B) utilizando listas por compreensão.

### Exercícios sobre Fatiamento e Métodos de Lista

**10.** Dada uma lista com 20 elementos, utilize o **fatiamento (`slice`)** para extrair uma sublista que contenha apenas os elementos do índice 5 ao 15, pulando de 2 em 2.

**11.** Use o fatiamento com **passo negativo** para inverter completamente uma lista de strings.

**12.** Demonstre o uso dos métodos `insert(i, x)` e `remove(x)` em uma lista de tarefas, inserindo uma tarefa prioritária no início e removendo uma tarefa concluída pelo seu nome.

**13.** Explique e demonstre via código a diferença entre o método `sort()` (que ordena a própria lista) e a função `sorted()` (que gera uma nova lista ordenada).

**14.** Crie um programa que identifique o **valor mínimo e o máximo** de uma lista digitada pelo usuário sem utilizar as funções `min()` e `max()`, apenas percorrendo a lista com um laço.

### Exercícios sobre Matrizes, Dicionários e Tuplas

**15.** Crie uma **matriz 3x3** (lista de listas) preenchida com zeros usando listas por compreensão e, em seguida, altere todos os elementos da diagonal principal para o valor 1.

**16.** Escreva um programa que utilize um **dicionário** para armazenar o nome de 5 produtos e seus respectivos preços. O programa deve permitir que o usuário consulte o preço de um produto digitando seu nome.

**17.** Utilize o método `get()` em um dicionário de contatos para buscar um telefone, garantindo que o programa não trave caso o nome pesquisado não exista (retornando `None`).

**18.** Crie uma **tupla** que represente uma data (dia, mês, ano) e tente alterar o valor do ano. Capture a exceção gerada e explique por que isso acontece com base na **imutabilidade** das tuplas.

### Exercícios sobre Clonagem e NumPy

**19.** Escreva um programa que demonstre o "efeito colateral" de criar um **apelido (*alias*)** para uma lista (`lista2 = lista1`) e como a **clonagem** utilizando `[:]` evita que alterações em uma lista afetem a outra.

**20.** Utilizando o módulo **NumPy**, crie dois arrays de 5 números cada e realize a soma e a multiplicação elemento a elemento entre eles, comparando o resultado com o que aconteceria se fossem listas comuns de Python.

---