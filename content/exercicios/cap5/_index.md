+++
title = 'Cap5'
date = 2026-04-10T17:59:43-03:00
draft = true
+++
# 📘 Exercícios — Capítulo 5
# Organizando a Informação

## 5.3 Processando uma Lista
### Exercício 5.1
Escreva um programa que receba uma lista de temperaturas em Celsius e escreva
na tela o resultado da conversão dessas temperaturas em Fahrenheit. (Não se
esqueça de usar a fórmula correta!)

{{< solucao nivel="iniciante" >}}
### Exercício — Temperatura em Fahrenheit
{{< codefile "assets/code/ex5.1_fahrenheit.py" >}}

{{< /solucao >}}


---
### Exercício 5.2 — Fahrenheit invertido
Reescreva o programa 5.13 de modo a imprimir o resultado a partir do último
elemento (de 300 para 0).

Programa 5.13 original:
```python
print('Tabela de conversão de Fahrenheit para Celsius')
for fahr in range(0, 301, 20):
    celsius = (5/9) * (fahr - 32)
    print('{:>5d} -> {:>5.1f}'.format(fahr, celsius))
```

{{< solucao nivel="iniciante" >}}
### Exercício — Fahrenheit invertido
{{< codefile "assets/code/ex5.2_fahrenheit_invertido.py" >}}

{{< /solucao >}}

---
### Exercício 5.3 — Fahrenheit com try...except
Reescreva o programa 5.14 validando a entrada de dados do usuário, usando a
estrutura try...except.

{{< solucao nivel="iniciante" >}}
### Exercício — Fahrenheit com try...except
{{< codefile "assets/code/ex5.3_fahrenheit_try_except.py" >}}

{{< /solucao >}}

---
### Exercício 5.4 — Fahrenheit com while
Reescreva o Programa 5.13 usando o comando while.

{{< solucao nivel="iniciante" >}}
### Exercício — Fahrenheit com while
{{< codefile "assets/code/ex5.4_fahrenheit_while.py" >}}

{{< /solucao >}}

---
### Exercício 5.5 — Ímpares para pares
Crie uma lista com os números ímpares entre 0 e 100 (use `range()`) e depois
use o comando `enumerate()` para percorrer a lista transformando o valor de cada
elemento no valor par subsequente.

{{< solucao nivel="iniciante" >}}
### Exercício — Ímpares para pares
{{< codefile "assets/code/ex5.5_impares_para_pares.py" >}}

{{< /solucao >}}

---
### Exercício 5.6 — Tabela de pi
Modifique o Programa 4.23 que calcula pi para que este não mais solicite o
número de pontos a serem gerados, mas gere uma tabela com ao menos 10
valores de pi calculados com números diferentes de pontos. Use `range()` para
gerar os diversos valores de entrada da função.

{{< solucao nivel="iniciante" >}}
### Exercício — Tabela de pi
{{< codefile "assets/code/ex5.6_tabela_pi.py" >}}

{{< /solucao >}}

---
## 5.4 Listas Por Compreensão
### Exercício 5.7 — Quadrado dos pares
Escreva um programa para gerar uma lista com o quadrado dos números pares
entre 10 e 20 (inclusive).

{{< solucao nivel="iniciante" >}}
### Exercício — Quadrado dos pares
{{< codefile "assets/code/ex5.7_quadrado_pares.py" >}}

{{< /solucao >}}

---
### Exercício 5.8 — Quadrado dos ímpares com range
Escreva um programa para gerar uma lista com o quadrado dos números ímpares
de 0 a 9, porém não use filtros. Use apenas o comando `range()` para controlar a
geração da sequência de números ímpares.

{{< solucao nivel="iniciante" >}}
### Exercício — Quadrado dos ímpares com range
{{< codefile "assets/code/ex5.8_quadrado_impares_range.py" >}}

{{< /solucao >}}

---
### Exercício 5.9 — Cubos
Escreva um programa que crie uma lista com o cubo dos números entre 1 e 10,
ambos inclusive.

{{< solucao nivel="iniciante" >}}
### Exercício — Cubos
{{< codefile "assets/code/ex5.9_cubos.py" >}}

{{< /solucao >}}

---
### Exercício 5.10 — Múltiplos de 7
Escreva um programa que crie uma lista com os 10 primeiros múltiplos de 7.

{{< solucao nivel="iniciante" >}}
### Exercício — Múltiplos de 7
{{< codefile "assets/code/ex5.10_multiplos_7.py" >}}

{{< /solucao >}}

---
## 5.5 Somando e Multiplicando Listas
### Exercício 5.11 — Rotação de lista
Escreva um programa que dada a lista `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` gere a lista
`[5, 6, 7, 8, 9, 0, 1, 2, 3, 4]`.

{{< solucao nivel="iniciante" >}}
### Exercício — Rotação de lista
{{< codefile "assets/code/ex5.11_rotacao_lista.py" >}}

{{< /solucao >}}

---
### Exercício 5.12 — Ímpares e pares separados
Escreva um programa que dada a lista `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` gere a lista
`[1, 3, 5, 7, 9, 0, 2, 4, 6, 8]`.

{{< solucao nivel="iniciante" >}}
### Exercício — Ímpares e pares separados
{{< codefile "assets/code/ex5.12_impares_pares.py" >}}

{{< /solucao >}}

---
## 5.6 Extraindo Sublistas
### Exercício 5.13 — Fatiamento
Dada a lista `[10, 2, 32, 14, 35, 46, 17, 58, 199, 19]`, escreva um programa que
imprima:

1. os elementos de índices pares;
2. os elementos de índices ímpares;
3. os elementos entre os índices 2 (inclusive) e 4 (exclusive);
4. o elemento de índice 1 e depois os elementos distantes 3 posições a partir de 1, até o final.

{{< solucao nivel="iniciante" >}}
### Exercício — Fatiamento
{{< codefile "assets/code/ex5.13_fatiamento.py" >}}

{{< /solucao >}}

---
### Exercício 5.14 — Fatiamento negativo
Gere uma lista com 100 números de 0 a 99, com o comando `range()` e, usando
valores negativos no fatiamento, escreva um programa que imprima:

1. o último elemento da lista original e depois, decrescendo, os elementos
distantes 3 posições a partir do final até o início;
2. os elementos entre o índice 87 (inclusive) e o índice 34 (exclusive), em ordem
decrescente de índices;
3. todos os elementos, exceto os dois últimos.

{{< solucao nivel="iniciante" >}}
### Exercício — Fatiamento negativo
{{< codefile "assets/code/ex5.14_fatiamento_negativo.py" >}}

{{< /solucao >}}

---
### Exercício 5.15 — Inverso com fatiamento
Dada a lista `[1, 2, 3, 4, 5, 6, 7]`, imprima seu inverso, ou seja, `[7, 6, 5, 4, 3, 2, 1]`
usando apenas fatiamento.

{{< solucao nivel="iniciante" >}}
### Exercício — Inverso com fatiamento
{{< codefile "assets/code/ex5.15_inverso_fatiamento.py" >}}

{{< /solucao >}}

---
### Exercício 5.16 — Planetas
Considere a lista:

`planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Saturno', 'Júpiter', 'Urano', 'Netuno']`

Execute as seguintes operações usando apenas fatiamento. Cada item usa a lista
resultante do item anterior.

1. Insira a lista `['Fobos','Deimos']` na posição 4 da lista.
2. Insira `['Sol']` na posição zero.
3. Qual seria o fatiamento para imprimir `['Urano', 'Júpiter', 'Saturno', 'Deimos', 'Fobos', 'Marte', 'Terra', 'Vênus']`, nessa ordem?

{{< solucao nivel="iniciante" >}}
### Exercício — Planetas
{{< codefile "assets/code/ex5.16_planetas.py" >}}

{{< /solucao >}}

---
## 5.17 Operações em Listas
### Exercício 5.17 — append() com lista
O que acontece se você chama o comando `append()` com outra lista? Considere
a lista `primos = [2, 3, 5, 7]` e que você use o comando
`primos.append([23,29,31])`.
Tente imprimir o elemento `primos[4]`. O que é impresso?

{{< solucao nivel="iniciante" >}}
### Exercício — append() com lista
{{< codefile "assets/code/ex5.17_append_lista.py" >}}

{{< /solucao >}}

---
### Exercício 5.18 — extend() com lista
Execute as mesmas operações do exercício 5.17, mas usando o comando
`extend()` no lugar de `append()` com uma lista. O que acontece? Houve
alguma diferença? Tente imprimir o elemento `primos[4]`. O que é impresso?

{{< solucao nivel="iniciante" >}}
### Exercício — extend() com lista
{{< codefile "assets/code/ex5.18_extend_lista.py" >}}

{{< /solucao >}}

---
### Exercício 5.19 — Fatiamento com passo -1
O que acontece se o terceiro parâmetro de uma operação de fatiamento for -1?
Teste em uma lista qualquer o comando `lista[::-1]`. Qual a diferença para
`reverse()`?

{{< solucao nivel="iniciante" >}}
### Exercício — Fatiamento com passo -1
{{< codefile "assets/code/ex5.19_fatiamento_reverse.py" >}}

{{< /solucao >}}

---
### Exercício 5.20 — Inverter com lista por compreensão
Escreva um programa que inverta uma lista usando o método de lista por
compreensão.

{{< solucao nivel="iniciante" >}}
### Exercício — Inverter com lista por compreensão
{{< codefile "assets/code/ex5.20_inverter_compreensao.py" >}}

{{< /solucao >}}

---
### Exercício 5.21 — Primeira metade
Use os comandos desta seção para criar uma nova lista com os elementos da
primeira metade de uma lista. Por exemplo, se temos
`lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, use os comandos para obter `[0, 1, 2, 3, 4]`.

{{< solucao nivel="iniciante" >}}
### Exercício — Primeira metade
{{< codefile "assets/code/ex5.21_primeira_metade.py" >}}

{{< /solucao >}}

---
### Exercício 5.22 — Apagar primeira metade
Use os comandos desta seção para apagar os elementos da primeira metade de
uma lista. Por exemplo, se temos `lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, use os
comandos para obter `lista = [5, 6, 7, 8, 9]`.

{{< solucao nivel="iniciante" >}}
### Exercício — Apagar primeira metade
{{< codefile "assets/code/ex5.22_apagar_primeira_metade.py" >}}

{{< /solucao >}}

---
### Exercício 5.23 — Inverter primeira metade
Use os comandos desta seção para inverter os elementos da primeira metade de
uma lista. Por exemplo, se a lista é `lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, use os
comandos para obter `[4, 3, 2, 1, 0, 5, 6, 7, 8, 9]`.

{{< solucao nivel="iniciante" >}}
### Exercício — Inverter primeira metade
{{< codefile "assets/code/ex5.23_inverter_primeira_metade.py" >}}

{{< /solucao >}}

---
### Exercício 5.24 — Segunda metade e primeira invertida
Partindo da `lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`, use os comandos desta seção para
obter `[5, 6, 7, 8, 9, 4, 3, 2, 1, 0]`.

{{< solucao nivel="iniciante" >}}
### Exercício — Segunda metade e primeira invertida
{{< codefile "assets/code/ex5.24_segunda_metade_invertida.py" >}}

{{< /solucao >}}

---
### Exercício 5.25 — Divisíveis por 7, não por 3
Escreva um programa que crie uma lista com todos os números entre 100 e 1000
que são divisíveis por 7 mas não são múltiplos de 3.

{{< solucao nivel="iniciante" >}}
### Exercício — Divisíveis por 7, não por 3
{{< codefile "assets/code/ex5.25_divisiveis_7_nao_3.py" >}}

{{< /solucao >}}

---
### Exercício 5.26 — Média
Escreva um programa que crie uma lista com números digitados pelo usuário e
forneça como saída a média desses números.

{{< solucao nivel="iniciante" >}}
### Exercício — Média
{{< codefile "assets/code/ex5.26_media.py" >}}

{{< /solucao >}}

---
## 5.11 Listas de Listas
### Exercício 5.27 — Matriz com for
Escreva um programa que crie uma matriz bidimensional usando 2 comandos
`for` encaixados, isto é, não use nem multiplicação nem lista por compreensão
para criar sua matriz.

{{< solucao nivel="iniciante" >}}
### Exercício — Matriz com for
{{< codefile "assets/code/ex5.27_matriz_for.py" >}}

{{< /solucao >}}

---
### Exercício 5.28 — Matriz tridimensional
Escreva um programa que crie uma matriz tridimensional usando o mecanismo de
lista por compreensão.

{{< solucao nivel="iniciante" >}}
### Exercício — Matriz tridimensional
{{< codefile "assets/code/ex5.28_matriz_3d.py" >}}

{{< /solucao >}}

---
## 5.12 Dicionários
### Exercício 5.29 — Estados e siglas
Escreva um programa que crie um dicionário relacionando o nome dos estados
brasileiros (como chaves) às suas siglas. O programa deve solicitar ao usuário o
nome de um estado, e chamar uma função que devolve a sua sigla.

{{< solucao nivel="iniciante" >}}
### Exercício — Estados e siglas
{{< codefile "assets/code/ex5.29_estados_siglas.py" >}}

{{< /solucao >}}

---
### Exercício 5.30 — Estados case-insensitive
Escreva um programa que crie um dicionário relacionando o nome dos estados
brasileiros (como chaves) às suas siglas. O programa deve perguntar ao usuário o
nome de um estado e chamar uma função que devolva a sua sigla. O nome do
estado pode estar em maiúsculas ou minúsculas e mesmo assim o programa deve
dar a resposta correta.

{{< solucao nivel="iniciante" >}}
### Exercício — Estados case-insensitive
{{< codefile "assets/code/ex5.30_estados_case_insensitive.py" >}}

{{< /solucao >}}

---
## 5.13 Tuplas
### Exercício 5.31 — Tupla divisíveis por 7
Escreva um programa que crie uma tupla com todos os números entre 100 e 1000
que são divisíveis por 7 mas não são múltiplos de 3.

{{< solucao nivel="iniciante" >}}
### Exercício — Tupla divisíveis por 7
{{< codefile "assets/code/ex5.31_tupla_divisiveis.py" >}}

{{< /solucao >}}

---
### Exercício 5.32 — Pi com lista de tuplas
Modifique o Programa 4.16 de modo que a função que gera coordenadas
aleatórias receba como parâmetro o número de coordenadas que precisam ser
geradas e devolva uma lista de tuplas com essas coordenadas. Deste modo, a
função que calcula o valor de pi também precisa ser modificada para tratar essas
coordenadas em forma de lista de tuplas.

{{< solucao nivel="iniciante" >}}
### Exercício — Pi com lista de tuplas
{{< codefile "assets/code/ex5.32_pi_tuplas.py" >}}

{{< /solucao >}}

---
### Exercício 5.33 — Aeroportos com tuplas
Os dicionários de Python não são ordenados, pois sua função principal é a busca
rápida de uma informação baseada em uma chave. Modifique o programa sobre
aeroportos desta seção para trabalhar apenas com tuplas, eliminando o dicionário
e usando o nome da cidade como primeiro elemento da tupla.

{{< solucao nivel="iniciante" >}}
### Exercício — Aeroportos com tuplas
{{< codefile "assets/code/ex5.33_aeroportos_tuplas.py" >}}

{{< /solucao >}}

---