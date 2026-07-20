# RM03 — Leads Diagnóstico para ManyChat

**Projeto:** RESET MASCULINO_2  
**Atualização:** 20/07/2026  
**Status:** operacional; rota de contato existente aprovada; criação de contato novo comprovada; recomenda-se apenas uma validação futura em execução única, sem bloquear o avanço da auditoria

## Problema identificado

O módulo `ManyChat — Create Subscriber` falhava quando o WhatsApp já existia no ManyChat, retornando:

> This WhatsApp ID already exists

O Make repetiu o mesmo registro e desativou automaticamente o cenário. Também foi identificado que o diagnóstico próprio envia o telefone como DDD + número, enquanto o ManyChat armazena o telefone com DDI `55`.

## Campo personalizado criado no ManyChat

- Nome: `RM - WA ID Lookup`
- Tipo: Texto
- Finalidade: localizar contatos existentes pelo telefone normalizado.

## Normalização definitiva do telefone

Nos módulos abaixo, o valor é montado visualmente no Make como:

```text
55 + token Airtable 2 → WA ID
```

Exemplo:

```text
21976372196 → 5521976372196
```

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

Configurações:

- `ManyChat 10 — Create Subscriber`:
  - First name: `Airtable 2 → Nome`;
  - Phone number: vazio;
  - WhatsApp phone number: `55` + `Airtable 2 → WA ID`.

- `ManyChat 22 — Set a Custom Field`:
  - Subscriber ID: primeiro `ID` retornado pelo `ManyChat 10`;
  - não usar `User ID`;
  - Field ID: `RM - WA ID Lookup`;
  - Field value: `55` + `Airtable 2 → WA ID`.

- `Airtable 12 — Update a Record`:
  - Record ID: `Airtable 2 → ID`;
  - Manychat Subscriber ID: primeiro `ID` retornado pelo `ManyChat 10`;
  - Enviado Manychat?: `Yes`.

### Rota de erro — contato já existente

```text
ManyChat 10 — Create Subscriber gera duplicidade
→ ManyChat 24 — Find Subscribers by a Custom Field
→ Airtable 25 — Update a Record
→ Skip 26
```

Configurações:

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

Permanece preservada e bloqueada temporariamente. Não apagar antes da conclusão de toda a auditoria de recuperação.

## Teste A — contato já existente

**Status: APROVADO.**

Validações realizadas com mais de um número:

- `Create Subscriber` reconheceu duplicidade;
- `ManyChat 24` encontrou o contato pelo campo `RM - WA ID Lookup`;
- retornou o Subscriber ID correto;
- `Airtable 25` gravou o ID;
- `Enviado Manychat? = true`;
- execução terminou corretamente via `Skip 26`.

Exemplos confirmados:

```text
WhatsApp = 5521976372196
Subscriber ID = 1122441770
```

```text
WhatsApp = 5521974512090
Subscriber ID = 1057713106
```

## Teste B — contato novo

**Status: CRIAÇÃO COMPROVADA E REGISTRO RECUPERADO.**

No teste com Mayara:

1. o número não havia passado pelo funil;
2. `ManyChat 10 — Create Subscriber` criou o contato;
3. foi retornado:

```text
Subscriber ID = 1697791282
```

4. o módulo `ManyChat 22` falhou inicialmente porque estava mapeado para `10. User ID`, que veio vazio;
5. o campo foi corrigido para o primeiro `ID` retornado pelo `ManyChat 10`;
6. o mesmo ajuste foi confirmado no `Airtable 12`;
7. o campo `RM - WA ID Lookup` foi preenchido;
8. a linha foi reprocessada e passou a apresentar:

```text
Manychat Subscriber ID = 1697791282
Enviado Manychat? = true
```

### Observação técnica honesta

A criação do contato novo foi comprovada e o erro de mapeamento foi corrigido. A linha foi recuperada com sucesso. Ainda é recomendável, quando surgir outro telefone totalmente novo, confirmar o percurso completo em uma única execução:

```text
Airtable 2 → ManyChat 10 → ManyChat 22 → Airtable 12
```

Essa confirmação adicional não impede o avanço para a recuperação dos leads e compradores históricos.

## Estado operacional atual

- normalização com DDI `55`: corrigida;
- contato existente: validado;
- contato novo: criação comprovada;
- Subscriber ID da rota nova: mapeado para `ID`, não `User ID`;
- gravação no Airtable: confirmada após reprocessamento;
- rota antiga: bloqueada e preservada;
- próximo bloco: recuperar leads sem compra e auditar compradores por combinação de produtos.

## Próxima etapa da auditoria

1. localizar os quatro leads reais que fizeram diagnóstico e não compraram;
2. confirmar Subscriber ID, perfil e estado das flags;
3. reenfileirar cada um no RM04 correspondente;
4. validar entrada nas automações RM02, RM07, RM08 ou RM09;
5. depois auditar os grupos de compra:
   - somente eBook;
   - eBook + áudio;
   - eBook + áudio + Reset Online.
