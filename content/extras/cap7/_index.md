---
title: "Capítulo 7 — Recursão"
weight: 7
bookCollapseSection: true
---
{{< katex />}}

# 📘 Exercícios — Capítulo 7 
# Recursão

[← Voltar](../)

---
### Exercícios Propostos

**1. Multiplicação por Somas Sucessivas:** Escreva uma função recursiva que calcule o produto de dois números inteiros (\\(a \times b\\)) utilizando apenas a operação de soma. Lembre-se: \\(a \times b = a + (a \times (b-1))\\).

**2. Potência Recursiva:** Crie uma função que receba a **base** e o **expoente** e retorne o resultado da potência (\\(base^{expoente}\\)) de forma recursiva, sem utilizar o operador `**`.

**3. Soma de Dígitos:** Escreva uma função recursiva que receba um número inteiro positivo e retorne a **soma de seus dígitos** (Exemplo: 123 retorna \\(1+2+3 = 6\\)).

**4. Máximo Divisor Comum (MDC):** Implemente o algoritmo de Euclides de forma recursiva para encontrar o MDC de dois números: \\(MDC(a, b) = MDC(b, a \bmod b)\\), com o caso trivial sendo quando o resto é zero.

**5. Resto da Divisão:** Crie uma função recursiva que calcule o **resto da divisão inteira** entre dois números usando apenas subtrações sucessivas.

**6. Somatório de N:** Escreva uma função que receba um número \\(n\\) e retorne a **soma de todos os inteiros** de 1 até \\(n\\).

### Exercícios de Processamento de Sequências

**7. Soma de Elementos de uma Lista:** Desenvolva uma função recursiva que receba uma lista de números e retorne a **soma total de seus elementos**.

**8. Maior Valor da Lista:** Crie uma função que encontre o **maior elemento** em uma lista de forma recursiva, comparando o primeiro elemento com o maior do restante da lista.

**9. Contador de Ocorrências:** Escreva uma função recursiva que conte quantas vezes um determinado valor aparece em uma lista (Exemplo: contar quantos "5" existem em `[5, 2, 8, 5, 3, 5, 1.]`).

**10. Verificador de Ordenação:** Desenvolva uma função recursiva que retorne `True` se uma lista estiver **ordenada de forma crescente** e `False` caso contrário.

**11. Busca Binária Recursiva:** Refine o algoritmo de busca binária da Seção 2.10 transformando-o em uma **função recursiva** que divide o universo de busca a cada chamada.

**12. Pertencimento:** Escreva uma função recursiva que verifique se um elemento está presente em uma lista, sem usar o operador `in`.

### Exercícios de Strings e Lógica

**13. Remoção de Caracteres:** Crie uma função recursiva que receba uma string e um caractere, retornando a string original **sem as ocorrências** desse caractere.

**14. Troca de Letras:** Escreva uma função que receba uma string e substitua recursivamente todas as letras "a" por "*".

**15. Fatorial Duplo:** O fatorial duplo de \\(n\\) (\\(n!!\\)) é o produto de todos os números de \\(n\\) até 1 com o mesmo passo de 2 (Exemplo: \\(5!! = 5 \times 3 \times 1\\)). Implemente-o recursivamente.

**16. Conversão de Base:** Desenvolva uma função recursiva que receba um número decimal e retorne sua representação em **binário** como uma string.

### Exercícios de Análise e Otimização

**17. Visualização da Pilha:** Pegue a função de fatorial criada no exercício 7.4 e desenhe a **evolução da pilha de execução** para a chamada `fat(4)`, identificando os endereços de retorno e as variáveis locais em cada nível.

**18. Fibonacci com Lista:** Refaça o exercício da série de Fibonacci utilizando uma **lista** para armazenar os resultados intermediários (técnica de memorização), comparando a velocidade com a versão recursiva simples.

**19. Limite da Pilha:** Escreva um pequeno programa que chame uma função recursiva sem caso trivial e observe qual é a mensagem de erro emitida pelo Python quando o **limite da pilha** é atingido.

**20. Fila Invertida:** Imagine que na "Fila de Programadores Míopes" (Seção 7.1), as pessoas resolvessem passar a informação do último para o primeiro. Como você adaptaria a lógica recursiva para que o primeiro da fila soubesse o **tamanho total da fila** apenas com uma resposta vinda de trás?.


---