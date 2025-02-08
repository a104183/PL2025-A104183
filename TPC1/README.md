# TPC1 - Relatório

## 1. Introdução
Este documento apresentará o funcionamento do meu código em Python que processa um ficheiro de texto, identificando e somando sequências de dígitos com base em três comandos de controlo (`on`, `off` e `=`). O objetivo é manter uma soma acumulada de todos os números encontrados, respeitando os comandos que podem surgir.

## 2. Funcionamento Geral
O código lê um ficheiro chamado `input.txt` e processa-o linha por linha, aplicando as seguintes regras:

1. **Números inteiros encontrados** são somados à soma total caso a soma esteja ativa.
2. **O comando `on`** ativa a soma (pode ser On,ON,oN ou on).

3. **O comando `off`** desativa a soma (pode ser OfF,OFF,oFf,etc).

4. **O comando `=`** imprime a soma acumulada até aquele ponto sem a passar a 0.
5. **O programa inicia com a soma ativada por padrão**.

## 3. Explicação do Código
### 3.1 Leitura do Ficheiro
- O ficheiro `input.txt` é aberto no modo de apenas leitura (`'r'`).

- O loop `for linha in ficheiro:` percorre o ficheiro linha por linha.

### 3.2 Processamento de Caracteres
- Cada linha é percorrida char a char com um loop `while`.

- Se encontrar um **dígito**, agrupa-o até encontrar um char não numérico.

- Se encontrar **'on'**, ativa a soma.

- Se encontrar **'off'**, desativa a soma.

- Se encontrar **'='**, imprime a soma atual sem a resetar.

### 3.3 Controlo de Fluxo com `elif`
| Condição | Ação |
|------------|------|
| `linha[i].isdigit()` | Lê um número e soma-o se `somar_ativo` estiver a `True` |
| `linha[i:i+2].lower() == 'on'` | Ativa a soma e avança 2 chars |
| `linha[i:i+3].lower() == 'off'` | Desativa a soma e avança 3 chars |
| `linha[i] == '='` | Imprime a soma acumulada e avança 1 char |

## 4. Exemplo de Entrada e Saída
### **Entrada (`input.txt`)**
```markdown
123On45Off67On89=On
123Off300=On2025-07-23Off45On67=
12Off34On56=78=
```

### **Saída Esperada**
```markdown
257
380
2502
2570
2648
```

## 5. Conclusão
O código cumpre todos os requisitos, processando corretamente o ficheiro de entrada e processando a soma acumulada com base nos comandos `on`, `off` e `=`. Caso o ficheiro não seja encontrado, o programa exibe uma mensagem de erro adequada.


