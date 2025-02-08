def processar_ficheiro():
    soma = 0
    somar_ativo = True  

    try:
        with open("input.txt", 'r') as ficheiro:
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

# funçao para processar o ficheiro desejado
processar_ficheiro()
