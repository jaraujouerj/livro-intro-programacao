# Site do livro *Introdução à Programação e aos Algoritmos*

Código-fonte do site com os exercícios resolvidos, os exercícios adicionais, os slides e os
trabalhos da disciplina **Algoritmos Computacionais I**, que complementam o livro de
J. A. Ribeiro (LTC, 2019). Endereço: <https://araujo.eng.uerj.br/livro/>.

O site é gerado com o [Hugo](https://gohugo.io/) e o tema [Hextra](https://github.com/imfing/hextra).

## Requisitos

* **Hugo 0.146 ou mais novo, na edição *extended*** (o tema exige). O site foi construído com a
  versão 0.160.
* **Git**, com o submódulo do tema (`themes/hextra`).

## Primeiros passos

```bash
git clone --recurse-submodules https://github.com/jaraujouerj/livro-intro-programacao.git
cd livro-intro-programacao
hugo server
```

Abra <http://localhost:1313/livro/>. Se você clonou sem `--recurse-submodules`, o Hugo não acha o
tema e a compilação falha. Corrija com:

```bash
git submodule update --init
```

Para gerar o site completo (a saída vai para `public/`, que não é versionada):

```bash
hugo --gc --minify
```

> As datas de "Última atualização" vêm do histórico do git (`enableGitInfo`). Em servidores que
> clonam só o último commit, as datas saem erradas: use um clone completo.

## Estrutura

```
content/
  _index.md            home
  errata.md            correções do livro, por versão
  exercicios/capN/     enunciados e soluções comentadas (um arquivo por capítulo)
  extras/capN/         exercícios adicionais, sem solução
  slides/              página dos slides e do plano de trabalho
  trabalhos/           trabalhos finais por engenharia (enunciado e guia do professor)
assets/code/           programas das soluções (exN.M_nome.py)
assets/css/custom.css  estilos próprios (caixa de solução, capa do livro)
static/slides/         PDFs dos slides
static/trabalhos/      PDFs e dados (CSV, ZIP) dos trabalhos
static/images/         capa do livro
layouts/shortcodes/    solucao, codefile, email
layouts/404.html       página de erro em português
i18n/pt-br.yaml        textos da interface em português do Brasil
themes/hextra/         tema (submódulo)
```

## Como editar

### Um exercício com solução

Em `content/exercicios/capN/_index.md`:

````markdown
### Exercício 7.1 — String na ordem inversa
Enunciado do exercício, em Markdown.

{{< solucao >}}
### Exercício — String na ordem inversa
{{< codefile "assets/code/ex7.1_string_inversa_recursiva.py" >}}

Explicação da solução.
{{< /solucao >}}
````

* `solucao` cria a caixa **recolhida** com "Ver solução". O texto dentro dela é Markdown comum.
* `codefile` mostra um arquivo do repositório como bloco de código, com realce e botão de copiar.
  O caminho parte da raiz do repositório. Para numerar as linhas:
  `{{< codefile "assets/code/arquivo.py" "linenos=true" >}}`.
* O título **dentro** da solução deve ser diferente do título do enunciado (por exemplo, sem o
  número). Títulos iguais geram âncoras duplicadas.
* Escreva identificadores de código entre crases: `` `math.tan()` ``.

### Cabeçalho (*front matter*) das páginas

```yaml
---
title: "Capítulo 4 — Subalgoritmos"
description: "Resumo de uma frase (aparece na busca e na prévia de links)."
weight: 4
---
```

* O **título da página** vem do `title`: não escreva um `# Título` no texto, ou ele aparecerá duas vezes.
* `weight` define a ordem no menu lateral.
* As seções `exercicios`, `extras`, `slides` e `trabalhos` usam `type: docs` (com `cascade`), o que
  ativa o menu lateral. Uma seção nova precisa do mesmo cabeçalho.

### Matemática

Fórmulas em LaTeX: `\( ... \)` no meio do texto e `$$ ... $$` em bloco.

### Slides

Os slides ficam em outro repositório (<https://github.com/jaraujouerj/algoritmos-computacionais-aulas>).
Para atualizar um PDF no site: compile com `make` naquele repositório e copie o arquivo para
`static/slides/`. A tabela em `content/slides/_index.md` aponta para cada PDF.

### Trabalhos por engenharia

Cada trabalho tem uma pasta em `content/trabalhos/<curso>/` (página do aluno e `professor.md`) e
os arquivos para download em `static/trabalhos/<curso>/`. Ao criar um novo, acrescente a linha na
tabela de `content/trabalhos/_index.md`. Atenção: o site é público, então o guia do professor
**não** fica protegido; não publique gabaritos nem soluções de referência.

### Textos da interface

O tema só traz português europeu. Os textos em português do Brasil estão em `i18n/pt-br.yaml`
(inclusive a linha de licença do rodapé).

## Tema

O Hextra é um submódulo, fixado em um commit. Para atualizar:

```bash
git -C themes/hextra fetch
git -C themes/hextra checkout <tag ou commit>
git add themes/hextra
```

O tema ainda está na série `0.x` e a configuração pode mudar entre versões. Depois de atualizar,
rode `hugo server` e confira a home, um capítulo, a busca e o modo escuro.

## Publicação

A publicação é manual: gera-se o site e transfere-se o resultado para o servidor por SFTP (por
exemplo, com o FileZilla).

1. Atualize o repositório e os submódulos (`git pull` e `git submodule update --init`).
2. Gere o site **numa pasta limpa**, para não levar arquivos de builds antigos:

   ```bash
   rm -rf public
   hugo --gc --minify
   ```

   O comando deve terminar **sem avisos nem erros**.
3. Transfira **o conteúdo** de `public/` (não a pasta `public` em si) para a pasta do servidor
   servida em `https://araujo.eng.uerj.br/livro/`.
4. Remova do servidor os arquivos que não existem mais em `public/`. Vários arquivos mudam de nome
   a cada alteração, porque levam um código no nome: o CSS do tema (em `css/compiled/`), os
   scripts de `js/` e o índice de busca (`pt-br.search...json` e `.js`, na raiz). Páginas renomeadas
   ou apagadas também ficam órfãs se ninguém as remover. Uma forma simples é limpar a pasta `livro/`
   do servidor antes de enviar, **desde que ela contenha só este site** (confira antes de apagar).
5. Confira no endereço real, com recarga sem cache (Ctrl+Shift+R): a home, um capítulo com uma
   solução aberta, a busca e a página de slides (um PDF deve abrir).

A `baseURL` está em `hugo.toml` e deve continuar terminando em `/livro/`. Se o endereço mudar,
altere-a antes de gerar o site.

## Licenças

* Soluções dos exercícios, exercícios adicionais e demais páginas escritas pelo autor:
  **CC BY-SA 4.0**, em [`LICENSE.md`](LICENSE.md).
* Os **enunciados** dos exercícios numerados são do livro e não são cobertos por essa licença.
* Código dos exemplos e slides: repositório de slides, com suas próprias licenças (MIT e CC BY-SA).
* O tema Hextra tem a licença do projeto original (MIT).
