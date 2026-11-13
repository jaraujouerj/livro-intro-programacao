---
title: "Slides e Plano de Trabalho"
description: "Slides de todas as aulas de Algoritmos Computacionais I e plano de trabalho da disciplina, com download em PDF e código-fonte no GitHub."
type: docs
cascade:
  type: docs
---
Aqui estão os **slides das aulas** de *Algoritmos Computacionais I* e o **plano de trabalho** da disciplina, seguindo o livro *Introdução à Programação e aos Algoritmos* (J. A. Ribeiro, LTC, 2019). Cada aula tem uma apresentação em PDF, que abre em uma nova aba ao clicar no link.

Os slides citam os exercícios deste site (com solução comentada) e usam os exemplos de código do livro. A disciplina é dada a **alunos de engenharia em geral** (o material pode ser adaptado a qualquer curso introdutório de programação): os capítulos 1 a 6 e 9 formam o curso básico, e o último bloco acrescenta análise de dados com NumPy, Pandas e Matplotlib e um projeto final.

> 💻 **Código-fonte:** o LaTeX (Beamer) de todos os slides, os programas em Python citados em cada aula e os notebooks de Matplotlib e Pandas estão no [repositório do GitHub](https://github.com/jaraujouerj/algoritmos-computacionais-aulas). Você também pode [baixar tudo em um arquivo ZIP](https://github.com/jaraujouerj/algoritmos-computacionais-aulas/archive/refs/heads/main.zip). O material está sob licença livre (CC BY-SA para os slides, MIT para o código), então pode ser copiado e adaptado.

> ⚠️ **Engenharia de Computação:** o curso para Engenharia de Computação tem **duas apresentações extras**, que não fazem parte do curso genérico para as demais engenharias: **Recursão** (capítulo 7) e **Ordenação** (capítulo 8). Veja a seção [Aulas extras](#aulas-extras-engenharia-de-computação) no fim da página.

---

## Plano de trabalho

Esta é apenas uma proposta de trabalho. Ela se baseia em duas aulas semanais, cada uma de 1:40h. O professor é livre, obviamente, para adaptar 
este plano de aula para seu curso.

**Livro-texto:** RIBEIRO, João Araujo. *Introdução à Programação e aos Algoritmos*. Rio de Janeiro: LTC, 2019.

A disciplina tem **35 aulas** em 4 blocos. As aulas 15 e 25 são as provas e não têm slides.

### Bloco 1 — Computação essencial (aulas 1 a 4)

*Objetivo: contextualizar sem afogar em teoria.*

| Aula (PDF) | Conteúdo | Referência |
|:---:|---|---|
| [Aula 01](aula01_apresentacao.pdf) | Apresentação do curso: expectativas, avaliação, pensamento lógico, o que é um algoritmo | Prefácio |
| [Aula 02](aula02_representacao_informacao.pdf) | Representação da informação: decimal e binário, prefixos, octal e hexadecimal, complemento a 2, ponto flutuante, ASCII/Unicode | Cap. 1 (1.1–1.7) |
| [Aula 03](aula03_arquitetura_execucao.pdf) | Arquitetura e execução: modelo de von Neumann, CPU, memória, SO; o ambiente de trabalho (interpretador *vs.* scripts) | Cap. 1 (1.8–1.12) e Cap. 2 (2.1) |
| [Aula 04](aula04_pensamento_algoritmico.pdf) | Pensamento algorítmico: refinamentos sucessivos, fluxogramas e pseudocódigo | Cap. 2 (2.2–2.5) |

### Bloco 2 — Fundamentos de programação (aulas 5 a 15)

| Aula (PDF) | Conteúdo | Referência |
|:---:|---|---|
| [Aula 05](aula05_bases_da_programacao.pdf) | Bases da programação: identificadores, dados numéricos, tipos e constantes | Cap. 2 (2.6–2.9) |
| [Aula 06](aula06_estrutura_basica.pdf) | Estrutura básica de programa: sequência, entrada e saída, expressões | Cap. 3 (3.1.1) |
| [Aula 07](aula07_estruturas_decisao.pdf) | Estruturas de decisão: `if`, `elif`, `else`, condições compostas | Cap. 3 (3.1–3.4) |
| [Aula 08](aula08_iteracao.pdf) | Iteração: `while`, laços contados com `for`, condições complexas | Cap. 3 (3.1.3, 3.5–3.6) |
| [Aula 09](aula09_laboratorio_problemas.pdf) | Laboratório de problemas reais: validação, médias e regras | Cap. 3 (3.4) |
| [Aula 10](aula10_subalgoritmos.pdf) | Subalgoritmos: funções, fluxo de execução e `return` | Cap. 4 (4.1–4.3) |
| [Aula 11](aula11_parametros_escopo.pdf) | Parâmetros e escopo: variáveis globais e locais, vários retornos | Cap. 4 (4.4–4.6) |
| [Aula 12](aula12_modulos.pdf) | Organização e módulos: reuso e estruturação de programas maiores | Cap. 4 (4.2 e 4.6) |
| [Aula 13](aula13_modulos_excecoes.pdf) | Módulos e exceções: `math`, `random` e `try/except` | Cap. 4 (4.2, 4.7) |
| [Aula 14](aula14_revisao_cap1a4.pdf) | Exercícios e revisão dos capítulos 1 a 4 | Cap. 1 a 4 |
| 15 | **Prova 1** *(sem slides)* | Cap. 1 a 4 |

### Bloco 3 — Estruturas de dados e modularização (aulas 16 a 25)

| Aula (PDF) | Conteúdo | Referência |
|:---:|---|---|
| [Aula 16](aula16_sequencias_listas.pdf) | Estruturas de dados I: sequências e listas | Cap. 5 (5.1–5.2) |
| [Aula 17](aula17_processamento_listas.pdf) | Processamento de listas: fatiamento, compreensão e métodos | Cap. 5 (5.3–5.6) |
| [Aula 18](aula18_operacoes_listas.pdf) | Operações avançadas: clonando listas, listas como parâmetros | Cap. 5 (5.7–5.9) |
| [Aula 19](aula19_matrizes.pdf) | Matrizes: tabelas de dados experimentais e pequenas simulações | Cap. 5 (5.10–5.11) |
| [Aula 20](aula20_dicionarios_tuplas.pdf) | Dicionários e tuplas: dados associativos | Cap. 5 (5.12–5.13) |
| [Aula 21](aula21_numpy.pdf) | NumPy: vetores, operações vetorizadas e aplicações numéricas | Cap. 5 (5.14) |
| [Aula 22](aula22_strings.pdf) | Strings: manipulação de texto e formatação | Cap. 6 (6.1–6.3) |
| [Aula 23](aula23_arquivos.pdf) | Arquivos: leitura e escrita (inclui CSV) | Cap. 6 (6.4–6.5) |
| [Aula 24](aula24_revisao_estilo.pdf) | Revisão e exercícios: modularização, boas práticas e estilo de código | Cap. 4 a 6 e Cap. 9 |
| 25 | **Prova 2** *(sem slides)* | Cap. 4 a 6 |

### Bloco 4 — Análise de dados e projeto final (aulas 26 a 35)

Cada engenharia tem um trabalho voltado para a sua área: veja os [trabalhos por engenharia](../trabalhos/).

O projeto integra funções, estruturas de dados, arquivos, tratamento de erros e, quando aplicável, NumPy, Pandas e Matplotlib. Os grupos têm 2 ou 3 alunos e o projeto resolve um problema real da área da engenharia do curso. Antes da especificação, três aulas apresentam as ferramentas de análise de dados.

| Aula (PDF) | Conteúdo | Referência |
|:---:|---|---|
| [Aula 26](aula26_lancamento_projeto.pdf) | Lançamento do projeto: temas por engenharia, formação de grupos e esboço inicial | Cap. 9 (base) |
| [Aula 27](aula27_matplotlib.pdf) | Visualização de dados com Matplotlib: linhas, dispersão, histograma, *boxplot*, barras | Notebook de Matplotlib |
| [Aula 28](aula28_pandas_1.pdf) | Introdução ao Pandas: `DataFrame`, `read_csv`, `loc`/`iloc` e filtros | Notebook de Pandas |
| [Aula 29](aula29_pandas_2.pdf) | Pandas na prática: `groupby`, agregações, valores ausentes e gráficos | Notebook de Pandas |
| [Aula 30](aula30_especificacao.pdf) | Especificação do projeto | Cap. 9 |
| [Aula 31](aula31_implementacao_1.pdf) | Implementação 1: estrutura básica, funções principais e dados | Cap. 3 a 5 |
| [Aula 32](aula32_implementacao_2.pdf) | Implementação 2: listas e dicionários, arquivos e tratamento de erros | Cap. 4 a 6 |
| [Aula 33](aula33_refatoracao_testes.pdf) | Refatoração e testes: legibilidade, casos extremos e boas práticas | Cap. 9 |
| [Aulas 34 e 35](aula34_35_apresentacao.pdf) | Apresentação dos projetos e critérios de avaliação | — |

**Critérios de avaliação do projeto:** funcionalidade, organização do código, modularização e clareza na explicação.

---

## Aulas extras: Engenharia de Computação

O curso de Algoritmos para **Engenharia de Computação** tem **duas apresentações extras**, correspondentes aos capítulos 7 e 8 do livro. Elas **não** fazem parte do curso genérico para as demais engenharias. Sugestão: ministrá-las depois da Aula 23 (Arquivos) e antes da Prova 2.

| Aula (PDF) | Conteúdo | Referência |
|:---:|---|---|
| [Aula C1](C1_recursao.pdf) | Recursão: caso base e passo recursivo, pilha de chamadas, Fibonacci, eficiência e memoização | Cap. 7 |
| [Aula C2](C2_ordenacao.pdf) | Ordenação: método da bolha e sentinela, inserção, intercalação e *mergesort* | Cap. 8 |

Os exercícios correspondentes estão nos capítulos [7](../exercicios/cap7/) e [8](../exercicios/cap8/) deste site.

---

## Exercícios

Cada apresentação termina com a lista dos exercícios do livro relacionados à aula:

* [Exercícios do livro (com solução comentada)](../exercicios/)
* [Exercícios adicionais (para praticar mais)](../extras/)
