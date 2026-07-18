# RM03 — Leads Diagnóstico para ManyChat

**Projeto:** RESET MASCULINO_2  
**Atualização:** 17/07/2026  
**Status:** em validação final; cenário salvo e desligado

## Problema identificado

O módulo `ManyChat — Create Subscriber` falhava quando o WhatsApp já existia no ManyChat, retornando o erro:

> This WhatsApp ID already exists

O Make repetiu o mesmo registro diversas vezes e desativou automaticamente o cenário. O contato existente foi localizado no ManyChat e o Subscriber ID confirmado foi `1122441770`, associado ao WA ID `5521976372196`.

## Correções realizadas

1. Criado no ManyChat o campo personalizado:
   - Nome: `RM - WA ID Lookup`
   - Tipo: Texto

2. Confirmada a localização de contato existente pelo módulo:
   - `ManyChat — Find Subscribers by a Custom Field`

3. Contato de teste confirmado:
   - WA ID: `5521976372196`
   - Subscriber ID: `1122441770`

4. Registros antigos reais do Airtable foram recuperados e atualizados com:
   - `Manychat Subscriber ID`
   - `Enviado Manychat? = true`

5. No módulo `Create Subscriber`:
   - removido o `WA ID` do campo `Phone number`;
   - mantido somente em `WhatsApp phone number`.

Isso elimina a exigência indevida de `SMS opt-in`.

6. Criada a rota principal para contato novo:

```text
Create Subscriber
→ Set a Custom Field
→ Airtable Update a Record
```

7. No módulo `Set a Custom Field`:
   - Subscriber ID: ID retornado pelo `Create Subscriber`;
   - Field ID: `RM - WA ID Lookup`;
   - Field value: `Airtable 2 → WA ID`.

8. No `Airtable 12 — Update a Record` da rota principal:
   - Record ID: `Airtable 2 → ID`;
   - Manychat Subscriber ID: `ManyChat 10 → ID`;
   - Enviado Manychat?: `Yes`.

9. Criada rota de tratamento de duplicidade no `Create Subscriber`:

```text
Create Subscriber gera erro de duplicidade
→ ManyChat 24 — Find Subscribers by a Custom Field
→ Airtable 25 — Update a Record
→ Skip 26
```

10. Configuração da busca na rota de erro:
   - Field ID: `RM - WA ID Lookup`;
   - Field value: `Airtable 2 → WA ID`;
   - Limit: `1`.

11. Configuração do `Airtable 25 — Update a Record`:
   - Record ID: `Airtable 2 → ID`;
   - Manychat Subscriber ID: primeiro `ID` retornado pelo módulo de busca;
   - Enviado Manychat?: `Yes`.

12. Adicionado `Skip 26` no final da rota de erro para encerrar o bundle duplicado sem derrubar ou desativar o cenário.

13. A rota antiga:

```text
ManyChat 20 — Find Subscribers by a Custom Field
→ Airtable 21 — Update a Record
```

foi preservada, porém bloqueada temporariamente para servir como contingência durante os testes finais.

14. A rota principal de criação também permaneceu bloqueada temporariamente enquanto a fila antiga era limpa.

## Limpeza da fila antiga

Os registros claramente fictícios foram removidos do Airtable. Todos os registros reais pendentes foram processados individualmente até ficarem com:

- `Enviado Manychat?` marcado;
- `Manychat Subscriber ID` preenchido.

Para o WA ID `5521976372196`, os registros processados receberam:

```text
Manychat Subscriber ID = 1122441770
Enviado Manychat? = true
```

## Estado atual seguro

- Fila antiga limpa.
- Registros reais pendentes recuperados.
- Nenhum módulo antigo foi apagado.
- Rota antiga preservada e bloqueada.
- Rota principal preservada e bloqueada.
- Nova rota de duplicidade montada e salva.
- RM03 permanece desligado.

## Testes finais pendentes

### Teste A — contato existente

Objetivo:

- liberar temporariamente a rota principal;
- enviar um registro de diagnóstico com um WhatsApp já existente;
- confirmar que `Create Subscriber` gera duplicidade;
- confirmar que a rota de erro localiza o Subscriber ID existente;
- confirmar atualização do Airtable;
- confirmar que o cenário termina com sucesso via `Skip 26`.

### Teste B — contato realmente novo

Objetivo:

- usar um número real que ainda não exista no ManyChat;
- confirmar criação do contato;
- confirmar preenchimento automático de `RM - WA ID Lookup`;
- confirmar gravação do novo Subscriber ID no Airtable;
- confirmar `Enviado Manychat? = true`.

## Critério para ativação

O RM03 somente poderá ser reativado após os testes A e B concluírem sem erro. Após validação:

1. remover o bloqueio temporário da rota principal;
2. manter a rota de erro ativa;
3. decidir se a rota antiga será arquivada ou mantida como contingência;
4. ativar o agendamento do cenário;
5. executar o teste completo do diagnóstico até a recuperação correta por perfil.
