---
title: "Capítulo 7 — Recursão"
weight: 7
bookCollapseSection: true
---
# 📘 Exercícios — Capítulo 7
# Recursão

[← Voltar](../)

---
## 7.2 Cálculo Recursivo para Tamanho de Lista
### Exercício 7.1 — String na ordem inversa
Escreva uma função recursiva que imprima uma string na ordem inversa.
Ex.: "celacanto provoca maremoto" será impressa como "otomeram acovorp otnacalec".

{{< solucao nivel="iniciante" >}}
### Exercício — String na ordem inversa
{{< codefile "assets/code/ex7.1_string_inversa_recursiva.py" >}}

{{< /solucao >}}

---
### Exercício 7.2 — Palíndromo recursivo
Escreva uma função recursiva que diga se uma palavra é um palíndromo.
Ex.: arara, ovo, radar, osso.

{{< solucao nivel="iniciante" >}}
### Exercício — Palíndromo recursivo
{{< codefile "assets/code/ex7.2_palindromo_recursivo.py" >}}

{{< /solucao >}}

---
### Exercício 7.3 — Palíndromo em frases (recursivo)
Escreva uma função recursiva que diga se uma frase é um palíndromo. Não
esqueça de ignorar ou apagar os espaços antes de comparar as letras. Ex.: "A mala
nada na lama", "a base do teto desaba".

{{< solucao nivel="iniciante" >}}
### Exercício — Palíndromo em frases (recursivo)
{{< codefile "assets/code/ex7.3_palindromo_frase_recursivo.py" >}}

{{< /solucao >}}

---
## 7.4 Coelhos de Fibonacci
### Exercício 7.4 — Fatorial recursivo
Escreva uma função que calcule o fatorial de um número. O fatorial pode ser
definido como:

fat(n) = 1, se n é 0 ou n × fat(n−1), se n é maior que 0

{{< solucao nivel="iniciante" >}}
### Exercício — Fatorial recursivo
{{< codefile "assets/code/ex7.4_fatorial_recursivo.py" >}}

{{< /solucao >}}

---
## 7.5 Eficiência da Recursão
### Exercício 7.5 — Fibonacci com lista
Reescreva o Programa 7.6 mas usando uma lista no lugar de um dicionário para
armazenar valores intermediários.

Programa 7.6 original:
```python
fibonacci = {0:0, 1:1}
def fib(n):
    """Calcula n-ésimo termo da série de Fibonacci."""
    if n not in fibonacci:
        fibonacci[n] = fib(n-2) + fib(n-1)
    return fibonacci[n]
for i in range(100):
    print('fib' + str(i) + '):'+ str(fib(i)))
```

{{< solucao nivel="iniciante" >}}
### Exercício — Fibonacci com lista
{{< codefile "assets/code/ex7.5_fibonacci_lista.py" >}}

{{< /solucao >}}

---
### Exercício 7.6 — Soma recursiva
Escreva uma função recursiva que some os n primeiros números.

{{< solucao nivel="iniciante" >}}
### Exercício — Soma recursiva
{{< codefile "assets/code/ex7.6_soma_recursiva.py" >}}

{{< /solucao >}}

---

## Quer ir além?

Se você quiser se desafiar com novos problemas, sem solução disponível:

👉 [Exercícios extras do Capítulo 7](../../extras/cap7/)