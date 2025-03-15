# TPC5 - Relatório Máquina de Venda

**Data:** 13 de Março de 2025  

## Autor
- **Nome:** Diogo Alexandre Gomes Silva
- **Número:** 104183

![Foto do Autor](../foto.png)

## 1. Introdução
Este documento apresenta o funcionamento e a implementação de uma máquina de venda em Python. A aplicação permite a interação do utilizador com a máquina através de comandos específicos, processando a inserção de moedas, a seleção de produtos e a devolução do troco.

## 2. Funcionamento Geral
A máquina de venda funciona através de comandos introduzidos pelo utilizador, seguindo estas regras:

1. **LISTAR** - Exibe os produtos disponíveis e os respetivos preços.
2. **MOEDA <valor>** - Insere moedas na máquina.
3. **SELECIONAR <código>** - Permite comprar um produto, caso haja saldo suficiente.
4. **SAIR** - Devolve o troco e termina a interação.

As moedas aceites são: `2e`, `1e`, `50c`, `20c`, `10c`, `5c`, `2c`, `1c`.

## 3. Explicação do Código
### 3.1 Estrutura Principal
O programa é composto por várias funções:
- `carregar_stock()` - Lê os produtos do ficheiro `stock.json`.
- `guardar_stock()` - Guarda o estado atualizado do stock no ficheiro.
- `listar_stock()` - Exibe os produtos disponíveis na máquina.
- `processar_moedas()` - Converte os valores inseridos em saldo.
- `selecionar_produto()` - Processa a compra de um produto.
- `calcular_troco()` - Devolve o troco em moedas.

### 3.2 Gestão do Stock
O stock dos produtos está armazenado no ficheiro `stock.json`, que contém informações como código, nome, quantidade e preço de cada item. O stock é atualizado após cada compra, garantindo que os dados são sempre consistentes.

### 3.3 Compra de Produtos
- O utilizador insere moedas para aumentar o saldo.
- Ao selecionar um produto, verifica-se se o saldo é suficiente e se há stock.
- Caso a compra seja bem-sucedida, o saldo é ajustado e o stock atualizado no ficheiro.
- O troco é devolvido corretamente ao utilizador.

## 4. Exemplo de Interação
### **Entrada do Utilizador**
```plaintext
LISTAR
MOEDA 2e
MOEDA 50c
SELECIONAR C67
SELECIONAR E12
SAIR
```
### **Saída Esperada**
```plaintext
🛒 Lista de Produtos Disponíveis 🛒
cod    | nome            | quantidade | preço
-------------------------------------------
A23    | Água 0.5L      | 8          | 0.7€
C67    | Batatas Fritas | 9          | 1.5€
...
💰 MÁQUINA: Saldo = 2e50c
🎯 Pode retirar o produto dispensado "Batatas Fritas"
🎯 Pode retirar o produto dispensado "Café"
💵 MÁQUINA: Pode retirar o troco: 0x 0c. Até à próxima !
```

## 5. Conclusão
A implementação da máquina de venda cumpre os requisitos de gestão de stock, processamento de pagamentos e interação com o utilizador. O código foi otimizado para garantir a correta manipulação de moedas e troco, utilizando uma lista ordenada de moedas. O programa pode ser facilmente expandido para incluir novas funcionalidades, como relatórios de vendas ou interface gráfica.
