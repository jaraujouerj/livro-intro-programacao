---
title: "Guia do professor — Produção"
description: "Guia do professor para o trabalho de Engenharia de Produção: objetivos, armadilhas intencionais, perguntas e rubrica."
weight: 2
---
# Trabalho de Engenharia de Produção — Guia do professor

[← Trabalho (aluno)](../) · [Trabalhos](../../)

📄 [Enunciado em PDF (entregue aos alunos)](../trabalho_final_algoritmos.pdf) · 📦 [Dados](../dados_producao.zip)

---

## 1. Contexto no curso

O trabalho integra o **Bloco 4** (projeto final). Pressupõe que os alunos já viram as ferramentas nas **Aulas 27 a 29** (Matplotlib, Pandas 1 e 2) e dialoga com o restante do bloco:

| Aula | Uso no trabalho |
|---|---|
| 26 | Lançamento: apresentar o tema e formar os grupos |
| 27 a 29 | Ferramentas: gráficos, `DataFrame`, `groupby`, `merge` |
| 30 | **Etapa 0** (especificação) |
| 31 e 32 | Implementação, com testes de sanidade |
| 33 | Revisão crítica do código e dos testes |
| 34 e 35 | Relatório e **defesa oral** |

O trabalho reforça a mesma exigência do curso todo: **especificar antes de codar, usar IA de forma documentada e validar tudo com testes**.

## 2. Dados

Dois CSV de um mês de operação de uma linha fictícia com 4 máquinas (M1 a M4): `producao_mensal.csv` (1.281 peças) e `paradas_mensal.csv` (44 paradas). Os arquivos compartilham `data` e `maquina`, o que obriga o aluno a praticar **`merge`**: não é só ler um CSV isolado, é combinar duas fontes, como numa análise real (dados de PCP raramente vêm de uma tabela só).

Descrição das colunas na [página do aluno](../#2-dados-fornecidos).

## 3. Objetivo

Produzir uma análise que ajude um gestor fictício a responder: **"Onde estamos perdendo eficiência e o que vale a pena investigar primeiro?"**

O aluno não deve apenas descrever os dados, e sim **priorizar problemas** e justificar a priorização com evidência numérica e visual.

## 4. O que observar em cada etapa

* **Etapa 0 (especificação).** Entregue separadamente e com nota própria: é a disciplina de "especificar antes de pedir para a IA". Peça perguntas verificáveis e suposições explícitas sobre os dados.
* **Etapa 1 (preparação).** Armadilha intencional: `defeito` vazio **não é dado faltante**, é ausência de defeito. Quem aplica `dropna()` cegamente perde todas as peças aprovadas.
* **Etapa 4 (log de IA).** O log é parte da nota, não um anexo. Não é permitido copiar um notebook inteiro gerado por IA sem ele.
* **Etapa 5 (testes).** Pelo menos 3 `assert`. Exemplo: a soma das contagens de status por máquina é igual ao total de linhas da máquina.
* **Etapa 6 (relatório e defesa).** Interpretação *para o gestor*, não só gráficos. Na defesa (5 a 7 min por aluno ou dupla), peça que expliquem qualquer célula, inclusive as geradas com IA.

## 5. Perguntas mínimas e o que cada uma ensina

1. **Maior taxa de retrabalho + descarte por máquina.** Proporção, não contagem bruta, para reforçar o cuidado com **normalização** (máquinas que produzem mais têm mais ocorrências absolutas).
2. **Tempo de ciclo entre turnos ou operadores.** Pista de diferença de treinamento, fadiga ou variação de setup.
3. **Motivos de parada que mais consomem tempo.** É um **Pareto de paradas**, que conecta com a análise de causas de perda de disponibilidade da Engenharia de Produção.
4. **Relação entre paradas e defeitos.** Entra o `merge` por `data` + `maquina`. Pede leitura crítica dos números, sem estatística inferencial formal.

**Opcionais:** (5) aproximação simplificada de **OEE** por máquina e (6) destaque de operador por máquina.

## 6. Visualizações mínimas

* **Barras:** taxa de retrabalho/descarte por máquina.
* **Boxplot:** tempo de ciclo por máquina ou turno. Introduz a ideia de **variabilidade**, não só média.
* **Pareto** (barras + linha acumulada): paradas por tempo perdido. É clássico da área e boa ocasião para ensinar dois eixos y no `matplotlib`.
* **Série temporal:** produção ou taxa de defeito diária, para ver tendência ou dias atípicos.

Todo gráfico precisa de título, rótulos de eixo e, quando fizer sentido, legenda: é o mínimo para ser lido por quem não o fez.

## 7. Rubrica sugerida

| Critério | Peso |
|---|---|
| Especificação prévia (Etapa 0): clareza das perguntas e suposições | 15% |
| Correção técnica do código (`pandas`/`matplotlib`) | 25% |
| Qualidade da interpretação: conecta números a decisões de produção, não só descreve gráficos | 25% |
| Log de uso de IA: honestidade e criticidade sobre o que foi corrigido | 15% |
| Testes de sanidade (Etapa 5) | 10% |
| Defesa oral: explicar qualquer trecho do próprio código | 10% |

## 8. Observação pedagógica

O trabalho é deliberadamente mais aberto que os exercícios dos capítulos: não há uma "resposta certa" única para "onde investigar primeiro". Isso é proposital. No mundo real do PCP, essa é a parte que não se terceiriza para a IA: decidir **qual pergunta vale a pena fazer** e **o que os números realmente significam** para quem vai agir sobre eles.

O código em si (ler CSV, agrupar, plotar) é a parte mais fácil de obter ajuda de IA. A **leitura crítica do resultado** continua sendo trabalho do engenheiro.
