---
title: "Capítulo 4 — Subalgoritmos"
weight: 4
bookCollapseSection: true

# Metadados (para uso futuro)
nivel: "iniciante"
topicos: ["entrada/saída", "variáveis"]
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