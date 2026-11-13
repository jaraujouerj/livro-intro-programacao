---
title: "Capítulo 6 — Strings e Arquivos"
weight: 6
bookCollapseSection: true
---
# 📘 Exercícios — Capítulo 6
# Strings e Arquivos

[← Voltar](../)

---
## 6.1 Strings
### Exercício 6.1 — Romani ite domum
Escreva uma função que escreva na tela 100 vezes a frase 'Romani ite domum'.

{{< solucao nivel="iniciante" >}}
### Exercício — Romani ite domum
{{< codefile "assets/code/ex6.1_romani.py" >}}

{{< /solucao >}}

---
### Exercício 6.2 — Listas e strings
Volte aos capítulos sobre listas e teste quais comandos de listas funcionam em
strings. Substitua nos programas do capítulo as listas por strings, quando couber, e
veja se ocorrem erros de execução.

{{< solucao nivel="intermediario" >}}
### Exercício — Listas e strings

Uma string é uma **sequência**, como uma lista, mas é **imutável**: seus caracteres não podem ser alterados depois de criada. Quase tudo o que *lê* uma lista funciona em strings. Quase tudo o que *modifica* uma lista dá erro. O programa abaixo testa os comandos e os programas do capítulo 5, e mostra o resultado ou o erro de cada um:

{{< codefile "assets/code/ex6.2_listas_em_strings.py" >}}

#### Parte 1: comandos de listas em uma string (`s = "celacanto"`)

**Funcionam**, pois só leem a sequência:

| Comando | Resultado |
|---|---|
| `s[0]`, `s[-1]` | `'c'`, `'o'` |
| `len(s)` | `9` |
| `for c in s` | percorre os caracteres |
| `enumerate(s)` | pares `(0, 'c')`, `(1, 'e')`, ... |
| `s[2:5]`, `s[::2]`, `s[::-1]` | `'lac'`, `'clcno'`, `'otnacalec'` (fatiamento igual ao das listas, inclusive o passo negativo) |
| `s + "xx"`, `s * 2` | cria uma **nova** string (concatenação e repetição) |
| `s == "celacanto"` | `True` (comparação) |
| `min(s)`, `max(s)` | `'a'`, `'t'` (ordem alfabética dos caracteres) |
| `list(s)` | converte a string em lista de caracteres |

**Funcionam, mas de forma diferente** do que se espera de uma lista:

| Comando | O que acontece |
|---|---|
| `"can" in s` | procura uma **subcadeia** e não um elemento: `True` |
| `s.count("ca")`, `s.index("can")` | também aceitam subcadeias: `1` e `4` |
| `sorted(s)` | devolve uma **lista** de caracteres, não uma string. Para voltar a string: `"".join(sorted(s))` |
| `[x for x in s if ...]` | a compreensão também devolve uma lista |

**Dão erro de execução:**

| Comando | Erro |
|---|---|
| `s[0] = "x"`, `s[1:3] = "xx"` | `TypeError: 'str' object does not support item assignment` |
| `del s[0]` | `TypeError: 'str' object doesn't support item deletion` |
| `s.append(...)`, `s.extend(...)`, `s.insert(...)`, `s.remove(...)`, `s.pop()`, `s.sort()`, `s.reverse()`, `s.copy()` | `AttributeError: 'str' object has no attribute '...'` |
| `3 in s` | `TypeError: 'in <string>' requires string as left operand, not int` |
| `s + ["a"]` | `TypeError: can only concatenate str (not "list") to str` |
| `sum(s)` | `TypeError`: `sum` soma números, e os elementos são strings |
| `s[20]` | `IndexError: string index out of range` (igual às listas) |
| `s.index("z")` | `ValueError: substring not found` (também ocorre com listas) |

A regra é simples: **tudo que modifica a sequência no lugar não existe em strings**. Para "modificar" uma string, constrói-se uma nova: `s = s[:2] + "x" + s[3:]`, ou `s = s.replace(...)`, ou converte-se para lista, altera-se e volta-se com `"".join(lista)`.

#### Parte 2: programas do capítulo 5 com strings no lugar de listas

Os elementos de uma string são **strings de um caractere**. Por isso `'7'` não é o número 7, e é preciso `int()` para fazer contas.

| Programa | Substituição | Resultado |
|---|---|---|
| 5.1 (soma de notas) | `notas = '7894'` | **Erro.** `notas[0] + notas[1]` concatena (`'78'`...), e `soma / 4` dá `TypeError` |
| 5.2 e 5.4 (soma com `range`) | `notas = '7894'` | **Erro:** `TypeError` ao somar `0` com `'7'` |
| 5.5 (soma com `for`) | `notas = '7894'` | **Erro:** `TypeError` ao somar `int` com `str`. Com `soma += int(nota)` funciona |
| 5.6 (lista mutável) | `notas[3] = '6'` | **Erro:** `item assignment` |
| 5.8 (dobra com `for`) | `lista = '12357'` | **Sem erro, mas resultado diferente:** imprime `11 22 33 55 77`, porque `'1' * 2` é `'11'` |
| 5.9, 5.10, 5.11 | `lista[i] *= 2` | **Erro:** `item assignment` |
| 5.15 (compreensão) | `[x * x for x in '12357']` | **Erro:** `TypeError`, não se multiplica string por string. Com `int(x) ** 2` funciona |
| 5.17 (bom dia) | `nomes = 'José João Joaquim'` | **Sem erro, mas errado:** percorre *letras*, gerando `'Bom dia, J'`, `'Bom dia, o'`... Com `nomes.split()` funciona |
| 5.18 (`lista *= 3`) | `lista = '123'` | Funciona: `'123123123'` |
| 5.19 (diferença) | `a = '2345547'` e `b = '745'` | Funciona, mas devolve uma **lista** de caracteres: `['2', '3']` |
| 5.20 e 5.22 (fatiamento) | `planetas = 'MVTMSJUN'` | Funciona, igual às listas |
| 5.21 (insere por fatia) | `primos[2:2] = '57'` | **Erro:** `item assignment`. Com `primos[:2] + '57' + primos[2:]` funciona |
| 5.23 (`i in primos`) | `primos = '235711131719'` | **Erro:** `TypeError` ao testar um inteiro. Com `str(i) in primos` roda, mas **dá resposta errada**: o `9` aparece "em primos", porque `'9'` é subcadeia de `'19'` |
| 5.24 (`del`) | `del primos[1:3]` | **Erro:** `item deletion` |
| 5.25 (comandos) | `count`, `index`, `min`, `max` | Funcionam |
| 5.25 e 5.26 | `append`, `sort`, `reverse`... | **Erro:** `AttributeError`. No 5.26, `numeros += str(n)` funciona |
| 5.27 | `lista2[1] = '4'` | **Erro:** `item assignment` |
| 5.28 (alias) | `lista2 = lista1` | **Sem o efeito do alias:** `lista2 += 'x'` cria outra string, e `lista1` não muda. Imutabilidade elimina o problema |
| 5.29 (`lista1[:]`) | `lista2 = lista1[:]` | Funciona, mas **não copia**: `lista2 is lista1` é `True`, pois não há motivo para copiar um objeto imutável |
| 5.30 (passagem) | `param += 'x'` | Com lista, a função **altera** a lista original (`['a', 'b', 'c', 'x']`). Com string, o original continua `'abc'` |
| 5.31 (matriz) | `['0' * 4] * 3` | Cria a "matriz", mas `matriz[0][2] = '3'` dá **erro**. A armadilha das linhas repetidas (5.31) some, mas a atribuição também |
| 5.a (`enumerate`) | `'DSTQQSS'` | Funciona |

Os programas 5.12, 5.13 e 5.16 só usam `range`, e os dicionários, tuplas e o NumPy (5.32 em diante) não são listas, então não foram testados.

#### Conclusões

1. **Leitura** (índices, fatias, `len`, `for`, `enumerate`, `in`, `+`, `*`) funciona nas duas.
2. **Modificação no lugar** (atribuição por índice ou fatia, `del`, `append`, `sort`...) só funciona em listas. Em strings gera `TypeError` ou `AttributeError`.
3. **Erros silenciosos** são os mais perigosos: `'1' * 2` vira `'11'`, `for` sobre `'José João'` percorre letras, `'9' in '19'` é verdadeiro. O programa roda e a resposta é errada.
4. Strings guardam **caracteres**, não números: para calcular, converta com `int()` ou `float()`.
5. Strings são **imutáveis**: por isso não há problema de alias nem de passagem de parâmetro, mas também não há como alterá-las. É preciso criar uma nova.

{{< /solucao >}}

---
### Exercício 6.3 — Contando espaços
Escreva um programa em Python que conte a quantidade de espaços em branco
de uma string.

{{< solucao nivel="iniciante" >}}
### Exercício — Contando espaços
{{< codefile "assets/code/ex6.3_conta_espacos.py" >}}

{{< /solucao >}}

---
## 6.2 Fatiando Strings
### Exercício 6.4 — String invertida
Escreva uma função que receba uma string como parâmetro e escreva-a invertida,
usando apenas o fatiamento. Ex.: 'celacanto provoca maremoto' imprime
'otomeram acovorp otnacalec'. Dica: o passo pode ser negativo.

{{< solucao nivel="iniciante" >}}
### Exercício — String invertida
{{< codefile "assets/code/ex6.4_string_invertida.py" >}}

{{< /solucao >}}

---
### Exercício 6.5 — Palíndromo com fatiamento
Tente outras formas de testar se uma palavra é um palíndromo. Tente outro
fatiamento.

{{< solucao nivel="iniciante" >}}
### Exercício — Palíndromo com fatiamento
{{< codefile "assets/code/ex6.5_palindromo_fatiamento.py" >}}

{{< /solucao >}}

---
### Exercício 6.6 — Palíndromo com lower()
O teste de palíndromo desta seção tem um grande problema: ele não diferencia
maiúsculas de minúsculas. Desse modo, 'Ovo' não seria identificado como
palíndromo. Como se pode consertar isso? Pesquise a função de Python
`lower()` que transforma maiúsculas em minúsculas.

{{< solucao nivel="iniciante" >}}
### Exercício — Palíndromo com lower()
{{< codefile "assets/code/ex6.6_palindromo_lower.py" >}}

{{< /solucao >}}

---
## 6.3 Operações sobre Strings
### Exercício 6.7 — Palíndromo em frases
Escreva uma função que receba uma string como parâmetro e diga se se trata de
um palíndromo ou não. Na string devem ser ignorados os espaços em branco e as
letras maiúsculas e minúsculas não são diferenciadas. Por exemplo, a frase 'Seco
de raiva coloco no colo caviar e doces' deve ser considerada um palíndromo.

{{< solucao nivel="iniciante" >}}
### Exercício — Palíndromo em frases
{{< codefile "assets/code/ex6.7_palindromo_frase.py" >}}

{{< /solucao >}}

---
### Exercício 6.8 — Nome composto
O Programa 6.10 só funciona bem com um nome composto de três partes.
Modifique o programa para que seja possível trabalhar com um número maior de
partes.

O Programa 6.10 original:
```python
nome = 'João Araujo Ribeiro'
lista = nome.split(' ')
print(lista)
lista[1] = lista[1][0] + '.'
print(lista)
lista[0], lista[1], lista[2] = lista[2], lista[0], lista[1]
lista[0] += ','
print(lista)
nome = ' '.join(lista)
print(nome)
```

{{< solucao nivel="iniciante" >}}
### Exercício — Nome composto
{{< codefile "assets/code/ex6.8_nome_composto.py" >}}

{{< /solucao >}}

---
### Exercício 6.9 — Nome com duas partes
Prepare seu programa do exercício anterior para aceitar também nomes
compostos de apenas duas partes.

{{< solucao nivel="iniciante" >}}
### Exercício — Nome com duas partes
{{< codefile "assets/code/ex6.9_nome_duas_partes.py" >}}

{{< /solucao >}}

---
## 6.4 Arquivos
### Exercício 6.10 — Arquivo em maiúsculas
Escreva um programa que converta todas as letras de um arquivo em maiúsculas e
escreva o resultado na tela.

{{< solucao nivel="iniciante" >}}
### Exercício — Arquivo em maiúsculas
{{< codefile "assets/code/ex6.10_arquivo_maiusculas.py" >}}

{{< /solucao >}}

---
### Exercício 6.11 — Arquivo em minúsculas
Escreva um programa que converta todas as letras de um arquivo em minúsculas e
escreva o resultado na tela.

{{< solucao nivel="iniciante" >}}
### Exercício — Arquivo em minúsculas
{{< codefile "assets/code/ex6.11_arquivo_minusculas.py" >}}

{{< /solucao >}}

---
### Exercício 6.12 — Primeira letra maiúscula
Escreva um programa que converta a primeira letra de cada palavra de um arquivo
em maiúscula e escreva o resultado na tela.

{{< solucao nivel="iniciante" >}}
### Exercício — Primeira letra maiúscula
{{< codefile "assets/code/ex6.12_arquivo_titulo.py" >}}

{{< /solucao >}}

---
## 6.5 Escrevendo em Arquivos
### Exercício 6.13 — Tabela Celsius-Fahrenheit em arquivo
Escreva um programa que salve uma tabela em um arquivo com a conversão de temperaturas
Celsius para Fahrenheit de 0 a 300.

{{< solucao nivel="iniciante" >}}
### Exercício — Tabela Celsius-Fahrenheit
{{< codefile "assets/code/ex6.13_tabela_celsius_fahrenheit.py" >}}

{{< /solucao >}}

---
### Exercício 6.14 — Cópia de arquivo
Escreva um programa que copie o conteúdo de um arquivo para um novo arquivo.
Seu programa deve testar se o arquivo de destino já existe e, se afirmativo, deve
perguntar ao usuário se ele quer sobrescrevê-lo.

{{< solucao nivel="iniciante" >}}
### Exercício — Cópia de arquivo
{{< codefile "assets/code/ex6.14_copia_arquivo.py" >}}

{{< /solucao >}}

---
### Exercício 6.15 — Pontos de pi em arquivo
Escreva um programa que guarde os pontos gerados pelo Programa 4.16 em um
arquivo, um ponto por linha. Ao final, escreva nesse arquivo o resultado do cálculo
para pi.

{{< solucao nivel="iniciante" >}}
### Exercício — Pontos de pi em arquivo
{{< codefile "assets/code/ex6.15_pi_arquivo.py" >}}

{{< /solucao >}}

---

## Quer ir além?

Se você quiser se desafiar com novos problemas, sem solução disponível:

👉 [Exercícios extras do Capítulo 6](../../extras/cap6/)