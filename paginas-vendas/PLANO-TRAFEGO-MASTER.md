# Plano Master de Aquisição — Meta Ads + Orgânico (20/07/2026)

Complementa `ESTRATEGIA-TRAFEGO.md` (criativos, Campanha 1 e calendário de
30 dias — continuam valendo). Este documento adiciona: auditoria ao vivo da
conta, arquitetura em 3 fases, públicos, remarketing, escala e o sistema de
validação do orgânico.

---

## ⚡ AUDITORIA AO VIVO DA CONTA (20/07, via API do Meta)

| Item | Status |
|---|---|
| Conta oficial "Novo Leandro Cunha" (1567614621462243) | ✅ ATIVA, moeda BRL, no portfólio Reset Masculino |
| Pixel/dataset 1307273057695610 | ✅ Vinculado ao portfólio, ATIVO |
| Disparo do pixel (navegador) | ✅ Último disparo HOJE |
| Disparo via servidor (Hotmart↔Meta) | ✅ Também HOJE — integração viva |
| **Forma de pagamento na conta oficial** | 🔴 **NÃO CADASTRADA — bloqueia tudo** |

**Ação imediata (5 min):** Gerenciador de Anúncios → conta 1567614621462243
→ Configurações de pagamento → cadastrar cartão. Sem isso, nenhuma campanha
roda. *(A conta 693264489602951 tem cartão, mas está fora do portfólio
oficial — não usar, para não construir histórico na conta errada.)*

---

## ARQUITETURA EM 3 FASES

### FASE 1 — VALIDAÇÃO (semanas 1–2) · R$50/dia
Campanha 1 "RM • Diagnóstico" exatamente como está em
`ESTRATEGIA-TRAFEGO.md`: objetivo Leads, CBO R$50/dia, 2 conjuntos
(Aberto + Interesses), 4 ângulos em cada. Regras de corte após ~R$150/conjunto.

**Saída esperada da fase:** 2 ângulos vencedores · CPL ≤ R$8 ·
primeiras vendas com custo ≤ R$37 (breakeven no ebook; lucro vem de
bump + upsell + curso R$97).

### FASE 2 — OTIMIZAÇÃO (semanas 3–4) · R$65–80/dia

**2a. Criar os públicos personalizados (fazer JÁ, eles populam sozinhos):**

| Público | Definição | Uso |
|---|---|---|
| ENV-IG-90 | Envolvidos com o Instagram, 90d | remarketing frio→quiz |
| ENV-FB-90 | Envolvidos com a Página FB, 90d | idem |
| SITE-30 | Visitantes do site, 30d | remarketing |
| QUIZ-VIU | Visitou /diagnostico.html, 14d, SEM evento Lead | "termina o diagnóstico" |
| LEAD-14 | Evento Lead 14d, SEM Purchase | "seu resultado te espera" |
| COMPRADORES | Evento Purchase, 180d | excluir das frias + base p/ lookalike e curso |
| CURSO-VIU | Visitou /curso-reset-masculino/, 14d, sem Purchase | remarketing curso |

**2b. Campanha 2 "RM • Remarketing" (R$15–20/dia, ABO):**
- Conjunto A (QUIZ-VIU): "Você começou e parou. 12 perguntas, 3 minutos —
  termina agora." → /diagnostico.html
- Conjunto B (LEAD-14): criativo de depoimento (Marcus/Julio/Roberto) +
  garantia 7 dias → página do resultado/oferta
- Conjunto C (COMPRADORES do ebook sem curso + CURSO-VIU): oferta do curso
  "de R$297 por R$97" → /curso-reset-masculino/?utm_campaign=rmk-curso
- Excluir COMPRADORES dos conjuntos A e B.

**2c. Migrar a Campanha 1 de Lead → Purchase** quando o pixel registrar
~50 compras em 30 dias (a Meta passa a caçar compradores, não curiosos).

### FASE 3 — ESCALA (mês 2+) · teto definido pelo CPA

- **Vertical:** +20% de orçamento a cada 2 dias na campanha vencedora
  (nunca dobrar de uma vez — reseta o aprendizado).
- **Horizontal:** novos conjuntos com **Lookalike 1% de COMPRADORES**
  (precisa ≥100 compras; antes disso, Lookalike 1–3% de Leads) e
  Lookalike de ENV-IG-90.
- **Criativos:** 2 novos por semana, sempre desafiando o campeão. Fontes:
  post orgânico que performou (ver loop abaixo), depoimento novo do
  Reset on Fire, corte de palestra.
- **Regra de ouro da escala:** enquanto CPA de venda ≤ R$37, tem espaço
  para subir orçamento. Passou disso por 3 dias seguidos → volta um nível
  e troca criativo.

---

## KPIs E ROTINA DE GESTÃO

| Métrica | Alvo | Alarme |
|---|---|---|
| CTR (link) | ≥ 1% | < 0,8% troca hook |
| CPL (Lead = quiz completo) | ≤ R$8 | > R$12 pausa conjunto |
| Custo por venda (front R$37) | ≤ R$37 | > R$50 por 3 dias → revisar |
| Conversão quiz→checkout | acompanhar no Airtable | queda súbita = problema técnico |

**Rotina:** 10 min/dia (gasto, CPL, CPA, comentários nos anúncios — a
automação RM10E responde, mas ler o que o público diz é pesquisa grátis) ·
decisão de criativos a cada 3 dias · revisão semanal com números ·
renovação mensal de criativos e bancos de mensagens.

---

## ORGÂNICO — projeto de validação (30 dias)

Calendário e pilares: seguir `ESTRATEGIA-TRAFEGO.md` Parte 3 (pilares
seg–dom + 4 semanas temáticas). O que este plano adiciona:

**1. O orgânico é o laboratório do pago.** Todo Reel é um teste de hook
grátis. Métrica de decisão: retenção + comentários "RESET". O post que
performar acima da média na semana **vira anúncio na segunda seguinte**
(sobe como criativo novo na Campanha 1). Loop: orgânico testa → pago
escala → engajado vira público (ENV-IG-90) → remarketing converte.

**2. Métricas semanais do orgânico (planilha simples ou Airtable):**
- Alcance e contas alcançadas não-seguidoras (%)
- Comentários RESET/CURSO → DMs disparadas (ManyChat mostra)
- Cliques no link da bio → leads do quiz com utm_source=instagram
- Vendas com sck/utm de origem orgânica

**3. Critério de validação (fim dos 30 dias):** o orgânico está validado
quando ≥30% dos leads do quiz vierem de origem orgânica (bio + RESET) e
pelo menos 1 venda/semana for atribuída ao orgânico. Validado → mantém
a cadência e reinveste o tempo ganho das automações em 1 conteúdo a mais
por semana.

---

## ORDEM DE EXECUÇÃO (atualizada)

1. 🔴 Cadastrar forma de pagamento na conta 1567614621462243 (bloqueio).
2. Verificar domínio leandrocunhaofc.com.br no Business Manager (se ainda
   não estiver).
3. Criar os 7 públicos personalizados (tabela 2a).
4. Gravar/preparar os 4 criativos (roteiros na ESTRATEGIA-TRAFEGO) +
   aproveitar as artes prontas guardadas.
5. Subir Campanha 1 (Fase 1) — posso montar a estrutura direto na conta
   via API e deixar em rascunho/pausada para o Leandro revisar e ativar.
6. Iniciar Semana 1 do calendário orgânico no mesmo dia do primeiro anúncio.
7. Revisão a cada 3 dias com os números; Fase 2 entra na semana 3.
