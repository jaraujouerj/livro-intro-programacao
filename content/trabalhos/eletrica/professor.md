---
title: "Guia do professor — Elétrica"
description: "Guia do professor para o trabalho de Engenharia Elétrica: objetivos, armadilhas intencionais, perguntas e rubrica."
weight: 2
---
📄 [Enunciado em PDF (entregue aos alunos)](../trabalho_final_eletrica.pdf) · 📦 [Dados](../dados_eletrica.zip)

---

## 1. Contexto no curso

Mesma estrutura do [trabalho de Produção](../../producao/professor/), adaptada à Engenharia Elétrica. Integra o **Bloco 4** e pressupõe as ferramentas vistas nas **Aulas 21** (NumPy) e **27 a 29** (Matplotlib e Pandas).

| Aula | Uso no trabalho |
|---|---|
| 26 | Lançamento: apresentar o tema e formar os grupos |
| 21, 27 a 29 | Ferramentas: `numpy`, gráficos, `DataFrame`, `groupby`, `merge` |
| 30 | **Etapa 0** (especificação) |
| 31 e 32 | Implementação, com testes de sanidade |
| 33 | Revisão crítica do código e dos testes |
| 34 e 35 | Relatório e **defesa oral** |

Reforça a mesma exigência do curso: **especificar antes de codar, usar IA de forma documentada e validar tudo com testes**.

## 2. Dados

Dados **fictícios**, gerados por script, de um prédio universitário trifásico (127/220 V) ao longo de setembro de 2026:

* `medicoes_horarias.csv`: 720 leituras horárias (tensões, correntes, *P*, *Q*, energia);
* `consumo_circuitos.csv`: consumo diário de 6 circuitos (180 registros);
* `cargas_instaladas.csv`: cadastro dos circuitos.

Foram construídos para ter **consistência física**: as potências por circuito somam a potência total, e *Q* decorre do fator de potência típico de cada tipo de carga (motores têm *FP* menor que iluminação e servidores). Por isso a soma de `energia_kwh` das medições bate com a soma dos circuitos, o que permite um bom teste de sanidade.

## 3. Objetivo

Responder, como engenheiro(a) de eficiência energética: **a instalação opera dentro dos limites de qualidade de energia e onde há mais oportunidade de economia?** O aluno deve **priorizar** ações e justificar com evidência numérica e visual, e não apenas descrever os dados.

## 4. Armadilhas intencionais (o que observar)

* **Falta de energia *versus* falha do medidor.** Há uma janela de horas em que tudo vai a **zero** (dado real: apagão) e outra em que a **tensão está ausente** (`NaN`: o medidor falhou, a instalação seguiu operando). Quem aplica `fillna(0)` ou `dropna()` sem pensar distorce a média de tensão e a contagem de horas fora da faixa. É o equivalente, aqui, do `defeito` vazio do trabalho de Produção. As datas exatas ficam no script de geração, com o professor.
* ***FP* com potência nula.** Durante o apagão *P* = *Q* = 0 e o *FP* não é definido (0/0). O aluno precisa tratar isso.
* **Normalização.** Comparar consumo de circuitos exige olhar o **fator de carga** (o circuito que mais consome não é necessariamente o mais utilizado em relação à sua potência instalada).
* **Fases diferentes, comportamentos diferentes.** As três fases não são iguais: vale checar fase a fase, e não só a média.
* **Associação não é causa.** A queda de tensão acompanha a demanda; o aluno deve interpretar a relação com cuidado e sem exagero.

## 5. O que cada pergunta ensina

1. **Demanda máxima e curva de carga.** Conceito de demanda, perfil de utilização, `groupby` por hora e comparação dia útil × fim de semana.
2. **Fator de potência abaixo de 0,92.** Cálculo de *S* e *FP*, filtragem condicional e conexão com a legislação (multa por baixo FP).
3. **Tensão em 117 V a 133 V.** Qualidade de energia, contagem de violações por fase, dispersão tensão × potência e ajuste linear com `numpy.polyfit`.
4. **Consumo e fator de carga por circuito.** `merge` entre fontes, indicador normalizado e priorização (Pareto).

**Opcionais:** desequilíbrio entre fases, dimensionamento de banco de capacitores e comparação de tarifas.

{{< callout type="warning" >}}
**Conferir as referências.** O limite de *FP* (0,92) e a faixa de tensão adequada (117 V a 133 V para 127 V) seguem a regulamentação da ANEEL (PRODIST, Módulo 8) como foram usados aqui. Confira a versão vigente antes de aplicar o trabalho. As tarifas do item opcional são **fictícias**.
{{< /callout >}}

## 6. Visualizações mínimas

* **Série temporal** da demanda: dias atípicos (inclusive o apagão).
* **Curva de carga:** média por hora, dia útil × fim de semana.
* **Histograma/boxplot de tensão** com os limites marcados.
* **Barras ou Pareto:** consumo por circuito, em kWh e em %.

Todo gráfico precisa de título, rótulos com unidade e, quando fizer sentido, legenda.

## 7. Rubrica sugerida

| Critério | Peso |
|---|---|
| Especificação prévia (Etapa 0): clareza das perguntas e suposições | 15% |
| Correção técnica do código (`pandas`, `numpy`, `matplotlib`) | 25% |
| Qualidade da interpretação: conecta números a decisões de engenharia | 25% |
| Log de uso de IA: honestidade e criticidade | 15% |
| Testes de sanidade (Etapa 5) | 10% |
| Defesa oral: explicar qualquer trecho do próprio código | 10% |

## 8. Observação pedagógica

Como no trabalho de Produção, não há uma "resposta certa" única para "o que fazer primeiro". É proposital: o que não se terceiriza para a IA é decidir **qual pergunta vale a pena fazer** e **o que os números significam para quem vai agir** (corrigir o fator de potência? reforçar a alimentação? remanejar cargas de horário?). Ler o CSV, agrupar e plotar é a parte mais fácil de obter ajuda de IA; a leitura crítica do resultado é trabalho do engenheiro.
