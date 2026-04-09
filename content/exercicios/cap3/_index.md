+++
title = 'Cap3'
date = 2026-04-08T19:17:35-03:00
draft = true
+++

# 📘 Exercícios — Capítulo 3

# Programação Estruturada
## 3.2 Tomando uma Decisão
### Exercício 3.1
Modifique o programa do exercício 2.9 de forma que este peça o valor do lado do
quadrado antes de calcular a área. (Use o conversor int)



{{< solucao nivel="iniciante" >}}
### Exercício — Área de um quadrado em Python

**Ideia:**  
A área de um quadrado é dada pelo lado multiplicado por ele mesmo.

**Programa:**
{{< codefile "assets/code/ex3.1_area_quadrado_int.py" >}}

{{< /solucao >}}

---
### Exercício 3.2
Faça o mesmo programa do exercício anterior usando o conversor float.

{{< solucao nivel="iniciante" >}}
### Exercício — Área de um quadrado em Python

{{< codefile "assets/code/ex3.2_area_quadrado_float.py" >}}

{{< /solucao >}}

---
### Exercício 3.3
Modifique as indentações dos programas desta seção e veja qual erro o
interpretador Python indica.

{{< solucao nivel="iniciante" >}}
Por exemplo, ao escrever

```python
# lê o valor do lado
lado = float(input("Digite o valor do lado do quadrado: "))
# calcula a área
   area = lado * lado  # perceba o deslocamnento

# imprime o resultado
print("Área do quadrado:", area)
```

O interpretador dá o erro:
<pre>
area = lado * lado  # perceba o deslocamnento

IndentationError: unexpected indent

ou em português: Erro de indentação. indentação incorreta.
</pre>
{{< /solucao >}}

---
### Exercício 3.4
Escreva um programa que diga se um número inteiro digitado é par ou ímpar.

{{< solucao nivel="iniciante" >}}
### Exercício — Par ou ímpar

{{< codefile "assets/code/ex3.4_par_ou_impar.py" >}}

{{< /solucao >}}

---
### Exercício 3.5
Escreva um programa que receba dois números inteiros pelo teclado e informe se
o segundo é um múltiplo do primeiro.

{{< solucao nivel="iniciante" >}}
### Exercício — Múltiplo

{{< codefile "assets/code/ex3.5_multiplo.py" >}}

{{< /solucao >}}

---
## 3.3 Testes em Sequência
### Exercício 3.6
Escreva um programa em Python que teste se um número é divisível por 3, 5 ou 7.
Seu programa deve dizer por qual desses valores o número é divisível.

{{< solucao nivel="iniciante" >}}
### Exercício — Divisível por 3, 5 ou 7 
{{< codefile "assets/code/ex3.6_divisivel_357.py" >}}
{{< /solucao >}}

---
## 3.4 Condições Compostas
### Exercício 3.7
Uma empresa vai conceder um aumento diferenciado a seus funcionários,
segundo os seguintes critérios: quem ganha até 1000 reais (inclusive) terá
aumento de 20 %; entre 1000 e 2000 (inclusive), aumento de 18 %; entre 2000 e
4000 (inclusive) aumento de 15 % e acima de 4000 aumento de 10 %. Escreva um
programa que, dado um valor de salário, calcule o novo valor após o aumento.

{{< solucao nivel="iniciante" >}}
### Exercício — Aumento de salário
{{< codefile "assets/code/ex3.7_aumento_salario.py" >}}

Claro que uma solução melhor seria:

{{< codefile "assets/code/ex3.7_aumento_salario_v2.py" >}}

{{< /solucao >}}

---
### Exercício 3.8
Sabendo que um triângulo é dito equilátero quando tem 3 lados iguais, isósceles
quando tem 2 lados iguais e escaleno quando todos os lados têm tamanhos
diferentes, escreva um programa que receba os valores dos três lados de um
triângulo e imprima se ele é equilátero, isósceles ou escaleno.

{{< solucao nivel="iniciante" >}}
### Exercício — Triângulo
{{< codefile "assets/code/ex3.8_triangulo.py" >}}

{{< /solucao >}}

---
### Exercício 3.9
Considere que um ser humano pode ser classificado segundo sua idade nas
seguintes faixas etárias:
•Bebê (nascimento até 3 anos).
•Criança (4 até 7 anos).
•Pré-adolescente (8 até 12 anos).
•Adolescente (13 até 20 anos).
•Jovem (21 a 40 anos).
• Meia-idade (41 até 64 anos).
• Idoso (65 anos em diante).

Escreva um programa que solicite uma idade e imprima a classificação
correspondente.

{{< solucao nivel="iniciante" >}}
### Exercício — Classificação de idade
```python
# lê a idade
idade = int(input("Digite a idade: "))

# classifica a idade
if idade <= 3:
    print("Bebê")
elif idade <= 7:
    print("Criança")
elif idade <= 12:
    print("Pré-adolescente")
elif idade <= 20:
    print("Adolescente")
elif idade <= 40:
    print("Jovem")
elif idade <= 64:
    print("Meia-idade")
else:
    print("Idoso")
{{< /solucao >}}

---
### Exercício 3.10
⚠️ Enunciado atualizado!

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


{{< solucao nivel="iniciante" >}}
### Exercício — Idade humana de cães
{{< codefile "assets/code/ex3.10_idade_humana_caes.py" >}}

{{< /solucao >}}

---
## 3.5 Estruturas de Repetição
### Exercício 3.11
Escreva um programa que receba um número inteiro n e calcule a soma dos
quadrados dos números até n-1. Exemplo: se n for igual a 3, seu programa deve
dar o resultado da soma dos números 1<sup>2</sup> + 2<sup>2</sup>.

{{< solucao nivel="iniciante" >}}
### Exercício — Soma dos quadrados
{{< codefile "assets/code/ex3.11_soma_quadrados.py" >}}
{{< /solucao >}}

---
### Exercício 3.12
Escreva um programa que calcule a média dos números digitados pelo usuário. O
programa deve calcular a média quando o usuário digitar o número zero.

{{< solucao nivel="iniciante" >}}
### Exercício — Média dos números
{{< codefile "assets/code/ex3.12_media_numeros.py" >}}

{{< /solucao >}}

---
## 3.6 Laços Contados
### Exercício 3.13
Reescreva o Exercício 3.11 usando o comando for.

{{< solucao nivel="iniciante" >}}
### Exercício — Soma dos quadrados (for)
{{< codefile "assets/code/ex3.13_soma_quadrados_for.py" >}}
{{< /solucao >}}

---
### Exercício 3.14
Escreva um programa que calcule a temperatura equivalente em Fahrenheit para
os graus Celsius entre 0 e 100 com intervalos de 10 graus.

{{< solucao nivel="iniciante" >}}
### Exercício — Temperatura em Fahrenheit
{{< codefile "assets/code/ex3.14_temp_fahrenheit.py" >}}

{{< /solucao >}}

---
### Exercício 3.15
Escreva um programa que gere o seguinte padrão usando laços encaixados:
<pre>
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
</pre>

{{< solucao nivel="iniciante" >}}
### Exercício — Padrão de asteriscos
{{< codefile "assets/code/ex3.15_padrao_asteriscos.py" >}}

{{< /solucao >}}

---

