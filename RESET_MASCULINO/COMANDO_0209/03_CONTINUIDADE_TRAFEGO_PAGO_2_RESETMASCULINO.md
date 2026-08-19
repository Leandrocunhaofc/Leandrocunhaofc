# RESET MASCULINO — COMANDO 0209

## Continuidade oficial — TRAFEGO PAGO 2_RESETMASCULINO

**Data:** 19/08/2026
**Evento:** QUEM ESTÁ NO COMANDO?
**Aula:** 02/09/2026 às 20h
**Status:** HANDOFF OFICIAL DE CONTINUIDADE

## Regra de governança

Toda decisão explicitamente aprovada, oficializada, definida ou travada durante a continuidade do lançamento deve ser registrada neste GitHub no mesmo ciclo de trabalho. O GitHub é a fonte de segurança do projeto e não se deve depender exclusivamente do histórico das conversas.

Não salvar dados pessoais de leads, telefones, e-mails, IDs individuais ou informações sensíveis neste repositório.

## Regra de precedência

1. Arquivos marcados como OFICIAL/TRAVADO prevalecem sobre versões anteriores.
2. Rascunhos não substituem decisões aprovadas.
3. Quando uma decisão nova substituir outra, registrar a substituição explicitamente.
4. Não reconstruir infraestrutura já concluída sem necessidade operacional real.

# 1. PRODUTO, EVENTO E OBJETIVO

## Super Aula

- Nome: **QUEM ESTÁ NO COMANDO?**
- Submarca: Encontro Online Reset Masculino
- Data: **02/09/2026**
- Horário: **20h**
- Formato: online, gratuito e ao vivo
- Meta estratégica de captação discutida: cerca de 400–500 inscritos

Posicionamento aprovado:

> Um encontro gratuito para homens que continuam funcionando, cumprindo responsabilidades e resolvendo problemas — mas perceberam que alguma área importante da vida entrou no automático.
>
> Você vai entender o que está conduzindo suas decisões hoje, identificar onde perdeu direção e conhecer os primeiros passos para retomar presença, prioridade e comando.

Linhas centrais:
- “Nem todo homem que desapareceu foi embora.”
- “Funcionar não é comandar.”
- “Quem está no comando?”
- “Você não nasceu para vencer sozinho.”
- “RESET não é apagar a história. É parar de ser comandado por ela.”

## Curso ofertado na aula

**RESET MASCULINO — O Protocolo da Reconstrução Masculina**

Estrutura vigente:
- 11 módulos
- workbooks
- missões
- Operação Reset 8 Dias
- comunidade Reset On Fire
- 1 ano de acesso Hotmart
- garantia de 7 dias
- preço de oferta atual: **R$297**

Página oficial do curso:
`https://leandrocunhaofc.com.br/reset-masculino_curso_online/`

Checkout Hotmart:
`https://pay.hotmart.com/V105952284O?checkoutMode=10&sck=pagina-curso`

Pixel/Dataset Meta:
`1307273057695610`

# 2. FUNIL OFICIAL DO LANÇAMENTO

**Anúncio / Conteúdo / Base própria → Landing “Quem Está no Comando?” → inscrição → página de confirmação → grupo de WhatsApp + WhatsApp/e-mail de aquecimento → Super Aula ao vivo → oferta do Curso Reset Masculino → página oficial do curso → Hotmart → compra.**

A infraestrutura principal deste funil JÁ FOI construída. Não começar do zero.

# 3. PÁGINAS DO FUNIL

## Landing de inscrição — Página 1

Página criada e testada end-to-end.

Destino público principal:
`/quem-esta-no-comando/`

Arquivo de referência produzido:
`QUEM_ESTA_NO_COMANDO_V7_FINAL_ROBUSTA_WORDPRESS.txt`

Características implementadas:
- formulário com Nome, WhatsApp e E-mail
- consentimento
- turma_aula = `comando_02092026`
- pagina_origem = `quem_esta_no_comando`
- origem_detalhada com fallback `direto_organico`
- UTMs e parâmetros de origem
- JavaScript normaliza WhatsApp para 55 + número antes do POST quando executado
- Meta Pixel com PageView/ViewContent
- NÃO dispara Lead nesta página
- countdown para 02/09/2026 às 20h
- webhook Make da captação integrado

Webhook da landing:
`https://hook.us2.make.com/2cy6m92dne19p8vqdgdd99wh5oaryf1n`

## Página de confirmação — Página 2

Destino:
`/inscricao-confirmada/?ok=1`

Arquivo de referência produzido:
`INSCRICAO_CONFIRMADA_COMANDO_V2_GRUPO_AGENDA_WORDPRESS.txt`

Características:
- confirma inscrição e data
- CTA de agenda
- CTA para grupo WhatsApp
- seção do grupo
- entrega do eBook bônus
- Meta Pixel
- evento `Lead` dispara SOMENTE com `?ok=1`
- deduplicação via localStorage
- depois remove query da URL

## Grupo WhatsApp

Nome:
**QUEM ESTÁ NO COMANDO? | RESET MASCULINO**

Grupo em modo admin-only.

Link de convite:
`https://chat.whatsapp.com/FzQXSOJWR8BIRjcj3eaj62`

Redirect estável:
`https://leandrocunhaofc.com.br/comando/`

## Aula YouTube

Live agendada:
**QUEM ESTÁ NO COMANDO? | Encontro Online Reset Masculino**

URL:
`https://youtube.com/live/O0EbrIonZVg?feature=share`

Redirect estável para aula:
`https://leandrocunhaofc.com.br/aula-comando/index.html`

# 4. BÔNUS PÓS-INSCRIÇÃO

eBook de preparação:
**Dez Passos para Desenvolver Sua Vida em 10 Dias através do Domínio da Inteligência Emocional**

PDF hospedado:
`https://leandrocunhaofc.com.br/wp-content/uploads/2026/08/1O-PASSOS-PARA-DESEVOLVER-SUA-VIDA-EM-DEZ-DIAS-ATRAVES-DO-DOMINIO-DA-INTELIGENCIA-EMOCIONAL.pdf`

Usado como presente/preparação pós-inscrição, não como substituto da oferta principal.

# 5. MAKE — CENÁRIOS COMANDO

## COMANDO 01 — Captação Encontro 02/09

Arquitetura:
**Webhook → Airtable Create Record → HTTP 302 para página de confirmação**

Redirect final:
`https://leandrocunhaofc.com.br/inscricao-confirmada/?ok=1`

Captação testada com sucesso.

## COMANDO 02 — Radar ManyChat

Objetivo:
pegar registros pendentes do Airtable e inserir/atualizar a pessoa no ecossistema ManyChat, aplicar tag e enviar fluxo de boas-vindas.

Filtro Airtable usado:
`AND({Status Radar}="PENDENTE",{Consentimento}="true",{WhatsApp}!="")`

Arquitetura atual:
**Airtable Search → ManyChat Create Subscriber → Manage Tags → Send a Flow**

Rota de contato existente:
quando Create Subscriber retorna erro por contato já existente, usa:
**ManyChat Find Subscribers by a Custom Field**
Campo: `RM - WA ID Lookup`
Valor: `55` + WhatsApp
→ Manage Tags
→ Send Flow
→ Skip

Essa arquitetura foi testada com sucesso em contato já existente.

Tag oficial dos inscritos da aula:
`COMANDO_0209`

Fluxo de boas-vindas:
**COMANDO 02 — Boas-vindas Inscrição**

Flow ID:
`content20260817233852_573510`

Template:
`comando_boas_vindas_0209`

O fluxo ficou online. O envio no teste do Make apareceu verde, mas a entrega da mensagem de boas-vindas ainda precisava de validação final com outro número. Não desperdiçar créditos tentando repetidamente no mesmo contato.

Pendência futura do COMANDO02:
- validar entrega com segundo número real
- adicionar atualização de Status Radar = PROCESSADO nas duas rotas, após confirmação segura

## COMANDO 03 — Reativação Base Diagnóstico

Cenário criado originalmente para copiar elegíveis da tabela Leads Diagnóstico para a tabela operacional da campanha.

Decisão posterior:
**COMANDO03 fica OFF** para não gastar créditos de Make em migração em massa.

A migração foi executada diretamente via Airtable, sem uso de créditos do Make.

# 6. AIRTABLE

Base:
**Reset Masculino**

Base ID:
`appzi726FXrGGCzKx`

## Tabela de inscritos da Super Aula

Tabela:
**COMANDO — Inscritos 02/09**

Table ID:
`tbldTbwJTCQebMUVz`

Campos principais:
- Nome
- WhatsApp
- Email
- Data inscrição
- UTMs
- Consentimento
- Status Radar
- ManyChat Subscriber ID
- Boas-vindas enviada em
- Erro Radar

Status Radar:
- PENDENTE
- PROCESSADO
- ERRO

## Base original do Diagnóstico

Tabela:
**Leads Diagnóstico**

Table ID:
`tblJmsIBSiBUhvKCu`

Campos relevantes incluem:
- Nome
- Email
- WhatsApp
- Resultado diagnóstico
- Comprou Reset?
- Comprou eBook?
- Comprou Áudio?
- Pediu SAIR?
- Consentimento WhatsApp?
- ManyChat Subscriber ID
- WA ID ManyChat
- Criado em

View criada:
**COMANDO 0209 — EXPORTAÇÃO**

Filtros oficiais da view:
- Consentimento WhatsApp? marcado
- Pediu SAIR? desmarcado
- Comprou eBook? desmarcado
- Comprou Reset? desmarcado
- WhatsApp não vazio
- ManyChat Subscriber ID não vazio

## Tabela operacional da Base Diagnóstico

Tabela:
**COMANDO 0209 — Base Diagnóstico**

Table ID:
`tblGRdXeEZdqpYfSQ`

Campos:
- Nome
- WhatsApp
- Email
- Resultado diagnóstico
- ManyChat Subscriber ID
- Status Convite COMANDO
- Data convite
- Origem
- Observações COMANDO

Status Convite COMANDO:
- PENDENTE
- ENVIADO
- CLICOU
- INSCREVEU
- ERRO

Origem default:
`base_diagnostico`

Migração direta concluída.
Verificação final correta:
- **616 linhas totais** na tabela
- **613 contatos preenchidos/elegíveis**
- **3 linhas vazias** criadas manualmente no início

Não confundir esse total com 614; o número verificado de contatos preenchidos é 613.

Regra estratégica fundamental:
**não adicionar automaticamente essa base à tag `COMANDO_0209`.**

Fluxo correto:
**Base Diagnóstico → convite/reactivação → landing Quem Está no Comando? → nova inscrição → COMANDO_0209 → grupo/reminders → aula.**

Isso preserva intenção, origem e mensuração.

Tag de segmentação da base antes da inscrição:
`COMANDO_BASE_DIAGNOSTICO`

Origem detalhada a usar no convite/link:
`base_diagnostico`

# 7. MANYCHAT — COMUNICAÇÃO E REMINDERS

Templates aprovados/construídos para o evento:
- `comando_boas_vindas_0209`
- `comando_7dias_0209`
- `comando_3dias_0209`
- `comando_amanha_0209`
- `comando_hoje_0209`
- `comando_2horas_0209`
- `comando_1hora_0209`
- `comando_ao_vivo_0209`
- modelo +20 min após início da aula

Agenda planejada/estruturada:
- 26/08 19h — 7 dias
- 30/08 19h — 3 dias
- 01/09 19h — amanhã
- 02/09 08h — hoje
- 02/09 18h — 2h
- 02/09 19h — 1h
- 02/09 20h — ao vivo
- 02/09 20h20 — +20 min após o início da aula

Atenção:
Existe limitação observada de **250 mensagens/24h** no ambiente ManyChat/WhatsApp. Não disparar os 613 contatos da base de uma vez sem resolver/planejar esse limite. Importar/segmentar não é o mesmo que enviar.

# 8. AUTOMAÇÃO MANYCHAT AINDA PENDENTE — COMENTÁRIO COMANDO

Pendência imediata antes de voltar integralmente à campanha:

Quando Leandro publicar Reels/feed/conteúdo relacionado à Super Aula no Instagram e uma pessoa comentar:
**COMANDO**

o ManyChat deve responder/acionar DM automaticamente com o link para a **LANDING DE INSCRIÇÃO** da Super Aula.

Não mandar direto para a aula.

Objetivo:
comentário → DM → landing → cadastro oficial → COMANDO_0209 → restante do funil.

Essa automação ainda precisa ser construída/finalizada.

# 9. META ADS — PLANO OFICIAL TRAVADO

Arquivo prevalente:
`01_META_ADS_PLANO_OFICIAL_TRAVADO.md`

Configuração oficial:

| Item | Configuração |
|---|---|
| Campanha | `COMANDO 0209 — LEADS — FRIO` |
| Objetivo | Leads |
| Local de conversão | Website |
| Evento | `Lead` em `/inscricao-confirmada/?ok=1` |
| Orçamento inicial | R$200/dia |
| Teto de contingência | R$290/dia, não ponto de partida |
| Estrutura | ABO |
| Conjunto A | Broad — Homens 28–55 — Brasil — R$100/dia |
| Conjunto B | Lookalike de quem concluiu o Diagnóstico — Homens 28–55 — Brasil — R$100/dia |
| Posicionamento | Advantage+ Placements |
| Exclusão | quem já se inscreveu |
| Criativos Fase 1 | AD01 15s + AD02 + AD04 + AD06 |
| Criativos Fase 2 | AD01 longo 25–35s + AD03 + AD05 |
| CTA | Cadastre-se |
| Destino | `/quem-esta-no-comando` |
| Checkpoint | 72h = leitura, não cirurgia |

Correções oficiais:
- Broad + Lookalike, não interesses como eixo principal.
- Lookalike do Diagnóstico é semente própria limpa e prioritária.
- excluir inscritos da prospecção fria.
- largada com 4 criativos, não 6.
- não afirmar que excesso de texto gera penalidade automática de entrega.
- CTA `Cadastre-se`, não `Saiba mais`.
- 72h é ponto de leitura, não gatilho automático de reestruturação.

# 10. MOTORES DE AQUISIÇÃO

1. **Meta Ads frio** — escala.
2. **Remarketing Meta** — visitantes, engajados, viewers e públicos quentes pertinentes.
3. **Instagram orgânico** — tratado em conversa específica separada.
4. **Base Diagnóstico** — reativação de homens que fizeram Diagnóstico e não compraram.
5. **Possível quinto motor** — compradores do eBook que ainda não compraram o curso.

# 11. CRIATIVOS

Arquivo atual:
`02_CRIATIVOS_EM_ANALISE.md`

Vídeos registrados ali ainda NÃO são automaticamente AD01, AD02, AD04 ou AD06 até avaliação e aprovação.

Para cada criativo aprovado, registrar:
- função
- ângulo
- público
- fase
- hook
- copy
- CTA
- posição na campanha

Diretriz visual:
- premium
- cinematográfica
- alto contraste
- tensão visual
- peças que façam parar o scroll
- não usar visual genérico de coach
- evitar banco de imagem óbvio
- pode ser provocativo/polêmico visualmente quando coerente com a marca

Frases centrais possíveis:
- “QUEM ESTÁ NO COMANDO?”
- “Nem todo homem que desapareceu foi embora.”
- “Funcionar não é comandar.”
- “Você trabalha. Resolve. Sustenta. Mas quem está no comando?”
- “Um homem pode estar presente e ainda assim ter desaparecido de si mesmo.”
- “RESET não é apagar a história. É parar de ser comandado por ela.”

# 12. POSICIONAMENTO DA MARCA

Masculinidade:
- firme
- emocionalmente madura
- prática
- responsável
- espiritual

Evitar:
- caricatura alfa
- hostilidade contra mulheres
- humilhação
- promessa milagrosa
- linguagem de coach genérico

Tese:
um homem pode trabalhar, resolver, sustentar e ainda assim não estar comandando a própria vida. Pode estar distraído, em guerra, no limite ou apagado.

RESET ajuda a recuperar:
- identidade
- presença
- propósito
- disciplina
- espiritualidade
- comunidade

# 13. AULA E CONVERSÃO

Existe roteiro-base da Super Aula recebido anteriormente e material de estratégia de lançamento.

O roteiro contempla:
- abertura
- identificação da dor
- tese central
- construção da consciência
- protocolo de reconstrução
- apresentação do curso
- oferta por R$297
- objeções
- fechamento
- downsell previsto no material-base

Os cinco movimentos do protocolo:
1. Enxergar
2. Interromper
3. Reordenar
4. Reconstruir
5. Sustentar

A aula ainda deve ser revisada/finalizada como peça de conversão antes de 02/09, mas não deve ser reconstruída do zero.

# 14. REGRA DE EFICIÊNCIA OPERACIONAL

Leandro não quer desperdício de créditos do Make.

Antes de qualquer operação em massa:
1. estimar consumo de créditos;
2. avaliar alternativa direta em Airtable, ManyChat, GitHub ou outro sistema;
3. separar teste de produção;
4. não executar centenas de operações só para validar;
5. não afirmar que algo não gasta créditos se gastar.

# 15. ORDEM DE CONTINUIDADE

1. Finalizar automação ManyChat de comentário `COMANDO` → DM → landing.
2. Finalizar/aprovar criativos da Fase 1.
3. Criar públicos necessários no Meta: Broad, Lookalike e exclusão de inscritos.
4. Montar campanha `COMANDO 0209 — LEADS — FRIO` exatamente conforme plano travado.
5. Estruturar remarketing.
6. Planejar disparo da Base Diagnóstico respeitando limite de 250 mensagens/24h.
7. Fazer teste final COMANDO02 com segundo número real e concluir atualização PROCESSADO quando seguro.
8. Revisar aula/pitch/conversão.
9. Validar tracking completo antes de abrir tráfego.
10. Acompanhar 72h iniciais sem cirurgia precipitada.

# 16. REGRA PARA A NOVA CONVERSA

A conversa nova deve se chamar:
**TRAFEGO PAGO 2_RESETMASCULINO**

Ela deve começar exatamente deste estado.

Antes de sugerir mudanças, ler:
- `00_FONTE_DA_VERDADE.md`
- `01_META_ADS_PLANO_OFICIAL_TRAVADO.md`
- `02_CRIATIVOS_EM_ANALISE.md`
- `03_CONTINUIDADE_TRAFEGO_PAGO_2_RESETMASCULINO.md`

Não voltar para fases concluídas.

Toda nova decisão aprovada/travada deve ser registrada no GitHub no mesmo ciclo de trabalho.

# 17. ATUALIZAÇÃO OPERACIONAL — AUTOMAÇÃO INSTAGRAM FEED/REELS

**Data:** 19/08/2026  
**Status:** CONCLUÍDA / ONLINE

Automação criada e ativada no ManyChat:

`COMANDO 0209 — Instagram Comentou COMANDO — Feed e Reels`

Configuração vigente:
- gatilho: comentário contendo a palavra `COMANDO` em publicação do Feed ou Reel;
- DM inicial com confirmação por botão `QUERO PARTICIPAR`;
- tag de intenção: `IG - Pediu COMANDO 0209`;
- tag de origem: `IG - Origem Comentário`;
- segunda DM com informações da Super Aula e botão `FAZER INSCRIÇÃO`;
- destino: landing oficial `/quem-esta-no-comando/`;
- rastreamento: `utm_source=instagram`, `utm_medium=organic`, `utm_campaign=comando_0209`, `utm_content=comentario_feed_reels`, `origem_detalhada=comentario_feed_reels`;
- tag pós-envio: `IG - Link COMANDO 0209 Enviado`;
- arte da Super Aula inserida na mensagem de inscrição.

A automação antiga do Diagnóstico permaneceu preservada; a nova foi criada por duplicação e adaptação, sem reconstruir a estrutura do zero.


# 18. ATUALIZAÇÃO OPERACIONAL — INSTAGRAM E BASE DIAGNÓSTICO

**Data:** 19/08/2026  
**Status:** AUTOMAÇÕES INSTAGRAM CONCLUÍDAS / BASE AINDA NÃO DISPARADA

## Instagram

Leandro confirmou como concluídas as automações de captação por:
- resposta `COMANDO` em Story;
- envio de `COMANDO` no Direct;
- comentário `COMANDO` em Feed/Reels.

A automação de Story foi criada como:
`COMANDO 0209 — Instagram Respondeu COMANDO — Story`

Regra preservada em todas as origens:
**interação no Instagram → DM → landing oficial → inscrição → grupo e sequência do evento.**

Não enviar diretamente para o grupo ou para a aula.

## Base Diagnóstico — leitura verificada no Airtable

Tabela:
`COMANDO 0209 — Base Diagnóstico` (`tblGRdXeEZdqpYfSQ`)

Leitura em 19/08/2026:
- total atual: **613 contatos**;
- `PENDENTE`: **613**;
- `ENVIADO`: **0**;
- `CLICOU`: **0**;
- `INSCREVEU`: **0**;
- `ERRO`: **0**.

Conclusão: a base permanece preparada, mas **nenhum disparo de produção foi iniciado**.

O objetivo da reativação continua sendo levar o contato à landing oficial para medir intenção. Somente após nova inscrição ele deve seguir para a tag de inscrito, grupo e lembretes da Super Aula.

A consulta ao conector do Make retornou erro interno ao tentar listar cenários; nenhum cenário foi executado ou alterado durante essa verificação.


# 19. AUDITORIA OPERACIONAL DO MAKE

**Data:** 19/08/2026  
**Status:** CORREÇÕES CRÍTICAS CONCLUÍDAS / DISPARO DA BASE AINDA NÃO CRIADO NEM INICIADO

Auditoria realizada diretamente no Make autenticado, sem executar disparos de produção.

## Correções aplicadas

1. Cenário ID `5983755`:
   - era o antigo `COMANDO 03 — Reativação Base Diagnóstico`;
   - arquitetura confirmada: `Airtable Search Records → Airtable Bulk Upsert Records (advanced)`;
   - não possuía módulo de envio de mensagem;
   - havia sido reativado indevidamente e executou novamente em 19/08/2026, consumindo 672 operações;
   - foi desligado;
   - foi renomeado para `ARQUIVO — COMANDO 03 migração concluída — NÃO ATIVAR`.

2. Cenário `COMANDO 02 — Radar ManyChat` (ID `5972525`):
   - confirmado como radar dos novos inscritos da tabela `COMANDO — Inscritos 02/09`, não como reativação da Base Diagnóstico;
   - estava desligado automaticamente pelo Make por erro de validação;
   - causa identificada na rota de criação de assinante: o campo obrigatório `Subscriber ID` recebia o bundle inteiro do módulo 3;
   - mapeamento corrigido para `3. User ID`;
   - cenário salvo e mantido desligado;
   - não foi executado nem reativado; permanece pendente o teste controlado com um segundo número real.

3. Duplicidade `RM05C — Compra Curso Reset — Marcar Curso`:
   - ID `5600289`: versão simples, zero execuções, desligada e renomeada para `ARQUIVO — RM05C simples antigo — NÃO ATIVAR`;
   - ID `5600338`: versão completa de produção preservada e ativa.

4. Cenários de arquivo que estavam ligados apesar do nome `NÃO ATIVAR`:
   - `ARQUIVO — RM05B antigo — NÃO ATIVAR` (ID `5599996`) foi desligado;
   - `ARQUIVO — RM05C antigo — NÃO ATIVAR` (ID `5600203`) foi desligado.

5. `COMANDO 01 — Captação Encontro 02/09`:
   - arquitetura verificada: `Webhook → Airtable Bulk Upsert Records (advanced) → Webhook response`;
   - cenário ativo, com execuções bem-sucedidas;
   - nenhuma alteração aplicada.

## Conclusão sobre a Base Diagnóstico

Após a auditoria, não existe no Make um cenário completo de produção que envie o convite aos 613 contatos da tabela `COMANDO 0209 — Base Diagnóstico`.

O antigo `COMANDO 03` era apenas a migração de dados e não deve ser reutilizado para envio.

Portanto:
- nenhum convite da Base Diagnóstico foi disparado;
- os 613 contatos permanecem em `PENDENTE`;
- é necessário criar um cenário novo e separado para o convite;
- o cenário deve enviar a pessoa para a landing oficial, nunca diretamente para o grupo;
- deve haver teste com um contato antes da produção;
- a produção deve respeitar o limite observado de 250 mensagens/24h e atualizar `PENDENTE → ENVIADO/ERRO`;
- não ativar o cenário até confirmar o fluxo/template correto do convite no ManyChat.
