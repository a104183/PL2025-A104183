# TPC3 - Relatório Conversor Markdown para HTML

**Data:** 27 de Fevereiro de 2025

## Autor
- **Nome:** Diogo Alexandre Gomes Silva
- **Número:** 104183

  ![Foto do Autor](../foto.png)

## 1. Introdução
Este documento apresentará o funcionamento do meu código em Python que converte um ficheiro em formato Markdown para HTML. O objetivo é transformar elementos básicos da sintaxe Markdown como cabeçalhos, formatação de texto, imagens e links em suas respectivas tags HTML equivalentes, preservando a estrutura do documento original.

## 2. Funcionamento Geral
O código solicita ao utilizador o nome de um ficheiro Markdown, processa-o e aplica as seguintes regras:
1. **Cabeçalhos Markdown** são convertidos para tags HTML `<h1>`, `<h2>` e `<h3>`.
2. **Texto em negrito** delimitado por `**` é convertido para tags `<b>`.
3. **Texto em itálico** delimitado por `*` é convertido para tags `<i>`.
4. **Imagens** no formato `![alt](url)` são convertidas para tags `<img>`.
5. **Links** no formato `[texto](url)` são convertidos para tags `<a>`.
6. **Listas numeradas** são convertidas para tags `<ol>` e `<li>`.

## 3. Explicação do Código

### 3.1 Função Principal de Conversão
- A função `convert_markdown_to_html()` recebe um texto em Markdown e retorna o HTML resultante.
- Processa primeiro os cabeçalhos dividindo o texto em linhas.
- Utiliza expressões regulares para converter formatação, imagens, links e listas.

### 3.2 Processamento de Elementos
- **Cabeçalhos**: Verifica linhas que começam com `#`, `##` ou `###`.
- **Formatação**: Usa `re.sub()` para substituir padrões de negrito e itálico.
- **Elementos Visuais**: Transforma imagens e links com padrões específicos.
- **Listas Numeradas**: Utiliza expressões regulares mais complexas para identificar e converter.

### 3.3 Expressões Regulares Utilizadas
| Elemento | Padrão Regex | Substituição |
|------------|------|------|
| Texto negrito | `\*\*(.*?)\*\*` | `<b>\1</b>` |
| Texto itálico | `\*(.*?)\*` | `<i>\1</i>` |
| Imagens | `!\[(.*?)\]\((.*?)\)` | `<img src="\2" alt="\1"/>` |
| Links | `\[(.*?)\]\((.*?)\)` | `<a href="\2">\1</a>` |
| Listas numeradas | `(?:^\d+\.\s.*(?:\n|$))+` | Função especial de conversão |

## 4. Exemplo de Entrada e Saída

### **Entrada (`exemplo.md`)**
```markdown
# Título Principal
## Subtítulo

Este é um **texto em negrito** e este está em *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

![Imagem de exemplo](imagem.jpg)
[Link para site](https://www.exemplo.com)
```

### **Saída Esperada (`exemplo.html`)**
```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>

Este é um <b>texto em negrito</b> e este está em <i>itálico</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

<img src="imagem.jpg" alt="Imagem de exemplo"/>
<a href="https://www.exemplo.com">Link para site</a>
```

## 5. Conclusão
O código implementa um conversor básico de Markdown para HTML que funciona corretamente para elementos fundamentais da sintaxe. Embora não implemente todas as funcionalidades do Markdown (como citações, blocos de código ou tabelas), fornece uma base sólida que pode ser expandida. O tratamento de erros básico garante que o utilizador seja informado caso o ficheiro não seja encontrado ou ocorram outros problemas durante a execução.