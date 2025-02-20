import re

def ler_ficheiro(lines):
    conteudo = "".join(lines)
    
    linhas_formatadas = []
    linha_atual = ""
    dentro_de_aspas = False
    
    for char in conteudo:
        if char == '"':
            dentro_de_aspas = not dentro_de_aspas
        
        linha_atual += char
        
        if char == '\n' and not dentro_de_aspas:
            if linha_atual.strip():
                linhas_formatadas.append(linha_atual.strip())
            linha_atual = ""
    
    if linha_atual.strip():
        linhas_formatadas.append(linha_atual.strip())
    
    dados = []
    for linha in linhas_formatadas:
        if not linha.strip():
            continue
        
        campos = []
        padrao = r'(?:^|;)\s*(?:"((?:[^"]|"")*)"|([^;\r\n]*))(?=;|$)'
        
        for match in re.finditer(padrao, linha + ";"):
            campo = match.group(1) if match.group(1) is not None else match.group(2)
            if campo is not None:
                campo = campo.replace('""', '"').strip()
                campos.append(campo)
        
        if campos:
            dados.append(campos)
    
    return dados


def analisar_dados(linhas_processadas):
    if not linhas_processadas:
        raise ValueError("Erro: O ficheiro está vazio ou mal formatado.")

    cabecalho = linhas_processadas[0]
    try:
        idx_id = cabecalho.index("_id")
        idx_nome = cabecalho.index("nome")
        idx_periodo = cabecalho.index("periodo")
        idx_compositor = cabecalho.index("compositor")
    except ValueError:
        raise ValueError(f"Erro: Nome de coluna não encontrado. Colunas detectadas: {cabecalho}")

    compositores = set()
    contagem_periodos = {}
    obras_por_periodo = {}

    for linha in linhas_processadas[1:]:
        if len(linha) <= max(idx_id, idx_nome, idx_periodo, idx_compositor):
            continue

        id_obra = linha[idx_id].strip()
        nome_obra = linha[idx_nome].strip()
        periodo = linha[idx_periodo].strip()
        compositor = linha[idx_compositor].strip()

        if not nome_obra or not periodo or not compositor:
            continue

        compositores.add(compositor)
        contagem_periodos[periodo] = contagem_periodos.get(periodo, 0) + 1
        obras_por_periodo.setdefault(periodo, []).append((nome_obra, id_obra))

    return {
        'compositores': sorted(compositores),
        'contagem_periodos': dict(sorted(contagem_periodos.items())),
        'obras_por_periodo': {p: sorted(t) for p, t in sorted(obras_por_periodo.items())}
    }


def exibir_resultados(resultados):
    print("\n1. Lista ordenada de compositores:")
    for compositor in resultados['compositores']:
        print(f"   - {compositor}")

    print("\n2. Quantidade de obras por período:")
    for periodo, quantidade in resultados['contagem_periodos'].items():
        print(f"   - {periodo}: {quantidade} obras")

    print("\n3. Obras agrupadas por período:")
    for periodo, obras in resultados['obras_por_periodo'].items():
        print(f"\n   {periodo}:")
        for nome, id_obra in obras:
            print(f"   - {nome} ({id_obra})")


if __name__ == "__main__":
    nome_ficheiro = input("Escreva o nome do ficheiro: ").strip()
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        linhas_processadas = ler_ficheiro(linhas)
        resultados = analisar_dados(linhas_processadas)
        exibir_resultados(resultados)
    except FileNotFoundError:
        raise FileNotFoundError(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

