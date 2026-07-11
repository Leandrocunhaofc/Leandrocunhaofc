# Funil Reset Masculino — Diagnóstico + Páginas de Vendas

Documento de referência do funil completo do e-book **7 Verdades**.

## Visão geral do funil

```
Anúncio (Meta)
   ↓
Diagnóstico (quiz)  ← diagnostico.html  (Pixel: PageView, QuizStart, Lead)
   ↓  (12 perguntas → calcula perfil por pontuação)
Página de resultado do perfil  ← reset-1..4  (Pixel: PageView, InitiateCheckout)
   ↓  botão "Quero iniciar meu Reset"
Checkout Hotmart  (C106036012S, com sck do perfil)
   ↓
Venda
```

Em paralelo (captura de lead), replicando o que o Tally fazia:

```
Diagnóstico → Webhook (Make) → Airtable "Leads Diagnóstico"
           → RM03 (Watch) → ManyChat → RM04..RM08
```

## Perfis e pontuação

Cada resposta vale 0–3 (Quase nunca → Quase sempre). Soma de 0 a 36:

| Faixa | Perfil | Página |
|---|---|---|
| 0–9 | Homem Distraído | `reset-1-distraido.html` |
| 10–18 | Homem Apagado | `reset-2-apagado.html` |
| 19–27 | Homem em Guerra Interna | `reset-3-guerra-interna.html` |
| 28–36 | Homem no Limite do Automático | `reset-4-limite.html` |

## Checkout Hotmart (já embutido nas 4 páginas)

`https://pay.hotmart.com/C106036012S?checkoutMode=10&sck=<perfil>`

O `sck` muda por página (`distraido`, `apagado`, `guerra`, `limite`) para
rastrear no relatório da Hotmart qual perfil mais converte.

## Meta Pixel (já embutido)

ID `1307273057695610`. Eventos:
- Quiz: `PageView`, `QuizStart`, `Lead`, `QuizComplete`.
- Páginas de resultado: `PageView`, `InitiateCheckout` (no clique do botão).

## Migração do Tally → Diagnóstico próprio (via Make)

O Tally hoje escreve direto no Airtable (cenário "RM01 - Tally Diagnóstico
para Airtable"). Como o quiz é uma página estática, ele não pode escrever
direto no Airtable com segurança — por isso usamos o **Make como ponte**.

### Novo cenário no Make (substitui o RM01)
1. **Webhooks → Custom webhook** (ex.: `RM01b - Quiz Diagnóstico`). Copie a URL.
2. Cole a URL no `LEAD_WEBHOOK` do `diagnostico.html`.
3. **Airtable → Create a Record** → base **Reset Masculino** → tabela **Leads Diagnóstico**.
4. Mapeie os campos:

| Campo do quiz (webhook) | Coluna no Airtable |
|---|---|
| `score` | Score do diagnóstico |
| `nome` | Nome |
| `email` | Email |
| `whatsapp` | WhatsApp |
| `consentimento` | Consentimento WhatsApp? |
| `utm_source` | UTM Source |
| `utm_medium` | Meio UTM |
| `utm_campaign` | UTM Campaign |
| `utm_content` | UTM Content |

Campos extras enviados pelo quiz (opcionais): `idade`, `estado_civil`, `perfil`, `respostas`.

O RM03 (Watch Records) detecta o novo registro e segue o fluxo normal
(ManyChat, RM04..RM08). Nada mais muda.

## Checklist para publicar

- [ ] Publicar `diagnostico.html` numa página do WordPress (ex.: `/diagnostico`).
- [ ] Publicar as 4 páginas de resultado (ex.: `/resultado-distraido` etc.).
- [ ] No `diagnostico.html`, trocar as 4 `RESULT_URLS` pelas URLs reais do WordPress.
- [ ] Criar o webhook no Make e colar em `LEAD_WEBHOOK`.
- [ ] Testar ponta a ponta e conferir Airtable, ManyChat, Pixel e Hotmart.
- [ ] Desligar o Tally (ou manter como backup).
