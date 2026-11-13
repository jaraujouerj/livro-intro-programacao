---
title: "Capítulo 8 — Ordenando Coisas"
description: "Exercícios adicionais do capítulo 8 (Ordenando Coisas), para praticar, sem solução publicada."
weight: 8
bookCollapseSection: true
---

# Capítulo 8 — Ordenando Coisas

*Exercícios adicionais, sem solução publicada.*

[← Voltar](../)

---

### Exercícios de Lógica e Rastreamento

**1. Rastreamento Manual:** Execute manualmente o algoritmo da bolha (sem sentinela) para a lista: **5, 1, 4, 2, 8**. Desenhe o estado da lista após cada troca no primeiro passo.

**2. O Pior Caso:** Crie uma lista de 5 elementos que represente o "pior caso" para o algoritmo de ordenação por inserção e explique por que ela exige o número máximo de movimentações.

**3. Identificação de Passos:** No algoritmo da bolha aplicado à lista **8, 7, 6, 5, 4**, quantos passos totais (iterações do laço externo) seriam necessários se utilizarmos a versão **com sentinela**?.

**4. Ordenação de Nomes:** Utilize o algoritmo de inserção para ordenar manualmente a seguinte lista de nomes: **Zico, Pelé, Garrincha, Ademir, Tostão**.

**5. Sensibilidade à Caixa:** Explique o que acontece ao ordenar a lista **‘Cleese’, ‘cleese’, ‘Idle’, ‘idle’** usando o algoritmo da bolha. Qual a ordem final e por quê?.

### Exercícios de Ordenação (Python)

**6. Ordem Decrescente (Bolha):** Modifique a função `bubblesort` (Programa 8.2) para que ela ordene a lista em **ordem decrescente**.

**7. Ordem Decrescente (Inserção):** Modifique a função `insert_sort` (Programa 8.4) para que ela ordene a lista em **ordem decrescente**.

**8. Contador de Trocas:** Altere o algoritmo da bolha para que ele, ao final da execução, imprima o **número total de trocas** realizadas entre elementos.

**9. Contador de Comparações:** Altere o algoritmo de inserção para que ele conte e exiba quantas vezes a **comparação** `lista{i} > elemento` foi testada.

**10. Sentinela Visual:** Modifique o Programa 8.3 para que ele imprima a lista apenas nas rodadas em que a sentinela `fora_de_ordem` for acionada (ou seja, quando houver trocas).

**11. Ordenação de Floats:** Crie um programa que gere uma lista com 10 números de **ponto flutuante** aleatórios e utilize o `insert_sort` para ordená-los.

**12. Limite Otimizado:** Implemente o exercício 8.2 do livro, criando a variável `limite` para diminuir a área de varredura do laço interno a cada passagem.

**13. Ordenação de Tuplas (Preço):** Dado um dicionário de produtos e preços, transforme-o em uma lista de tuplas no formato **(preço, nome)** e ordene-a pelo preço usando `insert_sort`.

**14. Busca após Ordenação:** Escreva um programa que ordene uma lista usando o método da bolha e, em seguida, peça ao usuário um valor para realizar uma **busca binária** (conceito do Capítulo 2).

**15. Ordenação de Strings por Tamanho:** Modifique o algoritmo de inserção para que ele ordene uma lista de strings não por ordem alfabética, mas pelo **tamanho (quantidade de caracteres)** de cada string.

**16. Par ou Ímpar Primeiro:** Crie um algoritmo de ordenação customizado que coloque todos os **números pares** no início da lista (ordenados entre si) e os ímpares ao final (também ordenados).

### Desafios de Análise e Integração

**17. Comparação de Performance:** Escreva um script que gere uma lista de 500 números aleatórios e meça o tempo de execução (usando o módulo `time`) do `bubblesort` comparado ao `insert_sort`.

**18. Identificação de Estilo:** Aplique o formatador **yapf** ou o analisador **pylint** em uma de suas funções de ordenação e corrija os problemas de estilo apontados (como nomes de variáveis e docstrings).

**19. Proteção com Try...Except:** Adicione um bloco `try...except` na sua função de ordenação para capturar erros caso a lista contenha elementos que **não podem ser comparados** (ex: misturar números e strings).

**20. Ordenação de Matriz (Linhas):** Dada uma matriz 3x3 (lista de listas), aplique o algoritmo de ordenação para que os elementos de **cada linha** individual fiquem ordenados de forma crescente.
