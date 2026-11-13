---
title: "Capítulo 9 — Um Pouco de Estilo"
description: "Atividades de prática do capítulo 9 do livro (Um Pouco de Estilo): planejamento, legibilidade, simplicidade e testes."
weight: 9
---
{{< callout type="info" >}}
**Sobre este capítulo.** O Capítulo 9 do livro trata de planejamento, legibilidade, simplicidade e testes. É um capítulo de **aconselhamento**, e por isso **não traz exercícios numerados**. As atividades abaixo (**A9.1 a A9.6**) são um complemento deste site: aprendem-se boas práticas **praticando-as**, e não apenas lendo sobre elas. Para perguntas de reflexão e discussão, veja também os [exercícios extras do Capítulo 9](../../extras/cap9/).
{{< /callout >}}

Estas atividades não têm uma única resposta correta. Cada uma termina com um **critério de autoavaliação**: se você conseguir marcar todos os itens, o trabalho está bom.

---

## 9.1 Pense antes de programar

### Atividade A9.1 — Reformule o problema
Um cliente pede: *"Quero um programa para controlar as notas dos alunos."*

Sem escrever nenhuma linha de código, responda por escrito:

1. Quais são as **entradas** do programa? E as **saídas**?
2. Quais **regras** precisam ser definidas (média simples ou ponderada, nota mínima para aprovação, arredondamento)?
3. Liste ao menos **cinco perguntas** que você faria ao cliente antes de começar.
4. Reescreva o pedido em **um parágrafo preciso**, sem ambiguidades.

**Critério de autoavaliação:**
- [ ] Alguém que não conhece o cliente conseguiria implementar o programa só com o seu parágrafo.
- [ ] Você definiu o que o programa *não* vai fazer.

*Relacionado às aulas 4, 26 e 30.*

---

### Atividade A9.2 — Casos-limite
Considere a função abaixo, que calcula a média de uma lista de notas:

```python
def media(notas):
    return sum(notas) / len(notas)
```

1. Liste **dez entradas** que podem causar problemas ou resultados inesperados (lista vazia, notas negativas ou maiores que 10, texto no lugar de número, e assim por diante).
2. Teste cada entrada no interpretador e anote o que acontece.
3. Corrija a função para tratar os casos que você considerar relevantes e **decida** o que ela deve fazer em cada um (devolver um valor especial? levantar uma exceção?).

**Critério de autoavaliação:**
- [ ] Você testou pelo menos um caso de cada tipo: vazio, valor extremo, tipo errado.
- [ ] Para cada caso, você consegue explicar *por que* escolheu aquele comportamento.

*Relacionado às aulas 13 e 33.*

---

### Atividade A9.3 — Refinamentos sucessivos
Escreva o algoritmo de um **caixa eletrônico simples** (consultar saldo, sacar e depositar), em três níveis:

1. **Nível 1:** de 4 a 6 passos gerais, em português.
2. **Nível 2:** detalhe cada passo em pseudocódigo (decisões e repetições).
3. **Nível 3:** só então escreva o código em Python, dividido em funções.

**Critério de autoavaliação:**
- [ ] Cada nível pode ser lido sem consultar os outros.
- [ ] O código final tem uma função para cada passo do nível 1.
- [ ] Você tratou saque maior que o saldo e valores negativos.

*Relacionado às aulas 4, 10 e 11.*

---

## 9.2 Legibilidade e simplicidade

### Atividade A9.4 — Caça aos erros de estilo
Reescreva o programa abaixo para que fique legível, **sem mudar o que ele faz**:

```python
def f(l):
    r=0
    for i in range(len(l)):
        if l[i]>0:
            r=r+l[i]
    n=0
    for i in range(len(l)):
        if l[i]>0:
            n=n+1
    if n==0:
        return 0
    else:
        return r/n
```

Passos sugeridos:

1. Descubra o que a função calcula e dê a ela um **nome** e uma *docstring*.
2. Renomeie as variáveis.
3. Elimine o código **duplicado** (os dois laços fazem a mesma varredura).
4. Simplifique, se possível, com *compreensão de listas*.
5. Formate o resultado com o **yapf** ou outro formatador e compare.

**Critério de autoavaliação:**
- [ ] Os mesmos testes dão o mesmo resultado antes e depois.
- [ ] Nenhum comentário explica o óbvio: os nomes já bastam.
- [ ] Nenhuma linha passa de 80 caracteres.

*Relacionado às aulas 24 e 33.*

---

### Atividade A9.5 — Revisão cruzada
Troque um programa seu (de qualquer capítulo anterior) com um colega. Ao receber o código dele, **sem executá-lo primeiro**:

1. Leia e escreva com suas palavras **o que o programa faz**.
2. Aponte **três melhorias** possíveis (nomes, funções muito longas, repetição, falta de tratamento de erros).
3. Anote **uma dúvida** de leitura: um trecho que você não entendeu de primeira.
4. Depois, execute e compare com o que você supôs.

Ao receber a revisão do seu código, responda: a dúvida do colega revela um problema de legibilidade?

**Critério de autoavaliação:**
- [ ] A descrição que o colega escreveu bate com o que você quis fazer.
- [ ] Você alterou o código a partir de pelo menos um comentário recebido.

*Relacionado às aulas 24 e 33.*

---

## 9.3 Juntando tudo

### Atividade A9.6 — Mini-especificação do projeto
Escolha o tema do seu projeto final (ou um deste capítulo) e escreva **uma página** contendo:

1. **Problema:** o que será resolvido e para quem.
2. **Funcionalidades:** de 3 a 5, em ordem de prioridade (o que fica para depois se faltar tempo?).
3. **Entradas e saídas:** formatos, arquivos, dados.
4. **Estrutura:** a lista das funções, cada uma com uma frase sobre o que faz.
5. **Plano de testes:** pelo menos cinco casos, incluindo casos-limite.

**Critério de autoavaliação:**
- [ ] Um colega consegue começar a programar a partir do seu documento.
- [ ] Cada funcionalidade corresponde a pelo menos uma função da estrutura.
- [ ] O plano de testes cobre entradas inválidas.

*Relacionado às aulas 26 e 30.*

---

👉 [Exercícios extras do Capítulo 9](../../extras/cap9/)
