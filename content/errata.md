+++
title = 'Errata'
description = 'Correções do livro Introdução à Programação e aos Algoritmos, organizadas por versão.'
date = 2026-11-13T09:36:51-03:00
draft = false
+++

# Errata

[← Voltar](../)

Esta página lista correções do livro organizadas por versão.  
Se encontrar um erro, entre em contato com o autor {{< email user="araujo+errata" domain="eng.uerj.br" >}}

---

## Versão 1.3

### Capítulo 2 — Bases da Programação

#### Programa 2.2 (`ola.py`) — mensagem de erro de codificação

**Imprecisão:** o livro mostra o comando `python3 ola.py` seguido da mensagem `SyntaxError: Non-ASCII character '\xc3' in file ola.py ... but no encoding declared`. Essa mensagem é característica do **Python 2**, e não do Python 3.

**Correção:** para reproduzir o erro mostrado no livro, use o Python 2:

```bash
$ python2 ola.py
```

No Python 3 (usado em todo o livro e neste site) a codificação padrão dos arquivos é UTF-8 e o programa roda normalmente, sem a declaração de codificação.

### Capítulo 3 — Programação Estruturada

#### Exercício 3.10

**Imprecisão no enunciado:** Enunciado do exercício ficou incompleto e misturou categorias.

**Correção:**  Novo enunciado:

Este programa irá exigir um pouco mais de testes. É comum que donos de
cachorros calculem a “idade humana” equivalente de seus cães usando uma
simples multiplicação por 7, mas a conta é um pouco mais complexa que isso. O
envelhecimento de um cão depende de sua raça e porte. Podemos fazer alguma simplificações para obter uma idade "humana" aproximada.
Considere a seguinte classificação por peso:
1. Pequeno: até 10 kg (inclusive)
2. Médio: acima de 10 kg até 23 kg (inclusive)
3. Grande: acima de 23 kg

O cálculo da idade humana deve seguir estas regras:

1. Para os dois primeiros anos de vida do cão:
   - Pequeno: cada ano equivale a 12,5 anos humanos
   - Médio: cada ano equivale a 10,5 anos humanos
   - Grande: cada ano equivale a 9 anos humanos
2. Para os anos adicionais (idade acima de 2 anos):
   - Pequeno: cada ano adicional equivale a 5,2 anos humanos
   - Médio: cada ano adicional equivale a 5,7 anos humanos
   - Grande: cada ano adicional equivale a 7,8 anos humanos

A idade humana equivalente deve ser calculada somando:
a contribuição dos dois primeiros anos (ou da idade total, se o cão tiver menos de 2 anos), e
a contribuição dos anos adicionais, se houver.

Tarefa:
Escreva um programa que solicite o peso (em kg) e a idade (em anos) de um cão e calcule sua idade humana equivalente de acordo com as regras acima.

Considere que os valores informados são positivos.

### Capítulo 4 - Subalgoritmos
#### Programa 4.1
Erro no fechamento de parêntesis:
```
5 print ('O fatorial de', n, 'é', fat
```

O correto é:

```python
5 print ('O fatorial de', n, 'é', fat)
```



5 print ('O fatorial de', n, 'é', fat

#### Exercício 4.2
- **Erro na faixa:** números devem começar em 10, não em 0.
  
Escreva um programa que imprima uma tabela das raízes quadradas dos números
entre 10 e 100, com incrementos de 10.

### Capítulo 5 - Organizando a Informação
#### Programa 5.31 
Erro no for: 
```
for i in range(n):
```

o correto é: 
```python
for i in range(lin):
```
