import re, pathlib
from rcssmin import cssmin
from rjsmin import jsmin

files = ["reset-1-distraido.html", "reset-2-apagado.html",
         "reset-3-guerra-interna.html", "reset-4-limite.html", "diagnostico.html"]
SENT = "@@BLK"

for f in files:
    html = pathlib.Path(f).read_text()
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)  # sem comentarios
    blocks = []

    def repl(m):
        tag, attrs, body = m.group(1), m.group(2), m.group(3)
        body = cssmin(body) if tag.lower() == "style" else jsmin(body)
        blocks.append("<%s%s>%s</%s>" % (tag, attrs, body, tag))
        return SENT + str(len(blocks) - 1) + SENT

    html = re.sub(r'(?is)<(style|script)([^>]*)>(.*?)</\1>', repl, html)
    html = re.sub(r'\s*\n\s*', ' ', html)   # tira TODAS as quebras de linha
    html = re.sub(r'>\s+<', '><', html)     # aperta entre tags
    html = html.strip()
    html = re.sub(SENT + r'(\d+)' + SENT, lambda m: blocks[int(m.group(1))], html)
    pathlib.Path(f).write_text(html)

    nl = html.count("\n")
    print(f, "| linhas_extra:", nl, "| tem_style:", "<style" in html,
          "| botao_hotmart:", "pay.hotmart.com/C106036012S" in html,
          "| KB:", len(html) // 1024)
