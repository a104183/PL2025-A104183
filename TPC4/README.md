# TPC - Relatório Analisador Léxico 

**Data:** 7 de Março de 2025  

## Autor
- **Nome:** Diogo Alexandre Gomes Silva
- **Número:** 104183

  ![Foto do Autor](../foto.png)

## 1. Introdução
Este documento apresentará o funcionamento do meu código em Python que implementa um analisador léxico (lexer) para uma linguagem de query utilizando a biblioteca PLY. O objetivo é analisar um ficheiro de texto, identificando e classificando os diferentes tokens presentes, como palavras-chave, variáveis, prefixos e outros elementos sintáticos.

## 2. Funcionamento Geral
O código lê um ficheiro escolhido pelo utilizador e processa-o, aplicando as seguintes regras para identificação de tokens:

1. **Comentários** - Linhas que começam com `#` são identificadas como comentários.
2. **Palavras-chave** - Identifica palavras reservadas como `select`, `where` e `LIMIT`.
3. **Variáveis** - Identifica variáveis que começam com `?` seguidos de caracteres alfanuméricos.
4. **Prefixos** - Reconhece prefixos no formato `prefixo:nome`.
5. **Literais** - Textos entre aspas duplas são identificados como literais.
6. **LangTag** - Tags de idioma que começam com `@` seguido de letras.
7. **Pontuação** - Caracteres especiais como `{}(),.` são identificados como pontuação.
8. **Números** - Sequências de dígitos são convertidas para valores inteiros.
9. **Nomes** - Identificadores que não se enquadram nas categorias anteriores.

## 3. Explicação do Código
### 3.1 Definição dos Tokens
- O programa define os tokens reconhecidos:
```python
tokens = (
    'COMENTARIO', 'SELECT', 'WHERE', 'LIMIT', 'VARIAVEL',
    'TIPO', 'PREFIX', 'NOME', 'LITERAL', 'LANGTAG', 'PONTUACAO', 'NUMERO'
)
```

### 3.2 Palavras Reservadas
- Um dicionário mapeia palavras reservadas para seus tipos de token:
```python
palavras_reservadas = {
    'select': 'SELECT',
    'where': 'WHERE',
    'LIMIT': 'LIMIT',
    'a': 'TIPO'
}
```

### 3.3 Funções de Reconhecimento
Para cada tipo de token, há uma função específica utilizando expressões regulares:

| Token | Padrão Regex | Descrição |
|------------|------|------|
| `t_COMENTARIO` | `r'\#.*'` | Linhas que começam com # |
| `t_PREFIX` | `r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z0-9_]+'` | Identificador seguido de : e outro identificador |
| `t_VARIAVEL` | `r'\?[a-zA-Z][a-zA-Z0-9_]*'` | ? seguido de letras e números |
| `t_LITERAL` | `r'"[^"]*"'` | Texto entre aspas duplas |
| `t_LANGTAG` | `r'@[a-zA-Z]+'` | @ seguido de letras |
| `t_NOME` | `r'[a-zA-Z_][a-zA-Z0-9_]+'` | Identificadores alfanuméricos |
| `t_NUMERO` | `r'\d+'` | Sequência de dígitos |
| `t_PONTUACAO` | `r'[\.\{\}\(\),]'` | Caracteres de pontuação |

### 3.4 Tratamento de Erros e Ignorados
- Espaços e tabulações são ignorados com `t_ignore = ' \t'`
- Novas linhas são contabilizadas para rastreamento de posição
- Caracteres inválidos geram mensagens de erro

### 3.5 Funções Principais
- `criar_lexer()`: Cria e retorna uma instância do analisador léxico
- `analisar_ficheiro(nome_ficheiro)`: Processa um ficheiro e retorna os tokens encontrados
- `main()`: Função principal que processa argumentos da linha de comando

## 4. Exemplo de Entrada e Saída
### **Entrada (`consulta.txt`)**
```sparql
# Consulta SPARQL de exemplo
select ?pessoa ?nome
where {
    ?pessoa a foaf:Person .
    ?pessoa foaf:name ?nome .
    ?pessoa foaf:age ?idade .
    FILTER(?idade > 18)
}
LIMIT 10
```

### **Saída Esperada**
```
(COMENTARIO, '# Consulta SPARQL de exemplo', linha 1, posição 0)
(SELECT, 'select', linha 2, posição 1)
(VARIAVEL, '?pessoa', linha 2, posição 8)
(VARIAVEL, '?nome', linha 2, posição 16)
(WHERE, 'where', linha 3, posição 22)
(PONTUACAO, '{', linha 3, posição 28)
(VARIAVEL, '?pessoa', linha 4, posição 34)
(TIPO, 'a', linha 4, posição 42)
(PREFIX, 'foaf:Person', linha 4, posição 44)
...
```

## 5. Conclusão
O código implementa com sucesso um analisador léxico para uma linguagem de query, identificando corretamente os diferentes elementos sintáticos da mesma. A utilização da biblioteca PLY simplifica o processo de definição e reconhecimento de tokens através de expressões regulares. O programa inclui ainda tratamento adequado de erros e mensagens informativas.
