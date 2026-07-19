# RM03 — Leads Diagnóstico para ManyChat

**Projeto:** RESET MASCULINO_2  
**Atualização:** 18/07/2026  
**Status:** teste de contato existente aprovado; teste de contato novo ainda pendente; cenário desligado

## Problema identificado

O módulo `ManyChat — Create Subscriber` falhava quando o WhatsApp já existia no ManyChat, retornando:

> This WhatsApp ID already exists

O Make repetiu o mesmo registro e desativou automaticamente o cenário. O contato existente foi localizado no ManyChat e o Subscriber ID confirmado foi `1122441770`, associado ao WhatsApp normalizado `5521976372196`.

Também foi identificado que o diagnóstico próprio envia o telefone como DDD + número, por exemplo `21976372196`, enquanto o ManyChat armazena o telefone com DDI, por exemplo `5521976372196`.

## Campo personalizado criado no ManyChat

- Nome: `RM - WA ID Lookup`
- Tipo: Texto
- Finalidade: localizar contatos já existentes pelo telefone normalizado.

## Normalização definitiva do telefone

Nos módulos abaixo, o valor passou a ser montado visualmente no Make como:

```text
55 + token Airtable 2 → WA ID
```

Exemplo:

```text
21976372196 → 5521976372196
```

A fórmula textual digitada anteriormente não foi interpretada pelo Make e foi removida.

A normalização foi aplicada em:

1. `ManyChat 10 — Create Subscriber` → `WhatsApp phone number`;
2. `ManyChat 22 — Set a Custom Field` → `Field value`;
3. `ManyChat 24 — Find Subscribers by a Custom Field` → `Field value`.

O campo `Phone number` permanece vazio no `Create Subscriber`, evitando exigência indevida de SMS opt-in.

## Arquitetura atual do RM03

### Rota principal — contato novo

```text
Airtable 2 — Watch Records
→ Router 16
→ ManyChat 10 — Create Subscriber
→ ManyChat 22 — Set a Custom Field
→ Airtable 12 — Update a Record
```

Configurações principais:

- `Create Subscriber`:
  - First name: `Airtable 2 → Nome`;
  - Phone number: vazio;
  - WhatsApp phone number: `55` + `Airtable 2 → WA ID`.

- `Set a Custom Field`:
  - Subscriber ID: `ManyChat 10 → ID`;
  - Field ID: `RM - WA ID Lookup`;
  - Field value: `55` + `Airtable 2 → WA ID`.

- `Airtable 12 — Update a Record`:
  - Record ID: `Airtable 2 → ID`;
  - Manychat Subscriber ID: `ManyChat 10 → ID`;
  - Enviado Manychat?: `Yes`.

### Rota de erro — contato já existente

```text
ManyChat 10 — Create Subscriber gera duplicidade
→ ManyChat 24 — Find Subscribers by a Custom Field
→ Airtable 25 — Update a Record
→ Skip 26
```

Configurações principais:

- `ManyChat 24 — Find Subscribers by a Custom Field`:
  - Field ID: `RM - WA ID Lookup`;
  - Field value: `55` + `Airtable 2 → WA ID`;
  - Limit: `1`.

- `Airtable 25 — Update a Record`:
  - Record ID: `Airtable 2 → ID`;
  - Manychat Subscriber ID: primeiro `ID` retornado pelo `ManyChat 24`;
  - Enviado Manychat?: `Yes`.

- `Skip 26` encerra o bundle duplicado sem derrubar ou desativar o cenário.

### Rota antiga de contingência

```text
ManyChat 20 — Find Subscribers by a Custom Field
→ Airtable 21 — Update a Record
```

Essa rota foi preservada e permanece bloqueada temporariamente. Não apagar antes da validação completa do RM03.

## Limpeza da fila antiga

Os registros claramente fictícios foram removidos do Airtable. Os registros reais pendentes foram processados individualmente.

Para o contato de teste principal:

```text
WhatsApp normalizado = 5521976372196
Manychat Subscriber ID = 1122441770
Enviado Manychat? = true
```

## Teste A — contato já existente

**Status: APROVADO em 18/07/2026.**

Procedimento executado:

1. novo diagnóstico usando o telefone já existente;
2. Airtable recebeu o WA ID sem DDI;
3. `Create Subscriber` identificou duplicidade;
4. `ManyChat 24` pesquisou o valor normalizado `5521976372196`;
5. `ManyChat 24` retornou:

```text
ID = 1122441770
whatsapp_phone = +5521976372196
Total number of bundles = 1
```

6. `Airtable 25` gravou:

```text
Manychat Subscriber ID = 1122441770
Enviado Manychat? = true
```

7. execução encerrada com sucesso pela rota de erro e `Skip 26`.

## Teste B — contato realmente novo

**Status: PENDENTE.**

Objetivo:

- usar um número real que ainda não exista no ManyChat;
- confirmar criação automática do contato;
- confirmar preenchimento de `RM - WA ID Lookup`;
- confirmar gravação do novo Subscriber ID no Airtable;
- confirmar `Enviado Manychat? = true`;
- confirmar que a rota de erro não é acionada.

## Critério para ativação

O RM03 só poderá ser ativado após o Teste B concluir sem erro. Depois da aprovação:

1. manter a rota principal liberada;
2. manter a rota de erro ativa;
3. manter a rota antiga bloqueada até decisão de arquivamento;
4. ativar o agendamento `Every 15 minutes`;
5. executar o teste completo do diagnóstico até a recuperação correta conforme o perfil.
