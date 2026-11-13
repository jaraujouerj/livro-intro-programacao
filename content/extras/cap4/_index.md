---
title: "Capítulo 4 — Subalgoritmos"
weight: 4
bookCollapseSection: true
---

{{< katex />}}

# 📘 Exercícios — Capítulo 4 
# Subalgoritmos

[← Voltar](../)

---

### Exercícios Propostos

**1. Calculadora de Potência:** Escreva uma função chamada `potencia(base, expoente)` que retorne o valor da base elevada ao expoente. Não utilize o operador `**`, utilize um laço `for` para o cálculo.

**2. Área do Círculo com Módulo:** Crie uma função que receba o raio de um círculo e retorne sua área. Utilize a constante `math.pi` do módulo `math`.

**3. Simulação de Dados (RPG):** Usando o módulo `random`, crie uma função `lancar_dados(quantidade, faces)` que simule o lançamento de múltiplos dados (ex: 3 dados de 6 faces) e retorne a soma total.

**4. Verificador de Primalidade:** Escreva uma função `e_primo(n)` que receba um número inteiro e retorne `True` se for primo e `False` caso contrário.

**5. Média Ponderada Funcional:** Crie uma função que receba três notas e seus respectivos pesos, retornando a média ponderada.

**6. Volume de uma Esfera:** Escreva uma função que calcule o volume de uma esfera (\\( V = \frac{4}{3} \pi r^3 \\)) dado o raio. Utilize o módulo `math`.

**7. Gerador de Senhas Aleatórias:** Crie uma função que receba um comprimento `n` e gere uma sequência de `n` dígitos numéricos aleatórios como uma string, usando `random.randint()`.

### Exercícios sobre Escopo e Parâmetros

**8. Demonstração de Escopo:** Escreva um programa que possua uma variável global `x` e uma função que defina uma variável local também chamada `x`. Imprima os valores em diferentes pontos para demonstrar a precedência.

**9. Função com Valores Padrão:** Crie uma função `saudar(nome, mensagem="Olá")` que imprima uma saudação. Demonstre a chamada da função com um e com dois parâmetros.

**10. Troca de Valores:** Escreva uma função que receba dois valores e tente trocá-los. Explique, com base na imutabilidade dos inteiros em Python, por que a troca não se reflete fora da função se os valores forem apenas números.

**11. Modificação de Listas:** Crie uma função que receba uma lista de números e multiplique cada elemento por um fator. Explique por que, diferentemente dos inteiros, a lista original é alterada.

### Exercícios sobre Retorno Múltiplo e Tuplas

**12. Estatísticas de Lista:** Escreva uma função que receba uma lista de números e retorne simultaneamente o maior valor, o menor valor e a média (como uma tupla).

**13. Conversão de Tempo:** Crie uma função que receba um total de segundos e retorne uma tupla contendo o equivalente em horas, minutos e segundos.

**14. Raízes de Equação do Segundo Grau:** Escreva uma função que receba os coeficientes `a`, `b` e `c` e retorne as duas raízes da equação (se existirem). Use `math.sqrt()`.

### Exercícios sobre Tratamento de Erros (Exceções)

**15. Entrada de Inteiro Segura:** Escreva uma função `ler_inteiro(mensagem)` que utilize `try...except` para garantir que o usuário digite um valor inteiro válido, repetindo a pergunta até o sucesso.

**16. Divisão com Proteção:** Crie uma função de divisão que capture a exceção `ZeroDivisionError` e retorne uma mensagem de erro amigável em vez de interromper o programa.

**17. Validação de Índice:** Escreva uma função que receba uma lista e um índice, tentando imprimir o elemento. Capture a exceção `IndexError` caso o índice seja inválido.

### Exercícios de Integração e Docstrings

**18. Função Documentada:** Escolha qualquer um dos exercícios anteriores e adicione uma `docstring` apropriada, seguindo as recomendações do livro (descrevendo o que faz, não como faz).

**19. Simulador de Caixa com Funções:** Refaça o exercício do caixa eletrônico (saque) dividindo a lógica em funções: uma para validar o valor (usando `try...except`) e outra para calcular a distribuição de notas.

**20. Menu Principal (`main`):** Escreva um programa que contenha três funções matemáticas diferentes e uma função `main()`. A `main()` deve apresentar um menu ao usuário para escolher qual função executar, tratando entradas inválidas.

---

### Monte Carlo

Com base na lógica do **Método de Monte Carlo** apresentada na Seção 4.4 do livro, que utiliza a probabilidade e a geração de coordenadas aleatórias para estimar valores matemáticos, resolva os 5 exercícios semelhantes.

Para todos os exercícios, utilize a estrutura modular sugerida no material: crie funções específicas para **gerar dados aleatórios**, para **testar a condição** e para **realizar o cálculo final**.

**1. Estimativa da Área sob a Curva \\(y = x^2\\)**

Escreva um programa que estime a área sob a parábola \\(y = x^2\\) no intervalo de \\(x = 0\\) a \\(x = 1\\).
*   **Lógica:** Gere coordenadas \\((x, y)\\) aleatórias onde \\(0 \le x \le 1\\) e \\(0 \le y \le 1\\).
*   **Condição:** O ponto está "dentro" da área se \\(y \le x^2\\).
*   **Cálculo:** A área estimada será a razão entre pontos dentro e o total de pontos (já que a área do quadrado total é \\(1 \times 1 = 1\\)).

**2. Volume de uma Esfera (Monte Carlo 3D)**

Expanda o conceito de Pi para a terceira dimensão e estime o volume de uma esfera de raio 1 dentro de um cubo de lado 2.
*   **Lógica:** Gere três coordenadas aleatórias \\((x, y, z)\\) no intervalo de 0 a 1 (representando um oitavo do cubo).
*   **Condição:** O ponto está dentro da esfera se \\(\sqrt{x^2 + y^2 + z^2} \le 1\\). Use a função `math.sqrt()` ou manipule as potências.
*   **Cálculo:** O volume da esfera é dado por \\(V = \frac{4}{3}\pi r^3\\). A proporção de pontos dentro multiplicada por 8 fornecerá o volume total estimado.

**3. Área de um Triângulo no Plano Cartesiano**

Crie um programa que use Monte Carlo para estimar a área de um triângulo com vértices em \\((0,0)\\), \\((1,0)\\) e \\((0,1)\\) dentro de um quadrado unitário.
*   **Lógica:** Gere pontos \\((x, y)\\) aleatórios entre 0 e 1.
*   **Condição:** O ponto está dentro do triângulo se \\(y \le 1 - x\\).
*   **Cálculo:** Compare o resultado da simulação com o cálculo geométrico clássico (\\(\frac{base \times altura}{2}\\)).

**4. Área de uma Elipse**

Estime a área de uma elipse definida pela equação \\(\frac{x^2}{a^2} + \frac{y^2}{b^2} \le 1\\), com \\(a=2\\) e \\(b=1\\).
*   **Lógica:** Gere pontos aleatórios dentro de um retângulo que envolva a elipse (neste caso, \\(x\\) entre \\(-2\\) e \\(2\\), e \\(y\\) entre \\(-1\\) e \\(1\\)).
*   **Condição:** Teste se a soma das frações da equação é menor ou igual a 1.
*   **Cálculo:** A área estimada será a (proporção de acertos) \\(\times\\) (área total do retângulo).

**5. Integração da Função Seno**

Calcule a área sob a curva da função \\(\sin(x)\\) no intervalo de \\(0\\) a \\(\pi\\) radianos.
*   **Lógica:** Gere coordenadas \\(x\\) entre \\(0\\) e `math.pi` e coordenadas $y$ entre \\(0\\) e \\(1\\)  (o valor máximo do seno).
*   **Condição:** O ponto está abaixo da curva se \\(y \le \sin(x)\\).
*   **Cálculo:** A área estimada é a proporção de pontos sob a curva multiplicada pela área do retângulo base (\\(\pi \times 1\\)).


---