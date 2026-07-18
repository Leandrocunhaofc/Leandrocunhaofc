# Automação de Mensagens — ManyChat/WhatsApp (18/07/2026)

Mapa completo dos fluxos automáticos + TODAS as mensagens prontas para colar.
Objetivo: nenhum aluno ou lead ficar sem resposta por depender de alguém
lembrar de mandar mensagem.

## Regra de ouro do WhatsApp (janela de 24h)

- **Até 24h** depois da última mensagem DO CLIENTE: pode enviar texto livre.
- **Depois de 24h**: só chega mensagem que for um **TEMPLATE APROVADO pela
  Meta** (cadastrado no ManyChat → Settings → WhatsApp → Message Templates).
- Neste documento, cada mensagem está marcada: `[LIVRE]` ou `[TEMPLATE]`.
- Template usa variáveis numeradas `{{1}}` (nome) — o texto já está no
  formato de aprovação: tom neutro, sem "COMPRE AGORA", sem excesso de
  emoji/caixa alta (a Meta reprova template com cara de spam).

## O que NÃO dá para automatizar (e a solução)

Postar **dentro do grupo** Reset on Fire: a API oficial do WhatsApp não
envia mensagem para grupos — isso é limite da Meta, não do ManyChat.
**Solução:** banco de posts prontos no fim deste documento (4 semanas).
Vira tarefa de 2 minutos: copiar, colar, enviar. Todo o resto (1-para-1
com lead e aluno) é 100% automático.

---

## MAPA DOS FLUXOS

| Fluxo | Gatilho | Quando | Mensagem | Tipo |
|---|---|---|---|---|
| RM11 Boas-vindas Curso | tag `comprou_curso` | +15 min | M1 | LIVRE* |
| RM06B Roteador pós-ebook | tag `comprou_ebook` | +1h | M2/M3/M4 | LIVRE* |
| RM12 Check-in Dia 3 | 3 dias após `comprou_curso` | 10h | M5 | TEMPLATE |
| RM13 Check-in Dia 7 | 7 dias após `comprou_curso` | 10h | M6 | TEMPLATE |
| RM14 Pede depoimento Dia 14 | 14 dias após `comprou_curso` | 10h | M7 | TEMPLATE |
| RM02/07/08/09 Recuperação lead | quiz sem compra | dia seguinte+ | M8 | TEMPLATE |

\* LIVRE se o cliente interagiu nas últimas 24h (acabou de comprar vindo do
fluxo, normalmente sim). Para garantir entrega sempre, cadastre M1 também
como template — custa nada e elimina o risco.

---

## FLUXO RM11 — Boas-vindas Curso (cobre upsell E compra direta)

Gatilho: tag `comprou_curso` aplicada (Make RM05C) → esperar 15 min → M1.

**M1 — Boas-vindas + comunidade** `[LIVRE + cadastrar como TEMPLATE]`

> Parabéns pela decisão, {{1}}. 👊
>
> Você acaba de entrar no Reset Masculino — e a partir de agora você não
> caminha mais sozinho.
>
> ✅ Seu acesso já está no seu e-mail (área de membros da Hotmart). Se não
> encontrar, olhe o spam ou me responda aqui.
>
> 🔥 Seu lugar na comunidade Reset on Fire está reservado:
> https://leandrocunhaofc.com.br/comunidade
>
> Chega lá, leia a mensagem fixada e se apresente. O Reset começa hoje.

## FLUXO RM06B — Roteador pós-compra do ebook

Gatilho: tag `comprou_ebook` → esperar 1h → condições em ordem:

1. TEM `comprou_curso` → **M2** (não oferece nada; RM11 já convidou p/ grupo)
2. senão, TEM `comprou_audio` → **M3** (oferta do curso)
3. senão → **M4** (oferta áudio + curso)

**M2 — Comprou tudo** `[LIVRE]`

> {{1}}, você fez o movimento completo: eBook + Reset Masculino. 👊
> Poucos homens decidem tão rápido — isso já diz muito sobre você.
> Seus acessos estão no e-mail, e o grupo te espera (te mandei o link).
> Primeira missão: assistir ao Módulo 1 ainda hoje. Topa?

**M3 — Ebook + áudio, sem curso** `[LIVRE]`

> {{1}}, seu eBook e seu áudio já estão no seu e-mail. 👊
>
> Antes de você começar a leitura, uma coisa que preciso te falar: o eBook
> abre os olhos — mas quem quer RECONSTRUIR na prática usa ele junto com o
> Reset Masculino: 11 módulos em vídeo, apostilas com exercícios, missões
> diárias e a comunidade Reset on Fire.
>
> Por ser aluno, sua condição de lançamento continua valendo: de R$297 por
> R$97 → https://leandrocunhaofc.com.br/curso-reset-masculino/
>
> Qualquer dúvida, me chama aqui.

**M4 — Só ebook** `[LIVRE]`

> {{1}}, seu eBook "7 Verdades" já está no seu e-mail. 👊
>
> Lê com calma — mas lê de verdade. E quando chegar na 7ª verdade, você vai
> entender por que ler sozinho não basta: é aí que entra o Reset Masculino,
> o protocolo prático de 11 módulos para sair do automático (com a
> comunidade Reset on Fire junto).
>
> Condição de lançamento: de R$297 por R$97 →
> https://leandrocunhaofc.com.br/curso-reset-masculino/
>
> Qualquer dúvida sobre o eBook ou o curso, me responde aqui.

## FLUXO RM12 — Check-in Dia 3 (retenção na garantia)

Gatilho: 3 dias após `comprou_curso`, às 10h → M5.

**M5** `[TEMPLATE — cadastrar na Meta]`

> Olá {{1}}, aqui é do Reset Masculino. Passando para saber: você já
> conseguiu assistir ao primeiro módulo e entrar na comunidade? Se travou
> em alguma coisa (acesso, e-mail, grupo), me responde esta mensagem que
> eu te ajudo a resolver hoje.

## FLUXO RM13 — Check-in Dia 7 (fim da janela de garantia)

Gatilho: 7 dias após `comprou_curso`, às 10h → M6.

**M6** `[TEMPLATE]`

> {{1}}, uma semana de Reset Masculino. É normalmente aqui que separa quem
> muda de quem volta ao automático. Me responde com uma palavra: como você
> está — AVANÇANDO, TRAVADO ou PARADO? Sua resposta me ajuda a te apontar
> o próximo passo certo.

*(Resposta abre a janela de 24h → equipe ou fluxo responde livre.)*

## FLUXO RM14 — Depoimento Dia 14 (fábrica de prova social)

Gatilho: 14 dias após `comprou_curso`, às 10h → M7.

**M7** `[TEMPLATE]`

> {{1}}, duas semanas atrás você decidiu sair do automático. Me conta em
> 2-3 frases: o que já mudou na sua rotina ou na sua mente desde então?
> Sua resposta pode ajudar outro homem que está hoje onde você estava —
> e os melhores relatos ganham destaque na comunidade.

*(Depoimentos que chegarem → pasta/Airtable → alimentam página e anúncios.)*

## FLUXOS RM02/07/08/09 — Recuperação de lead (quiz sem compra)

Já existem no ManyChat, mas (auditoria de 12/07) disparam texto livre após
24h = **não entregam**. Cadastrar como template, 1 por perfil, exemplo:

**M8 — base (adaptar 1 linha por perfil)** `[TEMPLATE]`

> Olá {{1}}. Ontem você fez o Diagnóstico do Homem no Automático e seu
> resultado foi: {{2}}. O material que destrava exatamente esse perfil
> está aqui: {{3}}. Se tiver qualquer dúvida, é só responder esta mensagem.

Variáveis: {{1}} nome · {{2}} perfil ("Homem Distraído"...) · {{3}} link da
página do perfil. Um template só serve os 4 fluxos.

---

## BANCO DE POSTS DO GRUPO (4 semanas — copiar e colar)

### Semana 1
- **SEG 🎯 Missão:** "Missão da semana: escolha UMA coisa que você vem
  adiando há mais de 30 dias e resolva até sexta. Não a maior — a que mais
  pesa na mente. Escreve ela aqui embaixo. Compromisso dito é compromisso
  cobrado. 👊"
- **QUA 🧠 Provocação:** "O automático não chega de uma vez. Ele chega de
  adiadinho em adiadinho. Qual foi o 'depois eu faço' de hoje que você vai
  fazer AGORA?"
- **SEX ✅ Check-in:** "Sexta é dia de prestar conta: quem resolveu a
  missão da semana? Quem travou, fala onde travou — aqui ninguém quebra em
  silêncio."

### Semana 2
- **SEG 🎯 Missão:** "Semana da mente: todo dia, antes de pegar o celular
  de manhã, 5 minutos de silêncio — sem tela, sem ruído. Só você e o dia
  que vem. Quem topa, responde EU."
- **QUA 🧠 Provocação:** "Disciplina não é fazer o que você gosta. É fazer
  o que você DECIDIU, principalmente no dia em que não está com vontade.
  Hoje é esse dia pra alguém aqui?"
- **SEX ✅ Check-in:** "Quantos dias de 5 minutos você fez? 0 a 5 — número
  aqui embaixo, sem vergonha. Número baixo com honestidade vale mais que
  silêncio."

### Semana 3
- **SEG 🎯 Missão:** "Missão: uma conversa que você vem evitando (esposa,
  filho, pai, sócio). Marca ela pra esta semana. Não precisa contar o tema
  — só confirma aqui: MARQUEI."
- **QUA 🧠 Provocação:** "Homem no automático provê a casa e some da casa.
  Presente de corpo, ausente de alma. Hoje, 30 minutos INTEIROS com quem
  importa — sem celular na mão."
- **SEX ✅ Check-in:** "A conversa aconteceu? Como foi? Uma frase basta.
  Quem não conseguiu, remarca agora e fala o dia."

### Semana 4
- **SEG 🎯 Missão:** "Semana de fechar ciclo: olhe as 3 últimas missões.
  Qual você deixou pela metade? É ela que você termina até sexta."
- **QUA 🧠 Provocação:** "Um mês atrás você decidiu sair do automático.
  Responde com sinceridade: o homem de hoje faria de novo a escolha que o
  de 30 dias atrás fez? Por quê?"
- **SEX ✅ Check-in:** "Fim do primeiro ciclo. Escreve UMA coisa que mudou
  em você nesses dias — pode ser pequena. É dela que nasce a próxima."

---

## Checklist de implantação

- [ ] Make: confirmar que RM05C aplica `comprou_curso` na compra direta.
- [ ] ManyChat: criar RM11 (M1), RM06B (M2/M3/M4), RM12 (M5), RM13 (M6),
      RM14 (M7).
- [ ] Meta/ManyChat: submeter templates M1, M5, M6, M7, M8 para aprovação
      (leva de minutos a ~1 dia; fazer primeiro, é o gargalo).
- [ ] Refazer RM02/07/08/09 usando o template M8 aprovado.
- [ ] Compra de teste R$97: valida RM11 → grupo → (aguardar) RM12/13/14.
- [ ] Agendar lembrete fixo (seg/qua/sex, 2 min) para colar o post do banco.
