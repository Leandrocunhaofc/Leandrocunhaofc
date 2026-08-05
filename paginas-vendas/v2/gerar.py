import base64, io, pathlib, re
from PIL import Image

SC = "/tmp/claude-0/-home-user-Leandrocunhaofc/f83181d0-989e-50b8-9412-4a867a3df75a/scratchpad/v2/"
UP = "/root/.claude/uploads/f83181d0-989e-50b8-9412-4a867a3df75a/"
CHECKOUT = "https://pay.hotmart.com/C106036012S?checkoutMode=10"

# foto do Leandro (circulo pequeno)
photo = Image.open(UP + "316deb0a-Leandro_Cunha_04.jpeg")
w, h = photo.size
crop = photo.crop((0, 250, w, 250 + w)).convert("RGB").resize((320, 320), Image.LANCZOS)
buf = io.BytesIO(); crop.save(buf, "JPEG", quality=82, optimize=True, progressive=True)
PHOTO = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

tpl = pathlib.Path(SC + "template-resultado.html").read_text()

def meter(level):
    return "".join('<i class="%s"></i>' % ("on" if i < level else "") for i in range(4))

def paras(items):
    return "".join("<p>%s</p>" % p for p in items)

PROFILES = [
 dict(
  key="distraido", level=1, file="resultado-distraido-2-0-teste.html",
  name="Homem Distraído",
  title="Homem Distraído — Seu Resultado | Reset Masculino",
  sub="Você ainda não foi dominado pelo automático. Mas ele já está decidindo pequenas coisas por você — e pequenas coisas viram padrão.",
  default_area="Trabalho e decisões",
  diagnosis=[
   "Seu resultado mostra dispersão. Você ainda produz, ainda entrega, ainda mantém a aparência de que está tudo sob controle — e é justamente isso que torna esse estágio perigoso.",
   "O que aparece nas suas respostas: o dia termina e o essencial continuou parado. As urgências dos outros decidem para onde vai sua energia. E o silêncio incomoda o suficiente para você buscar o celular antes de encarar o que está sentindo.",
   "Nada disso parece grave isoladamente. O problema é que nenhum homem se apaga de uma vez. Ele se dispersa primeiro."
  ],
  impact="O homem distraído não cai de uma vez. Ele vai se afastando de si mesmo aos poucos — e só percebe quando já está longe.",
  costs=[
   "<b>Tempo.</b> Você está gastando seus melhores anos executando o urgente e adiando o que constrói.",
   "<b>Presença.</b> Quem está perto de você recebe as suas sobras, não a sua atenção.",
   "<b>Confiança em si.</b> Cada promessa não cumprida com você mesmo corrói um pouco do homem que você acredita ser."
  ],
  cost_close="A boa notícia: neste estágio, uma correção pequena ainda muda a rota inteira. Daqui a seis meses, não vai ser mais pequena.",
  cta="Quero retomar o controle — R$37",
  cta_short="Começar meu Reset — R$37",
 ),
 dict(
  key="apagado", level=2, file="resultado-apagado-2-0-teste.html",
  name="Homem Apagado",
  title="Homem Apagado — Seu Resultado | Reset Masculino",
  sub="Por fora você funciona. Por dentro, faz tempo que você não sente presença no que faz.",
  default_area="Identidade e direção",
  diagnosis=[
   "Seu resultado mostra desconexão. Você cumpre o que esperam de você, resolve, provê, aparece — mas está executando funções, não vivendo.",
   "O que aparece nas suas respostas: você esteve com quem ama e só o seu corpo estava ali. Se afastou da fé, dos valores ou das convicções que antes organizavam sua vida, e não encontrou força para reagir.",
   "Isso não é preguiça e não é fraqueza. É o custo de anos funcionando no automático sem ninguém perguntar como você está."
  ],
  impact="O homem apagado não perdeu valor. Ele perdeu conexão — consigo, com os seus e com o que dá sentido ao esforço.",
  costs=[
   "<b>Vínculo.</b> Sua família tem a sua presença física e sente a sua ausência emocional.",
   "<b>Sentido.</b> Você continua andando, mas já não sabe exatamente para onde — e isso rouba a força do esforço.",
   "<b>Vontade.</b> Quanto mais tempo apagado, mais difícil fica reacender. O apagamento se acomoda."
  ],
  cost_close="Você não precisa de mais disciplina para carregar o vazio. Precisa reencontrar o eixo que fazia o esforço valer.",
  cta="Quero me reconectar — R$37",
  cta_short="Começar meu Reset — R$37",
 ),
 dict(
  key="guerra", level=3, file="resultado-guerra-2-0-teste.html",
  name="Homem em Guerra Interna",
  title="Homem em Guerra Interna — Seu Resultado | Reset Masculino",
  sub="Existe uma batalha acontecendo dentro de você — e ela está vazando para fora.",
  default_area="Relacionamentos e casamento",
  diagnosis=[
   "Seu resultado mostra conflito. Existe distância entre quem você sabe que deveria ser e quem você tem conseguido ser no dia a dia — e essa distância cobra caro todos os dias.",
   "O que aparece nas suas respostas: uma crítica simples te fecha ou te faz discutir mentalmente por horas. Tensão, medo, culpa e frustração saem de você como irritação, frieza, cobrança ou controle.",
   "Você já percebeu que a forma como reage está ferindo o que você mais quer proteger. E mesmo assim, na hora, é mais forte que você."
  ],
  impact="A guerra que o homem não vence por dentro começa a destruir o que ele ama por fora.",
  costs=[
   "<b>As pessoas que você ama.</b> Elas estão convivendo com a sua defesa, não com você.",
   "<b>Sua paz.</b> Você não descansa nem quando o dia acaba — a discussão continua na sua cabeça.",
   "<b>Sua autoridade.</b> Um homem que não governa a própria reação perde a autoridade que sustenta sua palavra."
  ],
  cost_close="Esse resultado não é uma sentença. É um chamado. E chamado ignorado por tempo demais vira arrependimento.",
  cta="Quero vencer essa guerra — R$37",
  cta_short="Começar meu Reset — R$37",
 ),
 dict(
  key="limite", level=4, file="resultado-limite-2-0-teste.html",
  name="Homem no Limite",
  title="Homem no Limite — Seu Resultado | Reset Masculino",
  sub="Você está carregando mais do que consegue sustentar por muito mais tempo. E sabe disso.",
  default_area="Identidade e direção",
  diagnosis=[
   "Seu resultado é o estágio mais crítico. O automático deixou de ser uma fase e virou o modo padrão de viver.",
   "O que aparece nas suas respostas: você já pensou “não posso continuar nesse ritmo” e seguiu assim mesmo, porque parecia que tudo dependia de você. Adiou conversas e decisões essenciais por não ter margem emocional para mais uma consequência.",
   "E chega ao fim do dia sem energia para conversar, decidir ou cuidar de si — querendo apenas que ninguém precise de você por algumas horas."
  ],
  impact="O limite pode ser o lugar onde o homem finalmente para de fugir e começa a reconstruir. Ou o lugar onde ele quebra em silêncio.",
  costs=[
   "<b>Sua saúde.</b> Corpo e mente já estão avisando. Aviso ignorado vira colapso.",
   "<b>Sua família.</b> Eles têm o homem exausto, não o homem inteiro. E percebem mais do que você imagina.",
   "<b>O tempo.</b> Cada mês nesse ritmo é um mês que não volta — e a conta chega junta."
  ],
  cost_close="Você não precisa resolver a vida inteira hoje. Precisa começar com verdade, e precisa começar agora.",
  cta="Quero sair do automático agora — R$37",
  cta_short="Começar meu Reset — R$37",
 ),
]

for p in PROFILES:
    out = tpl
    out = out.replace("{{TITLE}}", p["title"])
    out = out.replace("{{PROFILE_NAME}}", p["name"])
    out = out.replace("{{PROFILE_KEY}}", p["key"])
    out = out.replace("{{PROFILE_SUB}}", p["sub"])
    out = out.replace("{{METER}}", meter(p["level"]))
    out = out.replace("{{DEFAULT_INTENSITY}}", "Moderada" if p["level"] < 3 else "Elevada")
    out = out.replace("{{DEFAULT_AREA}}", p["default_area"])
    out = out.replace("{{DIAGNOSIS}}", paras(p["diagnosis"]))
    out = out.replace("{{IMPACT}}", p["impact"])
    out = out.replace("{{COST_1}}", p["costs"][0])
    out = out.replace("{{COST_2}}", p["costs"][1])
    out = out.replace("{{COST_3}}", p["costs"][2])
    out = out.replace("{{COST_CLOSE}}", p["cost_close"])
    out = out.replace("{{CTA_TEXT}}", p["cta"])
    out = out.replace("{{CTA_SHORT}}", p["cta_short"])
    out = out.replace("{{CHECKOUT_URL}}", CHECKOUT + "&sck=" + p["key"] + "_v2")
    out = out.replace("__PHOTO__", PHOTO)

    left = re.findall(r"\{\{[A-Z_0-9]+\}\}|__PHOTO__", out)
    assert not left, (p["key"], set(left))
    pathlib.Path(SC + p["file"]).write_text(out)
    print("OK", p["file"], "|", len(out) // 1024, "KB")

print("\n4 paginas de resultado 2.0 geradas.")
