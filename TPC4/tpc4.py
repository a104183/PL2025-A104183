import ply.lex as lex
import sys

# Definição dos tokens
tokens = (
    'COMENTARIO', 'SELECT', 'WHERE', 'LIMIT', 'VARIAVEL',
    'TIPO', 'PREFIX', 'NOME', 'LITERAL', 'LANGTAG', 'PONTUACAO', 'NUMERO'
)

# Palavras reservadas
palavras_reservadas = {
    'select': 'SELECT',
    'where': 'WHERE',
    'LIMIT': 'LIMIT',
    'a': 'TIPO'
}

# Definição dos padrões para cada token
def t_COMENTARIO(t):
    r'\#.*'
    return t

def t_PREFIX(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z0-9_]+'
    t.type = palavras_reservadas.get(t.value, 'PREFIX')
    return t

def t_VARIAVEL(t):
    r'\?[a-zA-Z][a-zA-Z0-9_]*'
    return t

def t_LITERAL(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_LANGTAG(t):
    r'@[a-zA-Z]+'
    return t

def t_NOME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]+'
    t.type = palavras_reservadas.get(t.value, 'NOME')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PONTUACAO(t):
    r'[\.\{\}\(\),]'
    return t

# Ignorar espaços/tabulações
t_ignore = ' \t'

# Contabilizar novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Erro: Caractere inválido '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Criar o lexer
def criar_lexer():
    return lex.lex()

# Função para processar um ficheiro
def analisar_ficheiro(nome_ficheiro):
    lexer = criar_lexer()
    
    try:
        with open(nome_ficheiro, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        
        lexer.input(conteudo)
        tokens_encontrados = [(t.type, t.value, t.lineno, t.lexpos) for t in lexer]
        return tokens_encontrados
    
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{nome_ficheiro}' não foi encontrado.")
        return []

# Execução principal
def main():
    if len(sys.argv) != 2:
        print("Uso: python3 lexer.py <ficheiro.txt>")
        sys.exit(1)
    
    nome_ficheiro = sys.argv[1]
    resultado = analisar_ficheiro(nome_ficheiro)
    
    for tipo, valor, linha, posicao in resultado:
        print(f"({tipo}, '{valor}', linha {linha}, posição {posicao})")

if __name__ == "__main__":
    main()
