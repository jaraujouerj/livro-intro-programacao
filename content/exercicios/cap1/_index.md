---
title: "Capítulo 1 — Introdução aos Computadores"
weight: 1
bookCollapseSection: true

# Metadados (para uso futuro)
nivel: "iniciante"
topicos: ["entrada/saída", "variáveis"]
---

# 📘 Exercícios — Capítulo 1 
# Introdução aos Computadores

---
## 1.1 Sistemas de Numeração
### Exercício 1.1

Se a espécie humana tivesse evoluído para ter 8 dedos, como estaríamos
   escrevendo os seguintes números?

   <ol type="a">
     <li>12</li>
     <li>100</li>
     <li>1234</li>
   </ol>

{{< solucao nivel="iniciante" >}}
A ideia central é que, com 8 dedos, provavelmente teríamos desenvolvido um sistema de numeração de **base 8 (octal)**, em vez do sistema decimal (base 10).

No sistema octal, os algarismos vão de 0 a 7. Assim, cada posição representa potências de 8:
- 8<sup>0</sup> = 1
- 8<sup>1</sup> = 8
- 8<sup>2</sup> = 64

Agora, convertemos os números decimais para base 8:

---

**a) 12 (decimal)**  
12 ÷ 8 = 1 resto 4  
→ 12 = 14<sub>8</sub>

**Resposta:** 14

---

**b) 100 (decimal)**  
100 ÷ 8 = 12 resto 4  
12 ÷ 8 = 1 resto 4  
→ 100 = 144<sub>8</sub>

**Resposta:** 144

---

**c) 1234 (decimal)**  
1234 ÷ 8 = 154 resto 2  
154 ÷ 8 = 19 resto 2  
19 ÷ 8 = 2 resto 3  
2 ÷ 8 = 0 resto 2  
→ 1234 = 2322<sub>8</sub>

**Resposta:** 2322

Potências de 8:

- 8<sup>0</sup> = 1
- 8<sup>1</sup> = 8
- 8<sup>2</sup> = 64
- 8<sup>3</sup> = 512
- 8<sup>4</sup> = 4096


{{< /solucao >}}

---
### Exercício 1.2

E se tivéssemos 12 dedos? Use A e B como símbolos extras para escrever os
números na nova base.

<ol type="a">
    <li>12</li>
    <li>100</li>
    <li>1234</li>
</ol>

{{< solucao nivel="iniciante" >}}
Se a espécie humana tivesse evoluído com 12 dedos, provavelmente usaríamos um sistema de numeração de **base 12 (duodecimal)**.

Nesse sistema, usamos os algarismos de 0 a 9 e mais dois símbolos extras:
- A = 10  
- B = 11  

Cada posição representa potências de 12:
- 12<sup>0</sup> = 1  
- 12<sup>1</sup> = 12  
- 12<sup>2</sup> = 144  

Agora, convertemos os números decimais para base 12:

---

**a) 12 (decimal)**  
12 ÷ 12 = 1 resto 0  
→ 12 = 10<sub>12</sub>  

**Resposta:** 10

---

**b) 100 (decimal)**  
100 ÷ 12 = 8 resto 4  
→ 100 = 84<sub>12</sub>  

**Resposta:** 84

---

**c) 1234 (decimal)**  
1234 ÷ 12 = 102 resto 10 (A)  
102 ÷ 12 = 8 resto 6  
8 ÷ 12 = 0 resto 8  
→ 1234 = 86A<sub>12</sub>  

**Resposta:** 86A

Potências de 12:

- 12<sup>0</sup> = 1  
- 12<sup>1</sup> = 12  
- 12<sup>2</sup> = 144  
- 12<sup>3</sup> = 1728  

{{< /solucao >}}

---
## 1.2 Números Binários
Para facilitar a visualização dos números binários vamos agrupá-los a cada 4 dígitos. Assim, desta forma, o número binário 
10101000<sub>2</sub> será escrito como 1010 1000<sub>2</sub>.

### Exercício 1.3

Quantos números diferentes são possíveis com 10 bits? Quais são o menor e o
maior valor?

{{< solucao nivel="iniciante" >}}
Um número com 10 bits é uma sequência de 10 dígitos binários, onde cada dígito pode ser 0 ou 1.

### Quantidade de números possíveis

Cada bit tem 2 possibilidades. Portanto, o total de combinações é:
2<sup>10</sup> = 1024

**Resposta:** 1024 números diferentes.

---

### Menor valor

O menor número ocorre quando todos os bits são 0:
00 0000 0000<sub>2</sub> = 0

**Resposta:** 0

---

### Maior valor

O maior número ocorre quando todos os bits são 1:
11 1111 1111<sub>2</sub>

Esse valor corresponde a:
2<sup>10</sup> − 1 = 1023

**Resposta:** 1023

{{< /solucao >}}

---
### Exercício 1.4
Converta os seguintes números decimais em binário usando o menor número de
bits possível.

<ol type="a">
    <li>1001</li>
    <li>256</li>
    <li>4095</li>
    <li>545</li>
</ol>

{{< solucao nivel="iniciante" >}}
Para cada número, fazemos a conversão para binário e usamos o **menor número de bits possível** (ou seja, sem zeros à esquerda).

---

Para converter um número decimal em binário, fazemos **divisões sucessivas por 2**, anotando os restos. O número binário é formado pela leitura dos restos **de baixo para cima**.

---

**a) 1001 (decimal)**  
1001 ÷ 2 = 500 resto 1  
500 ÷ 2 = 250 resto 0  
250 ÷ 2 = 125 resto 0  
125 ÷ 2 = 62 resto 1  
62 ÷ 2 = 31 resto 0  
31 ÷ 2 = 15 resto 1  
15 ÷ 2 = 7 resto 1  
7 ÷ 2 = 3 resto 1  
3 ÷ 2 = 1 resto 1  
1 ÷ 2 = 0 resto 1  

→ 1001 = 1111101001<sub>2</sub>  

**Resposta:** 11 1110 1001

---

**b) 256 (decimal)**  
256 ÷ 2 = 128 resto 0  
128 ÷ 2 = 64 resto 0  
64 ÷ 2 = 32 resto 0  
32 ÷ 2 = 16 resto 0  
16 ÷ 2 = 8 resto 0  
8 ÷ 2 = 4 resto 0  
4 ÷ 2 = 2 resto 0  
2 ÷ 2 = 1 resto 0  
1 ÷ 2 = 0 resto 1  

→ 256 = 100000000<sub>2</sub>  

**Resposta:** 1 0000 0000

---

**c) 4095 (decimal)**  
4095 ÷ 2 = 2047 resto 1  
2047 ÷ 2 = 1023 resto 1  
1023 ÷ 2 = 511 resto 1  
511 ÷ 2 = 255 resto 1  
255 ÷ 2 = 127 resto 1  
127 ÷ 2 = 63 resto 1  
63 ÷ 2 = 31 resto 1  
31 ÷ 2 = 15 resto 1  
15 ÷ 2 = 7 resto 1  
7 ÷ 2 = 3 resto 1  
3 ÷ 2 = 1 resto 1  
1 ÷ 2 = 0 resto 1  

→ 4095 = 111111111111<sub>2</sub>  

**Resposta:** 1111 1111 1111

---

**d) 545 (decimal)**  
545 ÷ 2 = 272 resto 1  
272 ÷ 2 = 136 resto 0  
136 ÷ 2 = 68 resto 0  
68 ÷ 2 = 34 resto 0  
34 ÷ 2 = 17 resto 0  
17 ÷ 2 = 8 resto 1  
8 ÷ 2 = 4 resto 0  
4 ÷ 2 = 2 resto 0  
2 ÷ 2 = 1 resto 0  
1 ÷ 2 = 0 resto 1  

→ 545 = 1000100001<sub>2</sub>  

**Resposta:** 10 0010 0001
{{< /solucao >}}

---
### Exercício 1.5

Converta os seguintes números binários em decimal.

<ol type="a">
    <li>11 0100 1101</li>
    <li>1001 0010</li>
    <li>1 0000</li>
    <li>1 0001</li>
</ol>

{{< solucao nivel="iniciante" >}}
Para converter um número binário em decimal, somamos as potências de 2 correspondentes às posições onde há dígito 1.

---

**a) 1101001101<sub>2</sub>**  
= 1·2<sup>9</sup> + 1·2<sup>8</sup> + 0·2<sup>7</sup> + 1·2<sup>6</sup> + 0·2<sup>5</sup> + 0·2<sup>4</sup> + 1·2<sup>3</sup> + 1·2<sup>2</sup> + 0·2<sup>1</sup> + 1·2<sup>0</sup>  
= 512 + 256 + 64 + 8 + 4 + 1  
= 845  

**Resposta:** 845

---

**b) 10010010<sub>2</sub>**  
= 1·2<sup>7</sup> + 0·2<sup>6</sup> + 0·2<sup>5</sup> + 1·2<sup>4</sup> + 0·2<sup>3</sup> + 0·2<sup>2</sup> + 1·2<sup>1</sup> + 0·2<sup>0</sup>  
= 128 + 16 + 2  
= 146  

**Resposta:** 146

---

**c) 10000<sub>2</sub>**  
= 1·2<sup>4</sup>  
= 16  

**Resposta:** 16

---

**d) 10001<sub>2</sub>**  
= 1·2<sup>4</sup> + 1·2<sup>0</sup>  
= 16 + 1  
= 17  

**Resposta:** 17
{{< /solucao >}}

---
### Exercício 1.6
Essa questão é mais filosófica que matemática. Nesta seção afirmei que binário
tem mais a ver com a existência ou não de uma grandeza física do que com a
comparação de opostos. Assim, ligado e não ligado é diferente de pensar em
ligado e desligado; aceso e não aceso é diferente de aceso e apagado. Na realidade,
se quisermos usar desligado, o par binário seria não desligado; no caso de
apagado, seria não apagado. Pense a respeito.

{{< solucao nivel="avançado" >}}
A ideia central é que o sistema binário não representa, originalmente, dois estados opostos no sentido conceitual (como “ligado” versus “desligado”), mas sim a **presença ou ausência de uma grandeza física**.

Em circuitos digitais, por exemplo, não existe uma “essência do desligado”. O que há é:
- presença de tensão (nível alto)
- ausência de tensão (nível baixo)

Por isso, faz mais sentido interpretar os estados como:
- “ligado” e **“não ligado”**
- “aceso” e **“não aceso”**

e não como pares simétricos como “ligado/desligado” ou “aceso/apagado”. Esses últimos carregam uma interpretação linguística de oposição, mas fisicamente o sistema distingue apenas se uma grandeza está presente ou não.

Essa perspectiva é importante porque aproxima o conceito de número binário da sua implementação real: dispositivos eletrônicos detectam níveis (faixas de tensão), não significados semânticos.

Em resumo, o binário é menos sobre dualidade filosófica e mais sobre **detecção de estados físicos discretos**.
{{< /solucao >}}

---
## 1.3 Octal e Hexadecimal
### Exercício 1.7
Converta os seguintes números binários em octais e hexadecimais.

<ol type="a">
    <li>1101001101</li>
    <li>10010010</li>
    <li>10000</li>
    <li>110001111</li>
    <li>1010111011110011</li>
</ol>

{{< solucao nivel="iniciante" >}}
Para converter de binário para octal e hexadecimal, agrupamos os bits:

- **Octal (base 8):** grupos de 3 bits (da direita para a esquerda)
- **Hexadecimal (base 16):** grupos de 4 bits (da direita para a esquerda)

Completamos com zeros à esquerda, se necessário.

---

**a) 1101001101<sub>2</sub>**

Octal:  
001 101 001 101  
→ 1 5 1 5 → 1515<sub>8</sub>  

Hexadecimal:  
0011 0100 1101  
→ 3 4 D → 34D<sub>16</sub>  

---

**b) 10010010<sub>2</sub>**

Octal:  
010 010 010  
→ 2 2 2 → 222<sub>8</sub>  

Hexadecimal:  
1001 0010  
→ 9 2 → 92<sub>16</sub>  

---

**c) 10000<sub>2</sub>**

Octal:  
010 000  
→ 2 0 → 20<sub>8</sub>  

Hexadecimal:  
0001 0000  
→ 1 0 → 10<sub>16</sub>  

---

**d) 110001111<sub>2</sub>**

Octal:  
110 001 111  
→ 6 1 7 → 617<sub>8</sub>  

Hexadecimal:  
0001 1000 1111  
→ 1 8 F → 18F<sub>16</sub>  

---

**e) 1010111011110011<sub>2</sub>**

Octal:  
001 010 111 011 110 011  
→ 1 2 7 3 6 3 → 127363<sub>8</sub>  

Hexadecimal:  
1010 1110 1111 0011  
→ A E F 3 → AEF3<sub>16</sub>  

{{< /solucao >}}

---
### Exercício 1.8
Converta os seguintes números octais em binários.

<ol type="a">
    <li>71</li>
    <li>416</li>
    <li>1110</li>
    <li>756</li>
    <li>1237</li>
</ol>

{{< solucao nivel="iniciante" >}}
Para converter de octal para binário, substituímos **cada dígito octal por um grupo de 3 bits** (pois 8 = 2<sup>3</sup>):

0 → 000  
1 → 001  
2 → 010  
3 → 011  
4 → 100  
5 → 101  
6 → 110  
7 → 111  

---

**a) 71<sub>8</sub>**  
7 → 111  
1 → 001  
→ 111001<sub>2</sub>  

---

**b) 416<sub>8</sub>**  
4 → 100  
1 → 001  
6 → 110  
→ 100001110<sub>2</sub>  

---

**c) 1110<sub>8</sub>**  
1 → 001  
1 → 001  
1 → 001  
0 → 000  
→ 001001001000<sub>2</sub>  
(Removendo zeros à esquerda: 1001001000<sub>2</sub>)  

---

**d) 756<sub>8</sub>**  
7 → 111  
5 → 101  
6 → 110  
→ 111101110<sub>2</sub>  

---

**e) 1237<sub>8</sub>**  
1 → 001  
2 → 010  
3 → 011  
7 → 111  
→ 001010011111<sub>2</sub>  
(Removendo zeros à esquerda: 1010011111<sub>2</sub>)  

{{< /solucao >}}

---
### Exercício 1.9
Converta os seguintes números hexadecimais em binários.

<ol type="a">
    <li>71</li>
    <li>AB</li>
    <li>F810</li>
    <li>1A</li>
    <li>AAB0</li>
</ol>

{{< solucao nivel="iniciante" >}}
Para converter de hexadecimal para binário, substituímos **cada dígito hexadecimal por um grupo de 4 bits** (pois 16 = 2<sup>4</sup>):

0 → 0000  
1 → 0001  
2 → 0010  
3 → 0011  
4 → 0100  
5 → 0101  
6 → 0110  
7 → 0111  
8 → 1000  
9 → 1001  
A → 1010  
B → 1011  
C → 1100  
D → 1101  
E → 1110  
F → 1111  

---

**a) 71<sub>16</sub>**  
7 → 0111  
1 → 0001  
→ 01110001<sub>2</sub>  
(Removendo zero à esquerda: 111 0001<sub>2</sub>)

---

**b) AB<sub>16</sub>**  
A → 1010  
B → 1011  
→ 1010 1011<sub>2</sub>  

---

**c) F810<sub>16</sub>**  
F → 1111  
8 → 1000  
1 → 0001  
0 → 0000  
→ 1111 1000 0001 0000<sub>2</sub>  

---

**d) 1A<sub>16</sub>**  
1 → 0001  
A → 1010  
→ 00011010<sub>2</sub>  
(Removendo zeros à esquerda: 1 1010<sub>2</sub>)

---

**e) AAB0<sub>16</sub>**  
A → 1010  
A → 1010  
B → 1011  
0 → 0000  
→ 1010 1010 1011 0000<sub>2</sub>  

{{< /solucao >}}

---
## 1.4 Kilo e Kibi
### Exercício 1.10
Seu provedor de Internet vende as velocidades de 15, 30, 50 e 100 Mbits/s. Calcule
as velocidades em MiBits/s.

{{< solucao nivel="iniciante" >}}
A diferença está no prefixo:

- **Mbit (megabit)** = 10<sup>6</sup> bits  
- **Mibit (mebibit)** = 2<sup>20</sup> bits = 1.048.576 bits  

Para converter de Mbit/s para Mibit/s:

1 Mbit/s = 10<sup>6</sup> / 2<sup>20</sup> ≈ 0,9537 Mibit/s

---

**a) 15 Mbit/s**  
15 × 0,9537 ≈ 14,31 Mibit/s  

---

**b) 30 Mbit/s**  
30 × 0,9537 ≈ 28,61 Mibit/s  

---

**c) 50 Mbit/s**  
50 × 0,9537 ≈ 47,68 Mibit/s  

---

**d) 100 Mbit/s**  
100 × 0,9537 ≈ 95,37 Mibit/s  

---

### Resumo

| Mbit/s | Mibit/s |
| ------ | ------- |
| 15     | 14,31   |
| 30     | 28,61   |
| 50     | 47,68   |
| 100    | 95,37   |

{{< /solucao >}}

### Exercício 1.11
Você resolve comprar um disco externo para fazer cópia de segurança de seus
arquivos. Analisando os arquivos, você percebe que precisa de 1 TiB de armazenamento. Qual deve ser o tamanho mínimo do disco que você deve
comprar, se o fabricante usa unidades do sistema métrico decimal para
comercializar seus produtos?

{{< solucao nivel="iniciante" >}}
O ponto central é a diferença entre os prefixos binários e decimais:

- 1 TiB (tebibyte) = 2<sup>40</sup> bytes = 1.099.511.627.776 bytes  
- 1 TB (terabyte) = 10<sup>12</sup> bytes = 1.000.000.000.000 bytes  

Queremos saber quantos **TB (decimais)** são necessários para armazenar **1 TiB**:

1 TiB = 2<sup>40</sup> bytes ≈ 1,0995 × 10<sup>12</sup> bytes  
⇒ 1 TiB ≈ 1,0995 TB  

---

### Conclusão

Para armazenar 1 TiB, você precisa de um disco de **pelo menos 1,1 TB**.

Na prática, como os discos são vendidos em tamanhos padronizados, o mínimo recomendado é:

**Resposta:** um disco de **2 TB**.

{{< /solucao >}}

---
## 1.5 Binário Sinalizado

### Exercício 1.12
Escreva o binário equivalente a –215 em sinal/valor, complemento a 1 e
complemento a 2, usando 16 bits para a codificação.

{{< solucao nivel="iniciante" >}}
Primeiro, representamos o valor absoluto em binário com 16 bits.

215 (decimal):

215 ÷ 2 = 107 resto 1  
107 ÷ 2 = 53 resto 1  
53 ÷ 2 = 26 resto 1  
26 ÷ 2 = 13 resto 0  
13 ÷ 2 = 6 resto 1  
6 ÷ 2 = 3 resto 0  
3 ÷ 2 = 1 resto 1  
1 ÷ 2 = 0 resto 1  

→ 215 = 11010111<sub>2</sub>  

Com 16 bits:  
0000 0000 1101 0111

---

### a) Sinal e valor

O bit mais significativo indica o sinal:
- 0 → positivo
- 1 → negativo

Mantemos o valor e colocamos sinal 1:

→ 1000 0000 1101 0111

---

### b) Complemento a 1

Invertemos todos os bits do valor positivo:

0000000011010111  
→ 1111 1111 0010 1000

---

### c) Complemento a 2

Somamos 1 ao complemento a 1:


```
1111 1111 0010 1000
                + 1
-------------------
1111 1111 0010 1001
```

---

### Resumo

| Representação   | Valor binário       |
| --------------- | ------------------- |
| Sinal e valor   | 1000 0000 1101 0111 |
| Complemento a 1 | 1111 1111 0010 1000 |
| Complemento a 2 | 1111 1111 0010 1001 |

{{< /solucao >}}

---
### Exercício 1.13
Escreva o binário equivalente a +215 em sinal/valor, complemento a 1 e
complemento a 2, usando 16 bits para a codificação.

{{< solucao nivel="iniciante" >}}
Primeiro, representamos o número 215 em binário com 16 bits.

215 (decimal):

215 ÷ 2 = 107 resto 1  
107 ÷ 2 = 53 resto 1  
53 ÷ 2 = 26 resto 1  
26 ÷ 2 = 13 resto 0  
13 ÷ 2 = 6 resto 1  
6 ÷ 2 = 3 resto 0  
3 ÷ 2 = 1 resto 1  
1 ÷ 2 = 0 resto 1  

→ 215 = 11010111<sub>2</sub>  

Com 16 bits:  
0000 0000 1101 0111

---

### a) Sinal e valor

Para números positivos, o bit de sinal é 0:

→ 0000 0000 1101 0111

---

### b) Complemento a 1

Para números positivos, a representação é igual ao valor binário:

→ 0000 0000 1101 0111

---

### c) Complemento a 2

Também igual ao valor binário para números positivos:

→ 0000 0000 1101 0111

---

### Resumo

| Representação   | Valor binário       |
| --------------- | ------------------- |
| Sinal e valor   | 0000 0000 1101 0111 |
| Complemento a 1 | 0000 0000 1101 0111 |
| Complemento a 2 | 0000 0000 1101 0111 |

Ou seja, números positivos têm a mesma representação nas três codificações.

{{< /solucao >}}

---

### Exercício 1.14

Escreva o binário equivalente a -215 em excesso–511. Qual o menor n possível
para escrever este número? Quantos bits são necessários neste caso?

{{< solucao nivel="iniciante" >}}
Na representação em **excesso–N**, somamos uma constante (viés) ao valor antes de convertê-lo para binário.

Aqui, N = 511.

---

#### Passo 1: aplicar o viés

Valor: −215  

−215 + 511 = 296  

---

#### Passo 2: converter 296 para binário

296 ÷ 2 = 148 resto 0  
148 ÷ 2 = 74 resto 0  
74 ÷ 2 = 37 resto 0  
37 ÷ 2 = 18 resto 1  
18 ÷ 2 = 9 resto 0  
9 ÷ 2 = 4 resto 1  
4 ÷ 2 = 2 resto 0  
2 ÷ 2 = 1 resto 0  
1 ÷ 2 = 0 resto 1  

→ 296 = 100101000<sub>2</sub>  

---

### Resultado em excesso–511

**1 0010 1000**

---

## Representação de –215 no menor número de bits

### Qual o menor n?

Para representar **–215** em complemento a 2, precisamos que o intervalo cubra esse valor.

Com **n bits**, o menor valor representável é -(2<sup>n-1</sup>-1) e o maior valor é +2<sup>n-1</sup>.


Precisamos que:

-(2<sup>n-1</sup>-1) ≤ -215 

Verificando:

2<sup>7</sup> - 1 = 127 < 215 ⇒ insuficiente

2<sup>8</sup> - 1  = 255 ≥ 215 ⇒ suficiente

N = 2<sup>8</sup> - 1 = 255.


Portanto **N = 255**.



### Resumo

- Representação (excesso–511): 01 0010 1000<sub>2</sub>  
- Menor N possível: 255  (excesso-255)  
- Número mínimo de bits: 9


{{< /solucao >}}

---
### Exercício 1.15
Escreva os binários equivalentes a 120 e a 8, usando 8 bits, e execute a soma
desses números binários. Dependendo da representação usada para números
inteiros, essa soma vai causar o chamado transbordamento (overflow). Como
interpretar esse resultado de acordo com as representações de números binários
negativos?

{{< solucao nivel="iniciante" >}}

Primeiro, representamos os números com 8 bits.

### Conversão para binário

120 (decimal):  
120 = 0111 1000<sub>2</sub>  

8 (decimal):  
8 = 0000 1000<sub>2</sub>  

---

### Soma binária
<pre>
 0111 1000  
+0000 1000
----------
=1000 0000  
</pre>

Resultado: **1000 0000<sub>2</sub>**

---

### Interpretação do resultado

O valor obtido depende da forma de interpretação dos números binários:

#### 1) Sem sinal (unsigned)

10000000<sub>2</sub> = 128  

Não há erro — o resultado está correto.

---

#### 2) Sinal e valor

O bit mais significativo indica o sinal:

- 1 → número negativo  
- valor = 0000000  

Resultado: **−0** (uma representação ambígua)

➡️ Aqui ocorre **overflow**, pois a soma de dois números positivos resultou em um valor negativo.

---

#### 3) Complemento a 1

Invertendo os bits para obter o valor:

10000000 → 01111111 = 127  

Resultado: **−127**

➡️ Também há **overflow**, pois o resultado correto (128) está fora do intervalo representável (−127 a +127).

---

#### 4) Complemento a 2

Interpretando diretamente:

10000000<sub>2</sub> = −128  

➡️ Há **overflow**, pois somamos dois números positivos e obtivemos um negativo.  
O intervalo com 8 bits é de −128 a +127, e 128 não pode ser representado.

---

### Conclusão

- A soma binária produz **10000000<sub>2</sub>**  
- O resultado correto (128) não cabe em 8 bits com sinal  
- O comportamento varia conforme a representação:
  - unsigned: correto (128)
  - sinal/valor: −0 (inconsistência)
  - complemento a 1: −127
  - complemento a 2: −128

➡️ **Overflow ocorre quando o resultado matemático não pode ser representado com o número de bits disponível.**

{{< /solucao >}}

---
## 1.6 Números Reais
### Exercício 1.16
Escreva os binários equivalentes a –215,5 na notação com vírgula fixa. Qual o
número mínimo de bits necessários?

{{< solucao nivel="iniciante" >}}
Queremos representar −215,5 em **notação de vírgula fixa**. Primeiro, convertemos o valor absoluto.

---

### Parte inteira (215)

215 ÷ 2 = 107 resto 1  
107 ÷ 2 = 53 resto 1  
53 ÷ 2 = 26 resto 1  
26 ÷ 2 = 13 resto 0  
13 ÷ 2 = 6 resto 1  
6 ÷ 2 = 3 resto 0  
3 ÷ 2 = 1 resto 1  
1 ÷ 2 = 0 resto 1  

→ 215 = 11010111<sub>2</sub>  

---

### Parte fracionária (0,5)

0,5 × 2 = 1,0 → parte inteira 1  

→ 0,5 = 0,1<sub>2</sub>  

---

### Representação em binário

215,5 = 11010111,1<sub>2</sub>  

---

### Inclusão do sinal

Usando sinal e valor:

→ −215,5 = 1 11010111,1<sub>2</sub>  

---

### Número mínimo de bits

- Parte inteira: 8 bits  
- Parte fracionária: 1 bit  
- Sinal: 1 bit  

Total: **10 bits**

---

### Resultado final

**1 11010111,1<sub>2</sub>**

---

### Observação

A notação de vírgula fixa exige definir previamente quantos bits são usados para a parte inteira e para a parte fracionária. Aqui usamos o mínimo necessário, mas em sistemas reais essa divisão é fixa (por exemplo, 16.16, 8.8 etc.).

{{< /solucao >}}

---
### Exercício 1.17
Escreva os binários equivalentes a –215,5 usando o padrão IEEE 754 para precisão
simples e dupla.

{{< solucao nivel="iniciante" >}}
Queremos representar −215,5 no padrão IEEE 754.

---

## Passo 1: converter para binário

Parte inteira:  
215 = 11010111<sub>2</sub>  

Parte fracionária:  
0,5 = 0,1<sub>2</sub>  

→ 215,5 = 11010111,1<sub>2</sub>  

---

## Passo 2: normalização

11010111,1<sub>2</sub> = 1,10101111<sub>2</sub> × 2<sup>7</sup>  

---

## Passo 3: sinal

Número negativo → bit de sinal = **1**

---

## Precisão simples (32 bits)

- Sinal: 1 bit  
- Expoente: 8 bits (viés = 127)  
- Mantissa: 23 bits  

### Expoente

7 + 127 = 134  
134 = 10000110<sub>2</sub>  

### Mantissa

Removendo o 1 implícito:  
10101111 e completando com zeros:

10101111000000000000000  

---

### Resultado (32 bits)

**1 10000110 10101111000000000000000**

---

## Precisão dupla (64 bits)

- Sinal: 1 bit  
- Expoente: 11 bits (viés = 1023)  
- Mantissa: 52 bits  

### Expoente

7 + 1023 = 1030  
1030 = 10000000110<sub>2</sub>  

### Mantissa

10101111 seguido de zeros até 52 bits:

1010111100000000000000000000000000000000000000000000  

---

### Resultado (64 bits)

**1 10000000110 1010111100000000000000000000000000000000000000000000**

---

## Observação

Como 0,5 tem representação binária exata, o número −215,5 é representado **sem erro de arredondamento** em IEEE 754.

{{< /solucao >}}

---
### Exercício 1.18
Escreva os binários equivalentes a 0,1 usando o padrão IEEE 754 para precisão
simples e dupla.

{{< solucao nivel="iniciante" >}}
Queremos representar 0,1 (decimal) no padrão IEEE 754.

---

## Passo 1: converter para binário

Multiplicações sucessivas por 2:

0,1 × 2 = 0,2 → 0  
0,2 × 2 = 0,4 → 0  
0,4 × 2 = 0,8 → 0  
0,8 × 2 = 1,6 → 1  
0,6 × 2 = 1,2 → 1  
0,2 × 2 = 0,4 → 0  
...

→ padrão periódico:

0,1 = 0,00011001100110011...<sub>2</sub>  

---

## Passo 2: normalização

0,0001100110011... = 1,1001100110011... × 2<sup>−4</sup>  

---

## Passo 3: sinal

Número positivo → bit de sinal = **0**

---

## Precisão simples (32 bits)

- Sinal: 1 bit  
- Expoente: 8 bits (viés = 127)  
- Mantissa: 23 bits  

### Expoente

−4 + 127 = 123  
123 = 01111011<sub>2</sub>  

### Mantissa (com arredondamento)

10011001100110011001101  

---

### Resultado (32 bits)

**0 01111011 10011001100110011001101**

---

## Precisão dupla (64 bits)

- Sinal: 1 bit  
- Expoente: 11 bits (viés = 1023)  
- Mantissa: 52 bits  

### Expoente

−4 + 1023 = 1019  
1019 = 01111111011<sub>2</sub>  

### Mantissa (com arredondamento)

1001100110011001100110011001100110011001100110011001  

---

### Resultado (64 bits)

**0 01111111011 1001100110011001100110011001100110011001100110011001**

---

## Observação

O número 0,1 **não tem representação finita em binário**, resultando em uma dízima periódica.  
Por isso, IEEE 754 armazena uma aproximação, o que pode causar pequenos erros de precisão em cálculos.

{{< /solucao >}}

---