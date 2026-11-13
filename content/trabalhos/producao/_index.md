---
title: "Engenharia de Produção"
weight: 1
bookCollapseSection: false
---
# 🏭 Trabalho Final — Engenharia de Produção
# Análise de Dados de Produção com Python

[← Trabalhos](../) · [Guia do professor](professor/)

---

**Material para download**

* 📄 [Enunciado completo (PDF)](trabalho_final_algoritmos.pdf)
* 📦 [Dados (ZIP com os dois CSV)](dados_producao.zip), ou separados: [producao_mensal.csv](producao_mensal.csv) e [paradas_mensal.csv](paradas_mensal.csv)

---

## 1. Objetivo

Você vai atuar como analista de **PCP** (Planejamento e Controle da Produção) e receber dados brutos de uma linha de produção fictícia. Com base em evidência numérica e visual, responda: **onde a fábrica está perdendo eficiência e o que vale a pena investigar primeiro?**

O trabalho usa `pandas` (manipulação de dados) e `matplotlib` (visualização) e reforça três hábitos: especificar o problema antes de programar, usar IA de forma crítica e documentada, e testar o próprio código antes de confiar nele. As ferramentas são vistas nas [Aulas 27 a 29](../../slides/).

## 2. Dados fornecidos

Um mês de operação de **4 máquinas (M1 a M4)**.

**`producao_mensal.csv`** — uma linha por peça (1.281 registros)

| Coluna | Descrição |
|---|---|
| `id_peca` | identificador da peça |
| `data` | data de produção (AAAA-MM-DD) |
| `maquina` | M1 a M4 |
| `operador` | operador responsável |
| `turno` | Manha, Tarde ou Noite (sem acento no arquivo) |
| `timestamp` | data e hora exatas |
| `tempo_ciclo_seg` | tempo de ciclo, em segundos |
| `status` | Aprovado, Retrabalho ou Descarte |
| `defeito` | tipo de defeito (vazio quando Aprovado) |

**`paradas_mensal.csv`** — uma linha por parada (44 registros)

| Coluna | Descrição |
|---|---|
| `id_parada` | identificador da parada |
| `data` | data da parada |
| `maquina` | máquina que parou |
| `turno` | turno da parada |
| `motivo` | troca de ferramenta, manutenção corretiva, falta de material etc. |
| `duracao_min` | duração, em minutos |

Os dois arquivos se relacionam por `data` e `maquina`. Parte do trabalho exige **combinar as duas fontes** (`merge`), como na prática. A coluna `data` é carregada como texto: converta para `datetime` antes de qualquer análise temporal.

```python
import pandas as pd

producao = pd.read_csv("producao_mensal.csv")
paradas = pd.read_csv("paradas_mensal.csv")
producao["data"] = pd.to_datetime(producao["data"])
```

## 3. Entregas

| Etapa | O que fazer |
|---|---|
| **0. Especificação** | *Antes do código*, meia página com: as perguntas que vai responder (mínimo 4, ver seção 4); o gráfico ou tabela adequado a cada uma; as suposições sobre os dados (por exemplo, `defeito` vazio é dado faltante ou ausência de defeito?). **Entrega e nota separadas.** |
| **1. Preparação** | Carregar os CSV, corrigir tipos (datas) e tratar ausentes **de forma justificada**. Não use `dropna()` sem saber o que descarta. |
| **2. Análise** | Responder às perguntas da seção 4 com `groupby`, `merge` e agregações. |
| **3. Visualizações** | Os gráficos da seção 5, todos com título e rótulos de eixo. |
| **4. Log de uso de IA** | Prompt usado, o que a IA gerou e o que você corrigiu ou rejeitou, e por quê. |
| **5. Testes de sanidade** | Pelo menos **3 `assert`** que confiram os números com uma conta simples (ex.: a soma das peças por status de uma máquina é o total dela). |
| **6. Relatório final** | De 2 a 4 páginas (ou notebook comentado) com respostas, gráficos e **interpretação para quem decide**; o log de IA entra como seção separada. |

**Formato:** `.ipynb` ou `.py` comentado, especificação em arquivo separado, log de IA e relatório em PDF ou Markdown.

## 4. Perguntas obrigatórias

1. **Qual máquina tem a maior taxa de retrabalho + descarte?** Calcule como *proporção*, não como contagem: máquinas que produzem mais têm mais ocorrências em números absolutos.
2. **O tempo de ciclo varia de forma relevante entre turnos ou entre operadores?**
3. **Quais motivos de parada consomem mais tempo total no mês?**
4. **Há relação entre dias/turnos com mais paradas e dias/turnos com maior taxa de defeito?** (exige combinar os dois arquivos)

**Opcionais (pontuação extra):**

5. Calcule uma aproximação simplificada do **OEE** por máquina.
6. Algum operador se destaca, positiva ou negativamente, em alguma máquina?

> **OEE** (Overall Equipment Effectiveness) mede a eficiência real de uma máquina:
> `OEE = Disponibilidade × Desempenho × Qualidade`.
> *Disponibilidade* é o tempo em que a máquina funcionou em relação ao planejado (descontadas as paradas); *Desempenho* compara a velocidade real com a ideal; *Qualidade* é a fração de peças sem defeito (sem refugo nem retrabalho). Valores acima de 85% são considerados de classe mundial.

## 5. Gráficos obrigatórios

* **Barras:** taxa de retrabalho/descarte por máquina.
* **Boxplot:** distribuição do tempo de ciclo por máquina ou por turno (a caixa vai do 1º ao 3º quartil, com a mediana em uma linha).
* **Pareto** (barras + linha acumulada): motivos de parada por tempo total perdido.
* **Série temporal:** produção diária ou taxa de defeito diária ao longo do mês.

## 6. Avaliação

| Critério | Peso |
|---|---|
| Especificação prévia (Etapa 0): clareza das perguntas e das suposições | 15% |
| Correção técnica do código (`pandas`/`matplotlib`) | 25% |
| Interpretação: conectar os números a uma decisão de produção | 25% |
| Log de uso de IA: honestidade e criticidade | 15% |
| Testes de sanidade (Etapa 5) | 10% |
| Defesa oral | 10% |

**Defesa oral** (5 a 7 minutos por aluno ou dupla): o professor pode pedir que você explique qualquer célula do código, inclusive trechos gerados com apoio de IA. Não é pegadinha: é o que todo engenheiro enfrenta ao revisar código que não escreveu sozinho.

## 7. Regras sobre uso de IA

O uso é **permitido e incentivado**, com duas condições:

1. **Documente tudo** (Etapa 4). Um notebook inteiro gerado por IA e entregue sem o log é penalizado, mesmo que esteja correto.
2. **Você precisa explicar qualquer linha** na defesa oral. Se a IA gerou algo que você não entende, estude antes de entregar.

Pedir ajuda para lembrar a sintaxe de uma função do `pandas` ou do `matplotlib` é uso legítimo. O que não se delega é a parte central do trabalho: **decidir quais perguntas fazer aos dados e o que os resultados significam**.
