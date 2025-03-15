import json
import re

STOCK_FILE = "stock.json"

MOEDAS_ACEITES = [("2e", 200), ("1e", 100), ("50c", 50), ("20c", 20), ("10c", 10), ("5c", 5), ("2c", 2), ("1c", 1)]

def carregar_stock():
    try:
        with open(STOCK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_stock(stock):
    with open(STOCK_FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, indent=4)

def listar_stock(stock):
    print("\n🛒 Lista de Produtos Disponíveis 🛒")
    print("--------------------------------------------------------------")
    print("  COD   |              Nome              | Quantidade | Preço ")
    print("--------------------------------------------------------------")
    for item in stock:
        print(f"{item['cod']:^7} | {item['nome']:^30} | {item['quant']:^10} | {item['preco']:.2f}€")
    print("--------------------------------------------------------------\n")

def processar_moedas(comando):
    padrao = re.findall(r'\b(\d+e|\d+c)\b', comando.lower())
    return sum(valor for moeda, valor in MOEDAS_ACEITES if moeda in padrao)

def selecionar_produto(comando, stock, saldo):
    match = re.search(r'SELECIONAR\s+(\w+)', comando)
    if not match:
        print("❌ Comando inválido.")
        return saldo
    
    cod = match.group(1)
    for item in stock:
        if item['cod'] == cod:
            if item['quant'] > 0 and saldo >= int(item['preco'] * 100):
                item['quant'] -= 1
                saldo -= int(item['preco'] * 100)
                print(f"Pode retirar o produto dispensado \"{item['nome']}\"")
            else:
                print(f"❌ Saldo insuficiente para {item['nome']} ({item['preco']}€).")
            return saldo
    
    print("❌ Produto inexistente.")
    return saldo

def calcular_troco(saldo):
    troco = {}
    for moeda, valor in MOEDAS_ACEITES:
        while saldo >= valor:
            if moeda not in troco:
                troco[moeda] = 0
            troco[moeda] += 1
            saldo -= valor
    
    return troco

def main():
    stock = carregar_stock()
    saldo = 0
    print("👋 MÁQUINA: Bom dia. Estou disponível para atender o seu pedido.")
    
    while True:
        comando = input(">> ").strip().upper()
        
        if comando == "LISTAR":
            listar_stock(stock)
        elif comando.startswith("MOEDA"):
            valor_inserido = processar_moedas(comando)
            saldo += valor_inserido
            print(f"💰 MÁQUINA: Saldo = {saldo // 100}e{saldo % 100}c")
        elif comando.startswith("SELECIONAR"):
            saldo = selecionar_produto(comando, stock, saldo)
            print(f"💰 MÁQUINA: Saldo = {saldo // 100}e{saldo % 100}c")
        elif comando == "SAIR":
            troco = calcular_troco(saldo)
            if not troco:
                troco_str = "0x 0c"
            else:
                troco_str = ", ".join(f"{v}x {k}" for k, v in troco.items())
            print(f"💵 MÁQUINA: Pode retirar o troco: {troco_str}. Até à próxima !")
            guardar_stock(stock)
            break
        else:
            print("❌ Comando inválido. Tente novamente.")

if __name__ == "__main__":
    main()
