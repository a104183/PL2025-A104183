def processar_ficheiro(nome_ficheiro):
    soma = 0
    somar_ativo = True  

    try:
        with open(nome_ficheiro, 'r') as ficheiro:
            for linha in ficheiro:
                i = 0
                while i < len(linha):
                    if linha[i].isdigit():
                        numero_atual = ''
                        while i < len(linha) and linha[i].isdigit():
                            numero_atual += linha[i]
                            i += 1
                        if somar_ativo:
                            soma += int(numero_atual)
                    elif linha[i:i+2].lower() == 'on':
                        somar_ativo = True
                        i += 2
                    elif linha[i:i+3].lower() == 'off':
                        somar_ativo = False
                        i += 3
                    elif linha[i] == '=':
                        print(f"{soma}")
                        i += 1
                    else:
                        i += 1

    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")

tente_novamente = True
while tente_novamente:
    nome_ficheiro = input("Insira o nome do ficheiro: ")
    if nome_ficheiro.strip():
        processar_ficheiro(nome_ficheiro)
        tente_novamente = False
    else:
        print("Erro: O nome do ficheiro não pode estar vazio. Tente novamente.")
