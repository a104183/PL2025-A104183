import re

def convert_markdown_to_html(markdown_text):
    """Converte um texto Markdown para HTML."""

    # Converte os cabeçalhos
    lines = markdown_text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('### '):
            lines[i] = f"<h3>{line[4:]}</h3>"
        elif line.startswith('## '):
            lines[i] = f"<h2>{line[3:]}</h2>"
        elif line.startswith('# '):
            lines[i] = f"<h1>{line[2:]}</h1>"

    text = '\n'.join(lines)

    # Converte texto em negrito
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    # Converte texto em itálico
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)

    # Converte as imagens 
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'\n<img src="\2" alt="\1"/>\n', text)

    # Converte os links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    # Converte as listas numeradas 
    list_pattern = re.compile(r'(?:^\d+\.\s.*(?:\n|$))+', re.MULTILINE)

    def convert_list(match):
        items = match.group(0).strip().split('\n')
        html_items = [f"<li>{item[item.find('.') + 2:]}</li>" for item in items]
        return "<ol>\n" + "\n".join(html_items) + "\n</ol>\n"

    text = list_pattern.sub(convert_list, text)

    return text


def main():
    ficheiro_markdown = input("Insira o nome do ficheiro Markdown: ")

    try:
        with open(ficheiro_markdown, 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        html_output = convert_markdown_to_html(markdown_text)

        ficheiro_html = ficheiro_markdown.replace('.md', '.html')
        with open(ficheiro_html, 'w', encoding='utf-8') as f:
            f.write(html_output)

        print(f"Conversão concluída! Ficheiro HTML salvo como {ficheiro_html}")

    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
