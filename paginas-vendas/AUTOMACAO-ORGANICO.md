# Automação do Orgânico — Instagram + Facebook (18/07/2026)

Sistema de resposta automática para comentários (feed/Reels), stories e DM,
via ManyChat (canal Instagram + Facebook Messenger — API oficial da Meta,
sem risco de bloqueio).

**Já existe (auditoria 12/07):** RM10A comentário · RM10B story · RM10C DM
"RESET". Este documento completa o sistema: RM10D a RM10G.

## Princípio: responder sempre, mas parecer humano

Responder TODO comentário com a MESMA frase mata o engajamento — o público
percebe o robô em 3 posts e para de comentar. A regra aqui:

1. **Todo comentário recebe resposta** (bom para o algoritmo e para quem
   comentou), mas a resposta pública vem de um **banco rotativo** — o
   ManyChat sorteia entre várias frases curtas.
2. **DM automática com link só para quem pediu** (comentou a palavra-chave
   ou respondeu story). Mandar link na DM de quem só elogiou = spam.
3. **Toda DM recebida tem resposta em segundos**, mesmo fora do horário —
   com menu que direciona para o funil certo.

---

## MAPA DOS FLUXOS

| Fluxo | Canal | Gatilho | Ação |
|---|---|---|---|
| RM10A (existe) | IG | comentário c/ palavra-chave "RESET" | resposta pública + DM com link do quiz |
| RM10B (existe) | IG | resposta/menção em story | DM de agradecimento + pergunta |
| RM10C (existe) | IG | DM com "RESET" | link do quiz |
| **RM10D** novo | IG + FB | **qualquer DM sem palavra-chave** | menu de boas-vindas (abaixo) |
| **RM10E** novo | IG | **qualquer comentário sem palavra-chave** | resposta pública rotativa (banco abaixo), SEM DM |
| **RM10F** novo | IG + FB | comentário/DM com "CURSO" | resposta + DM com link da página do curso |
| **RM10G** novo | FB | comentário em post da página | espelho do RM10A/E no Facebook |

---

## RM10D — Resposta padrão de DM (o "recepcionista 24h")

Gatilho: qualquer mensagem recebida que não casou com palavra-chave.
Configurar no ManyChat como **Default Reply** (IG e Messenger).

> Fala, guerreiro! 👊 Aqui é o assistente do Leandro Cunha / Reset
> Masculino. Me diz o que você procura:
>
> 🔎 **1** — Descobrir em que estágio do automático eu estou (diagnóstico
> gratuito de 3 minutos)
> 🔥 **2** — Conhecer o curso Reset Masculino
> 🎓 **3** — Já sou aluno / preciso de suporte
>
> Responde com o número (ou me conta com suas palavras).

Botões/respostas:
- **1** → "Boa decisão. São 12 perguntas honestas — responde sem pensar
  demais: https://leandrocunhaofc.com.br/diagnostico.html"
- **2** → "O protocolo completo para sair do automático está aqui (condição
  de lançamento ativa): https://leandrocunhaofc.com.br/curso-reset-masculino/"
- **3** → "Fechado. Me diz rapidinho qual é a dúvida (acesso, grupo,
  pagamento) que a equipe te responde por aqui." + tag `suporte_pendente`
  (notificação para a equipe).

## RM10E — Resposta pública rotativa (todo comentário)

Configurar: Comment Automation → todos os posts → responder públicamente
com UMA frase sorteada do banco. **Sem DM automática** (DM só via RM10A/F).

Banco de respostas públicas (o ManyChat rotaciona):

1. Boa, guerreiro! 👊
2. É disso que eu tô falando. 🔥
3. Tamo junto nessa caminhada. 👊
4. Palavra de homem que acordou. 🔥
5. Segue firme. O automático não te pega mais. 👊
6. Respeito. É um passo de cada vez. 💪
7. Isso aí. Pequenas ações, grande reconstrução. 🔥
8. Valeu por dividir isso aqui, irmão. 👊

*(Trocar/renovar o banco a cada mês para não repetir demais. Comentários
com pergunta real caem para a equipe responder — ver "governança" abaixo.)*

## RM10F — Palavra-chave CURSO

Espelho do RM10A, mas para o produto de R$97:
- Comentário "CURSO" → resposta pública: "Te chamei na DM, guerreiro 👊" +
  DM: "Aqui está o que você pediu: o protocolo para sair do automático —
  https://leandrocunhaofc.com.br/curso-reset-masculino/ (de R$297 por R$97
  no lançamento). Qualquer dúvida, me responde aqui."
- Nos criativos/legendas: CTA "comenta CURSO que eu te mando o link".

## RM10B — Story (ajuste no existente)

- **Resposta a story** → DM: "Valeu por responder, guerreiro 👊 Já fez o
  diagnóstico do automático? 3 minutos e você descobre seu estágio.
  Quer o link?" (sim → link).
- **Menção em story** → DM: "Tamo junto! 🔥 Obrigado por compartilhar o
  Reset. Se algum irmão te perguntar, manda ele comentar RESET em qualquer
  post que o link chega automático."

## RM10G — Facebook (espelho)

A página do Facebook usa os mesmos fluxos via Messenger:
- Default Reply = RM10D (mesmo texto).
- Comment automation nos posts da página = RM10E + palavras-chave
  RESET/CURSO.
*(No ManyChat, conectar o canal Facebook Messenger além do Instagram.)*

---

## Governança (para o robô não virar problema)

- **Pergunta real no comentário** ("quanto custa?", "funciona pra quem tem
  depressão?"): o robô responde a rotativa pública normalmente, mas a
  EQUIPE varre os comentários 1x/dia para responder as perguntas de
  verdade. Robô dá presença; humano dá profundidade.
- **Tag `suporte_pendente`**: revisar 2x/dia (manhã/fim de tarde). DM de
  aluno com problema não pode esperar 24h.
- **Críticas/haters**: NUNCA responder no automático além da rotativa.
  Decisão humana: responder com altura, ocultar ou ignorar.
- **Métrica mensal**: quantos entraram no quiz vindos de RESET (comentário
  vs story vs DM) — o Airtable já registra origem; usar para decidir qual
  CTA repetir nos criativos.

## Checklist de implantação

- [ ] Conferir RM10A/B/C: apontam para /diagnostico.html (não para o Tally
      antigo)?
- [ ] Criar RM10D (Default Reply) no IG e no Messenger.
- [ ] Ativar RM10E (comment automation todos os posts + banco rotativo).
- [ ] Criar RM10F (palavra-chave CURSO) — e passar a usar "comenta CURSO"
      nos conteúdos sobre o curso.
- [ ] Conectar canal Facebook Messenger no ManyChat (RM10G).
- [ ] Definir quem varre comentários 1x/dia e `suporte_pendente` 2x/dia.
