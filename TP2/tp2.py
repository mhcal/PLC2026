import re
import sys
import os

def markdown_to_html(txt):
    # headers: verificamos o nível através da quantidade de #s
    def header_repl(match):
        level = len(match.group(1))
        content = match.group(2)
        return f"<h{level}>{content}</h{level}>"
    
    # `re.sub` pode receber como parâmetro repls (match -> string)
    html = re.sub(r'^(#{1,6})\s+(.*)$', header_repl, txt, flags=re.MULTILINE)
    
    # bold
    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)
    
    # itálico
    html = re.sub(r'\*(.*?)\*', r'<i>\1</i>', html)
    
    # images
    html = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', html)
    
    # links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    
    # lista numerada
    def list_repl(match):
        block = match.group(0)
        items = re.sub(r'^\d+\.\s+(.*)$', r'<li>\1</li>', block, flags=re.MULTILINE)
        return f"<ol>\n{items}</ol>\n"
        
    html = re.sub(r'(?:^\d+\.\s+.*(?:\n|$))+', list_repl, html, flags=re.MULTILINE)
    
    return html

def boilerplate(html_body):
    return f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{os.path.basename(input_file)}</title>
</head>
<body>
{html_body}
</body>
</html>"""

if __name__ == "__main__":
    input_file = "foo.md"
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    
    # verifica se o ficheiro tem extensão md
    if not input_file.lower().endswith('.md'):
        print(f"ficheiro '{input_file}' não é um ficheiro .md")
        sys.exit(1)
        
    # verifica se o ficheiro existe no sistema
    if not os.path.exists(input_file):
        print(f"o ficheiro '{input_file}' não foi encontrado")
        sys.exit(1)
        
    # lê o conteúdo do ficheiro md
    f = open(input_file, 'r', encoding='utf-8')
    md_content = f.read()
        
    # converte o conteudo para html
    html_body = markdown_to_html(md_content)
    html = boilerplate(html_body)

    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.html"
    
    # escreve o resultado no novo ficheiro html
    f = open(output_file, 'w', encoding='utf-8')
    f.write(html)

    print('success')
