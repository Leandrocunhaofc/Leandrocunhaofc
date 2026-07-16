# Auditoria do Funil — Make + ManyChat (12/07/2026)

Raio-X completo feito a partir dos vídeos das telas do Make e do ManyChat,
antes de iniciar a campanha no Meta.

## Mapa real do funil

```
Anúncio / Instagram (RM10A-C)
   ↓
/diagnostico.html  (quiz, fora do WordPress)
   ↓ webhook
Make RM01b → Airtable "Leads Diagnóstico"
   ↓ (Watch Records)
Make RM03 → cria contato no ManyChat
   ↓
Make RM04A-D → etiqueta por perfil
   ↓ (etiqueta dispara)
ManyChat: RM02 (Distraído) · RM07 (Apagado) · RM08 (Guerra) · RM09 (Limite)
   = sequências de recuperação no WhatsApp

Compra na Hotmart
   ↓
Make RM05  → para a recuperação
Make RM05B → marca "Comprou Áudio" (order bump)
Make RM05C → marca "Comprou Curso" (upsell)
   ↓ (etiqueta)
ManyChat RM06 → Pós-compra e Onboarding
```

## Status na data da auditoria

### Make (cenários ON)
- RM01b Diagnóstico do Questionário ✅ (testado, 19 exec)
- RM03 Leads → ManyChat ✅ (335 exec)
- RM04A/B/C/D + RM04 Recuperação Ebook ✅
- RM05, RM05B, RM05C ✅

### ManyChat (AO VIVO)
- RM01 Entrada WhatsApp Diagnóstico (15 exec)
- RM02 Rec Distraído (3) · RM07 Rec Apagado (0) · RM08 Rec Guerra (0) · RM09 Rec Limite (0)
- RM06 Pós-compra e Onboarding (0)
- RM10A/B/C Instagram (comentário / story / DM "RESET")

## 🔴 Pendências encontradas

1. **Make: RM05C duplicado** — dois cenários com o mesmo nome, ambos ON.
   → Desligar o que tem 0 execuções (sem pasta).
2. **Make: "ARQUIVO — NÃO ATIVAR" (RM05B antigo e RM05C antigo) estão LIGADOS.**
   → Desligar os dois (risco de processar compra em duplicidade).
3. **Automações lembradas que NÃO EXISTEM (fase 2 — construir depois):**
   - Comprou eBook+bump sem upsell → oferta do curso Reset Online no WhatsApp.
   - Comprou tudo → convite para o grupo Reset on Fire.
4. **Nunca testados de verdade:** RM07/RM08/RM09 (0 exec) e RM06 (0 exec).
   → Validar com os 4 testes do quiz + 1 compra real de R$37.

## Checklist pré-tráfego

- [ ] Desligar RM05C duplicado + 2 "ARQUIVO — NÃO ATIVAR" no Make
- [ ] 4 testes do quiz (A/B/C/D) → página certa → Airtable → ManyChat → msg chega
- [ ] 1 compra real de teste → RM05 para recuperação → RM06 onboarding dispara
- [ ] Pixel disparando (Gerenciador de Eventos: PageView, Lead, InitiateCheckout)
- [ ] Apontar anúncio/bio para /diagnostico.html e desligar o Tally

---

# Projeto: Pós-compra e Retenção (14/07/2026)

## Status validado nesta data
- Quiz /diagnostico.html → 4 páginas → checkout Hotmart (com order bump): ✅ funcionando ponta a ponta.
- Causa raiz dos últimos erros: slugs errados em 2 páginas de resultado (corrigidos).

## A construir: RM06B — Roteador Pós-compra (ManyChat)
Gatilho: tag "comprou_ebook" → Delay 1h → Condições:
1. tem "comprou_curso" → Msg 3: parabéns completo + LINK GRUPO RESET ON FIRE
2. senão, tem "comprou_audio" → Msg 2: parabéns + oferta Curso Reset Online
3. senão → Msg 1: parabéns + oferta Áudio + Curso

As 3 mensagens (rascunho aprovável) estão no histórico do chat.

## Atenção — janela de 24h do WhatsApp
Mensagens após 24h da última interação exigem TEMPLATE aprovado (Meta).
- Roteador (delay 1h): dentro da janela, ok.
- Retenção RM02/07/08/09 (dias): PRECISAM usar templates aprovados, senão não entregam.

## Testes pendentes
- [ ] Compra só eBook → Msg 1 + recuperação para (RM05)
- [ ] Compra eBook+Áudio → Msg 2
- [ ] Compra tudo → Msg 3 + grupo
- [ ] Retenção: msgs programadas chegando após os testes do quiz
