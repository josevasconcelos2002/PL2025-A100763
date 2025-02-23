import sys
import re

def markdown_to_html(path_to_file):
    html = ""
    in_ol = False  # Controle para listas ordenadas
    
    with open(path_to_file) as file:
        for line in file:
            line = line.strip()  # Remove espaços extras

            # Cabeçalhos
            line = re.sub(r'^# (.+)', r'<h1>\1</h1>', line)
            line = re.sub(r'^## (.+)', r'<h2>\1</h2>', line)
            line = re.sub(r'^### (.+)', r'<h3>\1</h3>', line)
            
            # Negrito
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            
            # Itálico
            line = re.sub(r'(?<!\*)\*(.*?)\*(?!\*)', r'<i>\1</i>', line)
            
            # Listas numeradas
            match = re.match(r'^(\d+)\. (.+)', line)
            if match:
                if not in_ol:
                    html += "<ol>\n"  # Abre a lista
                    in_ol = True
                html += f"<li>{match.group(2)}</li>\n"
                continue
            elif in_ol:
                html += "</ol>\n"  # Fecha a lista quando a sequência termina
                in_ol = False
            
            # Imagens
            line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)
            
            # Links
            line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)
            
            # Adiciona a linha ao HTML
            html += line + "\n"

    # Garante que a última lista seja fechada corretamente
    if in_ol:
        html += "</ol>\n"

    return html.strip()


def main(argc, argv):
    if(argc < 2):
        print("USAGE: tpc3.py <file>")
    
    elif(argc == 2):
        file = argv[1]
        html = markdown_to_html(file)
        print(html)
    
    
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)