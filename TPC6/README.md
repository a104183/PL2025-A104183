# Analisador de Expressões Aritméticas

**Data:** 28 de Março de 2025

## Autor
- **Nome:** Diogo Alexandre Gomes Silva
- **Número:** 104183

![Foto do Autor](../foto.png)

## 1. Introdução
Este relatório apresenta a implementação de um analisador sintático para expressões matemáticas em Python. O programa permite a análise e avaliação de expressões aritméticas, respeitando a precedência de operadores e estruturas de parênteses, sem utilizar bibliotecas externas para a análise sintática.

## 2. Estrutura do Código
O programa está organizado em três componentes principais:

1. **Tokenizador** (`classe Tokenizador`) - Responsável pela análise léxica, convertendo a expressão em tokens
2. **Analisador Sintático** (`classe AnalisadorLL1`) - Implementa o parser LL(1) que analisa e avalia as expressões
3. **Interface** (`função calcular_expressao`) - Fornece uma interface simples para utilização do analisador

## 3. Explicação das Classes e Funções

### 3.1 Classe Tokenizador
Esta classe implementa o analisador léxico do sistema:

- **Inicialização**: Recebe a expressão como texto e inicializa o ponteiro de posição
- **Método `proximo_token()`**: Identifica e classifica o próximo token da expressão
- **Reconhecimento de tokens**: Identifica números (inteiros e decimais), operadores (+, -, *, /) e parênteses
- **Método `consumir()`**: Verifica se o token atual corresponde ao esperado e avança para o próximo
- **Tratamento de espaços**: Ignora espaços em branco na entrada
- **Tratamento de erros**: Detecta caracteres inválidos e formatos incorretos de números

### 3.2 Classe AnalisadorLL1
Esta classe implementa o analisador sintático LL(1):

- **Gramática LL(1)**: Implementa uma gramática sem recursão à esquerda para expressões aritméticas
- **Funções de parsing**: Implementa funções para cada não-terminal da gramática
  - `expr()`: Processa expressões (adição e subtração)
  - `termo()`: Processa termos (multiplicação e divisão)
  - `fator()`: Processa fatores (números, expressões entre parênteses e negações)
- **Avaliação simultânea**: Calcula os resultados enquanto realiza a análise sintática
- **Tratamento de precedência**: Garante que multiplicação/divisão tenha precedência sobre adição/subtração
- **Suporte a parênteses**: Permite o agrupamento de expressões entre parênteses

### 3.3 Função de Interface
A função `calcular_expressao(expressao)` serve como interface para o analisador:
- Cria uma instância do analisador com a expressão fornecida
- Inicia o processo de análise a partir do não-terminal inicial (expr)
- Verifica se toda a expressão foi consumida corretamente
- Retorna o resultado calculado ou levanta exceções em caso de erros

### 3.4 Módulo Principal
O bloco `if __name__ == '__main__'` implementa uma interface de linha de comando simples:
- Solicita expressões ao usuário
- Utiliza a função `calcular_expressao` para processar cada entrada
- Exibe os resultados ou mensagens de erro
- Permite encerrar o programa com o comando 'sair'

## 4. Gramática LL(1) Implementada
A gramática implementada segue a estrutura LL(1), organizando as produções para evitar a recursão à esquerda:

```
expr   -> termo (('+' | '-') termo)*
termo  -> fator (('*' | '/') fator)*
fator  -> NUM | '(' expr ')' | '-' fator
```

Esta gramática assegura:
- Precedência correta dos operadores (multiplicação/divisão antes de adição/subtração)
- Prioridade das expressões entre parênteses
- Suporte para números negativos através do operador unário '-'
- Análise determinística, característica essencial do parsing LL(1)

## 5. Funcionamento do Analisador
O processo de análise e avaliação de uma expressão ocorre nas seguintes etapas:

1. **Tokenização**: A expressão é dividida em tokens (números, operadores, parênteses)
2. **Análise sintática**: Os tokens são processados de acordo com as regras da gramática
3. **Avaliação**: As operações são calculadas respeitando a precedência dos operadores
4. **Resultado**: O valor final é retornado ao usuário

O analisador implementa o método de análise descendente recursiva, característico dos parsers LL(1), onde cada não-terminal da gramática é representado por uma função que reconhece e processa a estrutura correspondente.

## 6. Exemplos de Entrada e Saída

### 6.1 Expressões de Exemplo
```
2+3
10-5*2
(3+4)*2
-5+7
2*(3+4)/2
```

### 6.2 Resultados Obtidos
```
2+3 = 5
10-5*2 = 0
(3+4)*2 = 14
-5+7 = 2
2*(3+4)/2 = 7
```

Os resultados demonstram:
- Precedência correta de operadores: em `10-5*2`, a multiplicação é realizada antes da subtração
- Processamento correto de parênteses: em `(3+4)*2`, a soma é realizada antes da multiplicação
- Suporte a operador unário: em `-5+7`, o número negativo é interpretado corretamente
- Expressões complexas: em `2*(3+4)/2`, a precedência e parênteses são respeitados

## 7. Conclusão
O analisador de expressões aritméticas demonstra a aplicação prática dos conceitos fundamentais de compiladores. A implementação manual, sem dependência de bibliotecas externas para o parsing, permite um entendimento mais profundo dos mecanismos de análise sintática.

O programa avalia corretamente expressões aritméticas com diferentes níveis de complexidade, respeitando a precedência de operadores e o agrupamento por parênteses. A estrutura de classes proporciona uma separação clara entre a análise léxica e sintática, facilitando a manutenção e extensão do código.
