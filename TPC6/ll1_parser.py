class Tokenizador:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.token_atual = None
        self.valor_atual = None
        self.proximo_token()
    
    def proximo_token(self):
        while self.pos < len(self.texto) and self.texto[self.pos].isspace():
            self.pos += 1
            
        if self.pos >= len(self.texto):
            self.token_atual = "EOF"
            return
            
        char = self.texto[self.pos]
        
        if char.isdigit() or char == '.':
            inicio = self.pos
            ponto_encontrado = False
            
            while self.pos < len(self.texto) and (self.texto[self.pos].isdigit() or self.texto[self.pos] == '.'):
                if self.texto[self.pos] == '.':
                    if ponto_encontrado:
                        break  
                    ponto_encontrado = True
                self.pos += 1
                
            self.token_atual = "NUM"
            self.valor_atual = float(self.texto[inicio:self.pos])
            if self.valor_atual.is_integer():
                self.valor_atual = int(self.valor_atual)
            return
            
        if char in "+-*/()":
            self.token_atual = char
            self.pos += 1
            return
            
        raise ValueError(f"Caractere inválido: {char}")
    
    def consumir(self, token_esperado):
        if self.token_atual == token_esperado:
            valor = self.valor_atual
            self.proximo_token()
            return valor
        else:
            raise ValueError(f"Token esperado: {token_esperado}, encontrado: {self.token_atual}")


class AnalisadorLL1:
    def __init__(self, texto):
        self.tokenizador = Tokenizador(texto)
    
    def expr(self):
        resultado = self.termo()
        
        while self.tokenizador.token_atual in ['+', '-']:
            op = self.tokenizador.token_atual
            self.tokenizador.proximo_token()
            termo_valor = self.termo()
            
            if op == '+':
                resultado += termo_valor
            else:  # op == '-'
                resultado -= termo_valor
                
        return resultado
    
    def termo(self):
        resultado = self.fator()
        
        while self.tokenizador.token_atual in ['*', '/']:
            op = self.tokenizador.token_atual
            self.tokenizador.proximo_token()
            fator_valor = self.fator()
            
            if op == '*':
                resultado *= fator_valor
            else:  # op == '/'
                resultado /= fator_valor
                
        return resultado
    
    def fator(self):
        if self.tokenizador.token_atual == 'NUM':
            return self.tokenizador.consumir('NUM')
            
        elif self.tokenizador.token_atual == '(':
            self.tokenizador.proximo_token()  # Consome '('
            resultado = self.expr()
            self.tokenizador.consumir(')')  # Espera e consome ')'
            return resultado
            
        elif self.tokenizador.token_atual == '-':
            self.tokenizador.proximo_token()  # Consome '-'
            return -self.fator()
            
        else:
            raise ValueError(f"Token inesperado: {self.tokenizador.token_atual}")


def calcular_expressao(expressao):
    try:
        analisador = AnalisadorLL1(expressao)
        resultado = analisador.expr()
        
        # Verifica se analisou toda a expressão
        if analisador.tokenizador.token_atual != "EOF":
            raise ValueError("Expressão inválida - caracteres não processados")
            
        return resultado
        
    except Exception as e:
        raise ValueError(f"Erro ao analisar a expressão: {str(e)}")


if __name__ == '__main__':
    print("Digite uma expressão para calcular ou 'sair' para encerrar.")
    
    while True:
        try:
            expressao = input("\n>> ")
            
            if expressao.lower() == 'sair':
                print("Encerrado!")
                break
                
            # Calcula e mostra o resultado
            resultado = calcular_expressao(expressao)
            print(resultado)
            
        except KeyboardInterrupt:
            print("\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro: {e}")