from PIL import Image
import base64, io, pathlib, html as _h

SC = "/tmp/claude-0/-home-user-Leandrocunhaofc/f83181d0-989e-50b8-9412-4a867a3df75a/scratchpad/"
UP = "/root/.claude/uploads/f83181d0-989e-50b8-9412-4a867a3df75a/"
TPL = SC + "reset-masculino-vendas.html"

# ---- mockup do e-book (webp, fundo preto -> jpeg leve) ----
book = Image.open(UP+"45a434e1-IMG_7838.webp").convert("RGB")
w,h = book.size
# alvo ~ 620px de largura mantendo proporcao
scale = 620/w
book = book.resize((620, int(h*scale)), Image.LANCZOS)
buf = io.BytesIO(); book.save(buf,"JPEG",quality=86,optimize=True,progressive=True)
book_uri = "data:image/jpeg;base64,"+base64.b64encode(buf.getvalue()).decode()
print(f"Mockup e-book: {len(buf.getvalue())//1024} KB ({book.size[0]}x{book.size[1]})")

tpl = pathlib.Path(TPL).read_text()
assert tpl.count("__BOOK_DATA__")==1, tpl.count("__BOOK_DATA__")
tpl = tpl.replace("__BOOK_DATA__", book_uri)

# ---- LINK DO CHECKOUT (Hotmart) ----
CHECKOUT_BASE = "https://pay.hotmart.com/C106036012S?checkoutMode=10"
def checkout_for(src):
    sep = "&" if "?" in CHECKOUT_BASE else "?"
    return f"{CHECKOUT_BASE}{sep}sck={src}"

def bars(level):
    return "".join(f'<i class="{"on" if i<level else ""}"></i>' for i in range(4))

def diag(paras, impact, nxt):
    body = "".join(f"<p>{p}</p>" for p in paras)
    body += f'<p class="impact">{impact}</p>'
    body += f'<p class="next"><b>Próximo passo:</b> {nxt}</p>'
    return body

PROFILES = [
  dict(
    slug="1-distraido", level=1, src="distraido",
    cta="Quero retomar o controle — R$37",
    title="Homem Distraído — Seu Diagnóstico | Reset Masculino",
    name="Homem Distraído",
    sub="Você ainda não está dominado pelo automático — mas os sinais de dispersão já começaram.",
    paras=[
      "Seu resultado mostra que você ainda não está completamente dominado pelo automático, mas já existem sinais de dispersão.",
      "Talvez você ainda produza, trabalhe, cuide das suas responsabilidades e mantenha a aparência de que tudo está bem. Mas por dentro, alguns sinais já começaram a aparecer: perda de presença, dificuldade de constância, pequenas fugas, distrações e decisões adiadas.",
      "O maior perigo aqui é achar que ainda está tudo sob controle.",
    ],
    impact="O homem distraído não cai de uma vez. Ele vai se afastando de si mesmo aos poucos.",
    nxt="Você precisa fortalecer clareza, rotina e governo antes que a distração vire apagamento.",
  ),
  dict(
    slug="2-apagado", level=2, src="apagado",
    cta="Quero me reconectar — R$37",
    title="Homem Apagado — Seu Diagnóstico | Reset Masculino",
    name="Homem Apagado",
    sub="Você funciona por fora — mas pode estar se apagando por dentro.",
    paras=[
      "Seu resultado mostra que você pode estar funcionando por fora, mas se apagando por dentro.",
      "Você faz o que precisa ser feito. Trabalha, responde, resolve, segue a rotina. Mas talvez esteja sem brilho, sem presença, sem prazer no processo e sem conexão profunda com aquilo que antes fazia sentido.",
      "O homem apagado não necessariamente parou. Ele continua andando. O problema é que já não sabe exatamente para onde.",
    ],
    impact="O homem apagado não perdeu valor. Ele perdeu conexão.",
    nxt="Você precisa parar de tratar esse estado como apenas cansaço. Talvez seja hora de olhar para o que está sendo negligenciado dentro de você.",
  ),
  dict(
    slug="3-guerra-interna", level=3, src="guerra",
    cta="Quero vencer essa guerra — R$37",
    title="Homem em Guerra Interna — Seu Diagnóstico | Reset Masculino",
    name="Homem em Guerra Interna",
    sub="Existe uma batalha acontecendo dentro de você.",
    paras=[
      "Seu resultado mostra que existe uma batalha acontecendo dentro de você.",
      "Pode haver conflito entre quem você sabe que deveria ser e quem você tem conseguido ser no dia a dia. Talvez existam fugas, culpa, irritação, desânimo, procrastinação, distância emocional ou uma sensação constante de estar lutando sozinho.",
      "Esse é o estágio em que o homem começa a se cansar de si mesmo. Mas esse resultado não é uma sentença. É um chamado.",
    ],
    impact="A guerra que o homem não vence por dentro começa a destruir o que ele ama por fora.",
    nxt="Você precisa de verdade, direção e um primeiro protocolo de reconstrução.",
  ),
  dict(
    slug="4-limite", level=4, src="limite",
    cta="Quero sair do automático agora — R$37",
    title="Homem no Limite do Automático — Seu Diagnóstico | Reset Masculino",
    name="Homem no Limite do Automático",
    sub="O automático deixou de ser uma fase — e virou o seu padrão.",
    paras=[
      "Seu resultado mostra que o automático pode ter deixado de ser apenas uma fase e se tornado um padrão.",
      "Talvez você esteja cansado de prometer mudanças que não sustenta. Talvez esteja fugindo do silêncio, da dor, da responsabilidade ou de decisões que precisam ser tomadas. Talvez esteja presente para todos, mas ausente de si mesmo.",
      "Mas existe uma verdade importante: você não precisa resolver sua vida inteira hoje. Você precisa começar com verdade.",
    ],
    impact="O limite pode ser o lugar onde o homem finalmente para de fugir e começa a reconstruir.",
    nxt="Você precisa sair da repetição e entrar em um processo. O primeiro passo é entender as verdades que estão por trás desse estado.",
  ),
]

for p in PROFILES:
    out = tpl
    out = out.replace("{{TITLE}}", _h.escape(p["title"]))
    out = out.replace("{{STAGE_BARS}}", bars(p["level"]))
    out = out.replace("{{PROFILE_NAME}}", p["name"])
    out = out.replace("{{PROFILE_SUB}}", p["sub"])
    out = out.replace("{{PROFILE_CTA}}", p["cta"])
    out = out.replace("{{CHECKOUT_URL}}", checkout_for(p["src"]))
    out = out.replace("{{DIAGNOSIS_HTML}}", diag(p["paras"], p["impact"], p["nxt"]))
    # sanity: nenhum token restante
    leftover = [t for t in ("{{TITLE}}","{{STAGE_BARS}}","{{PROFILE_NAME}}","{{PROFILE_SUB}}","{{PROFILE_CTA}}","{{CHECKOUT_URL}}","{{DIAGNOSIS_HTML}}","__BOOK_DATA__") if t in out]
    assert not leftover, (p["slug"], leftover)
    fn = SC + f"reset-{p['slug']}.html"
    pathlib.Path(fn).write_text(out)
    print(f"OK  {fn.split('/')[-1]}  ({len(out)//1024} KB)")

print("\nGerado com sucesso as 4 paginas.")
