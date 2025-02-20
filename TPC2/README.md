# TPC2 - Relatório sobre Parser de Ficheiros CSV

**Data:** 19 de Fevereiro de 2024  

## Autor
- **Nome:** Diogo Alexandre Gomes Silva
- **Número:** 104183

  ![Foto do Autor](../foto.png)


## 1. Introdução
Este relatório documenta a implementação e funcionamento de um programa em Python que lê, processa e analisa ficheiros CSV que contém informações sobre obras musicais. O programa trata corretamente campos multi-linha e realiza análises sobre compositores, períodos musicais e obras.

## 2. Estrutura do Código
O programa está dividido em três partes principais:

1. **Leitura e processamento do ficheiro** (`ler_ficheiro`)
2. **Análise dos dados** (`analisar_dados`)
3. **Demonstração dos resultados** (`exibir_resultados`)

Além disto, existe um bloco principal que orquestra a execução do programa.

## 3. Explicação das Funções

### 3.1 `ler_ficheiro(lines)`
Esta função lê um ficheiro CSV, lidando com campos que contêm quebras de linha dentro de aspas.

- Junta todas as linhas num único bloco de texto.
- Separa corretamente os registos considerando aspas que podem envolver múltiplas linhas.
- Utiliza expressões regulares para separar os campos corretamente.
- Retorna os dados processados como uma lista de listas.

### 3.2 `analisar_dados(linhas_processadas)`
Esta função analisa os dados e extrai informações relevantes:

- Identifica as colunas principais (`_id`, `nome`, `periodo`, `compositor`).
- Filtra dados inválidos.
- Conta quantas obras existem por período.
- Agrupa as obras por período.
- Retorna um dicionário com:
  - Lista ordenada de compositores.
  - Contagem de obras por período.
  - Obras agrupadas por período.

### 3.3 `exibir_resultados(resultados)`
Esta função exibe os resultados obtidos:

- Compositores ordenadamente.
- Contagem das obras por período.
- Obras agrupadas por período.

## 4. Execução do Programa
O programa solicita ao utilizador o nome do ficheiro a ser processado. Se o ficheiro for encontrado, ele:

1. Lê e processa o conteúdo do ficheiro CSV.
2. Analisa os dados extraídos.
3. Exibe os resultados ao utilizador.

Em caso de erro (ex: ficheiro não encontrado ou formato inválido), uma mensagem de erro é apresentada.

## 5. Exemplo de Entrada e Saída

### 5.1 Exemplo de Entrada (CSV)
```
nome;desc;anoCriacao;periodo;compositor;duracao;_id
"Sinfonia nº 5";"Uma das sinfonias mais famosas";1808;Clássico;"Ludwig van Beethoven";31:45;001
"Canon em D";"Peça icônica do período barroco";1680;Barroco;"Johann Pachelbel";4:15;002
```

### 5.2 Exemplo de Saída (Resultados)
```
Lista ordenada de compositores:
- Johann Pachelbel
- Ludwig van Beethoven

Distribuição de obras por período:
- Barroco: 1 obra
- Clássico: 1 obra

Obras agrupadas por período:
Barroco:
- Canon em D (ID: 002)

Clássico:
- Sinfonia nº 5 (ID: 001)
```

## 6. Conclusão
Este programa oferece uma solução robusta para processar ficheiros CSV com formatação complexa, extraindo informações valiosas sobre obras musicais. Usar expressões regulares e tratar adequadamente campos multi-linha garante um processamento correto e eficiente.

## 7. Possíveis Melhorias
- Suporte para outros delimitadores além de `;`.
- Melhor tratamento de erros e logs mais detalhados.
- Maior atenção á acentuação.





