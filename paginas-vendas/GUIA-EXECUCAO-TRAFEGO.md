# Guia de Execução — Gravação, Pixels e Campanha (detalhado)

## PARTE A — Os 4 criativos: o que é cada um

| Criativo | Tipo | Quem produz |
|---|---|---|
| Ângulo 1 — Identificação | VÍDEO (você falando) | Você grava |
| Ângulo 2 — Curiosidade | IMAGEM (pronta: `anuncio-angulo2-feed.png`) | ✅ já feita |
| Ângulo 3 — Autoridade | VÍDEO (você falando) | Você grava |
| Ângulo 4 — Confronto | VÍDEO (você falando) | Você grava |

### Como gravar os 3 vídeos (setup único, 1 tarde)

**Equipamento:** só o celular. Nada mais.
1. **Formato:** vertical (9:16), gravando pela câmera TRASEIRA (melhor qualidade).
2. **Luz:** de frente pra uma janela (luz no seu rosto, nunca atrás de você).
3. **Fundo:** neutro e limpo (parede escura, escritório organizado). Roupa escura/lisa.
4. **Enquadramento:** do peito pra cima, olhos na linha do terço superior da tela,
   olhando PARA A LENTE (não para a tela).
5. **Áudio:** ambiente silencioso. Se tiver fone com microfone, use.
6. **Ritmo:** fale como quem conversa com UM homem, não como palestra.
   Frases curtas. Pausa seca entre frases. Sem "oi pessoal" — começa direto no hook.
7. Grave cada roteiro **3 vezes** e escolha a melhor tomada.

### Roteiros palavra por palavra

**ÂNGULO 1 (20–30s):**
> "Você acorda, trabalha, provê, resolve... e por dentro, tá vazio?
> Isso tem nome: modo automático.
> Não é falta de esforço. É desconexão.
> Eu criei um diagnóstico gratuito de 2 minutos que mostra em que estágio
> do automático você está — e o que fazer pra sair.
> Toca no botão aí embaixo e descobre."

**ÂNGULO 3 (30–45s):**
> "Depois de 20 anos e mais de 10 mil homens impactados, eu aprendi uma coisa:
> o homem não quebra de uma vez. Ele se apaga aos poucos.
> Primeiro perde a presença. Depois a disciplina. Depois a fé. E um dia ele
> olha no espelho e não reconhece quem tá ali.
> Por isso eu criei o Reset Masculino.
> O primeiro passo é um diagnóstico gratuito de 2 minutos.
> Toca no botão e descobre em que estágio você está."

**ÂNGULO 4 (15–20s):**
> "Isso que você chama de cansaço... não é cansaço.
> É desconexão. Da sua mente. Da sua fé. Do seu propósito.
> E desconexão não se resolve aguentando mais um pouco.
> Diagnóstico gratuito, 2 minutos. Toca no botão."

Depois de gravar: legendas automáticas (CapCut gratuito → "Legendas automáticas"
→ fonte branca com contorno). Legendas aumentam MUITO a retenção.

---

## PARTE B — Alinhamento dos Pixels (site + Hotmart + Meta)

O objetivo: o Meta "enxergar" a jornada completa:
PageView → QuizStart → Lead → InitiateCheckout → **Purchase**.

### B1. Sites (JÁ FEITO ✅ — só entender)
O Pixel `1307273057695610` já está embutido por mim em:
- `/diagnostico.html` → dispara PageView, QuizStart, **Lead** (quiz completo)
- 4 páginas de resultado → PageView e **InitiateCheckout** (clique no botão)
Você não precisa fazer nada nos sites.

### B2. ⚠️ Plugin "Meta Pixel for WordPress" — NÃO CONFIGURAR
No seu painel do WordPress aparece o aviso "Meta Pixel for WordPress is almost
ready...". **NÃO complete essa configuração** (ou desative o plugin em Plugins).
Motivo: nossas páginas já têm o Pixel embutido — o plugin dispararia PageView
DUPLICADO nas mesmas páginas e sujaria os dados da campanha.

### B3. Hotmart → Meta (o Purchase — ESSA É A SUA TAREFA)
1. Entre na **Hotmart** → produto **eBook 7 Verdades**.
2. Menu **Ferramentas** → **Pixel de rastreamento** (ou "Rastreamento").
3. Escolha **Meta/Facebook Pixel** → **Adicionar**.
4. Cole o ID: `1307273057695610`.
5. Marque os eventos de **compra aprovada (Purchase)** — e, se oferecido,
   ative também para **página de checkout (InitiateCheckout)**.
6. Salvar. **Repita para os produtos Áudio e Reset Online** (cada produto tem
   sua própria configuração de pixel).

### B4. Conferir no Meta (Gerenciador de Eventos)
1. **business.facebook.com** → menu ☰ → **Gerenciador de Eventos**.
2. Selecione o pixel `1307273057695610`.
3. Aba **"Testar eventos"** → abra `leandrocunhaofc.com.br/diagnostico.html`
   no celular e faça o quiz → os eventos devem aparecer na tela em tempo real:
   `PageView` → `QuizStart` → `Lead`.
4. Clique no botão de compra numa página de resultado → deve aparecer
   `InitiateCheckout`.
5. Faça a compra-teste com cupom → em até alguns minutos deve aparecer
   **Purchase** (vindo da Hotmart).
6. (Recomendado) **Configurações do Business → Segurança da marca → Domínios**
   → adicionar e verificar `leandrocunhaofc.com.br`.

Se os 5 eventos aparecerem: pixels 100% alinhados. ✅

---

## PARTE C — Subir a campanha (clique a clique, iniciante)

1. **facebook.com/adsmanager** → botão verde **+ Criar**.
2. Objetivo: **Leads** → Continuar (modo manual, se perguntar).
3. **Nível Campanha:**
   - Nome: `RM • Diagnóstico • 01`
   - Orçamento da campanha (CBO / Advantage): **ATIVADO**, R$50/dia. Avançar.
4. **Nível Conjunto (1º):**
   - Nome: `Aberto • BR • H 28-55`
   - Local de conversão: **Site** · Pixel: `1307273057695610` · Evento: **Lead**
   - Público: Brasil · Homens · 28–55 · SEM interesses
   - Posicionamentos: **Advantage+ (automáticos)**. Avançar.
5. **Nível Anúncio (crie 4 dentro do conjunto):**
   - Identidade: sua Página do FB + seu Instagram.
   - Anúncio 1: vídeo Ângulo 1 · Anúncio 2: imagem Ângulo 2 ·
     Anúncio 3: vídeo Ângulo 3 · Anúncio 4: vídeo Ângulo 4.
   - **Texto principal** e **Título**: usar os da ESTRATEGIA-TRAFEGO.md.
   - **URL do site**: o link do diagnóstico COM UTM (trocar utm_content por anúncio):
     `https://leandrocunhaofc.com.br/diagnostico.html?utm_source=facebook&utm_medium=cpc&utm_campaign=diagnostico01&utm_content=angulo1`
   - Botão (CTA): **Saiba mais**.
6. **Duplicar o conjunto** (botão Duplicar) → renomear `Interesses • BR • H 28-55`
   → em Público, adicionar interesses: desenvolvimento pessoal, estoicismo,
   fé cristã, paternidade, empreendedorismo. Os 4 anúncios vêm juntos.
7. **Publicar** e aguardar aprovação (algumas horas).

### Leitura dos números (a cada 2–3 dias, me traga):
CPM · CTR (link) · Custo por Lead · Leads · Compras (Hotmart) · Valor gasto.
Metas iniciais: CTR ≥ 1% · Lead ≤ R$8 · Compra ≤ R$37.

---

## Links oficiais do funil (guardar)
- Quiz (anúncios/bio): `https://leandrocunhaofc.com.br/diagnostico.html`
- Resultados: `/resultado-distraido` · `/resultado-apagado` · `/resultado-guerra` · `/resultado-limite`
- Comunidade: `https://leandrocunhaofc.com.br/comunidade`
- Checkout: `https://pay.hotmart.com/C106036012S?checkoutMode=10`
- Pixel Meta: `1307273057695610`
