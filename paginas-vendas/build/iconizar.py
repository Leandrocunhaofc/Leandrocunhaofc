import re, base64, pathlib

SENT = "@@STASH"

def iconize(fn):
    html = pathlib.Path(fn).read_text()
    stash = []

    def st(m):
        stash.append(m.group(0))
        return SENT + str(len(stash) - 1) + SENT

    # protege <style> e <script> (nao converter o svg do url() do CSS)
    html = re.sub(r'(?is)<(style|script)\b[^>]*>.*?</\1>', st, html)

    count = [0]

    def conv(m):
        attrs, inner = m.group(1), m.group(2)
        if 'xmlns' not in attrs:
            attrs = ' xmlns="http://www.w3.org/2000/svg"' + attrs
        svg = '<svg' + attrs + '>' + inner + '</svg>'
        b64 = base64.b64encode(svg.encode('utf-8')).decode()
        count[0] += 1
        return '<img class="rmi" alt="" src="data:image/svg+xml;base64,' + b64 + '">'

    html = re.sub(r'(?is)<svg\b([^>]*)>(.*?)</svg>', conv, html)

    # restaura blocos; dentro do <style> troca seletor de elemento svg -> img.rmi
    def unst(m):
        block = stash[int(m.group(1))]
        if block[:6].lower() == "<style":
            block = re.sub(r'(?<=[ ,>])svg(?=[\s,:{])', 'img.rmi', block)
        return block

    html = re.sub(SENT + r'(\d+)' + SENT, unst, html)
    pathlib.Path(fn).write_text(html)
    return count[0]

for f in ["reset-masculino-vendas.html", "diagnostico.html"]:
    n = iconize(f)
    t = pathlib.Path(f).read_text()
    print(f, "| icones->img:", n, "| <svg restante:", t.count("<svg"), "| class=rmi:", t.count('class="rmi"'))
