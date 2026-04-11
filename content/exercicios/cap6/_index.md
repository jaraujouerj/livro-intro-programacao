+++
title = 'Cap6'
date = 2026-04-11T10:00:00-03:00
draft = true
+++
# 📘 Exercícios — Capítulo 6
# Strings e Arquivos

---
## 6.2 Strings
### Exercício 6.1 — Romani ite domum
Escreva uma função que escreva na tela 100 vezes a frase 'Romani ite domum'.

{{< solucao nivel="iniciante" >}}
### Exercício — Romani ite domum
{{< codefile "assets/code/ex6.1_romani.py" >}}

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
## 6.3 Arquivos
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
