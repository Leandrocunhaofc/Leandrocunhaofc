# RESET MASCULINO — COMANDO 0209

## Continuidade oficial — TRAFEGO PAGO 2_RESETMASCULINO

**Data:** 19/08/2026
**Evento:** QUEM ESTÁ NO COMANDO?
**Aula:** 02/09/2026 às 20h
**Status:** HANDOFF OFICIAL DE CONTINUIDADE

## Regra de governança

Toda decisão explicitamente aprovada, oficializada ou travada durante a continuidade do lançamento deve ser registrada no GitHub no mesmo ciclo de trabalho. O GitHub passa a ser a fonte de segurança do projeto, sem depender apenas do histórico da conversa.

## Estado atual do lançamento

O lançamento NÃO está começando do zero. A infraestrutura principal já foi construída.

### Funil oficial
Anúncio → Landing `Quem Está no Comando?` → inscrição → confirmação → grupo/WhatsApp + aquecimento → aula ao vivo → oferta do Reset Masculino → página do curso → Hotmart.

### Evento
- Nome: `QUEM ESTÁ NO COMANDO?`
- Data: 02/09/2026
- Horário: 20h
- Online, gratuito e ao vivo
- Destino principal de captação: `/quem-esta-no-comando`

### Infraestrutura já construída
- Landing de inscrição pronta, faltando apenas ajustes finais de frente/layout quando necessário.
- Página de confirmação pronta.
- Meta Pixel já integrado ao funil.
- Evento `Lead` configurado para disparar em `/inscricao-confirmada/?ok=1`.
- Make + Airtable + ManyChat estruturados para captação e comunicação.
- Grupo de WhatsApp da aula criado.
- Sequência de lembretes de WhatsApp estruturada.
- Base Diagnóstico preparada para reativação sem inclusão automática em `COMANDO_0209`; a pessoa precisa se cadastrar novamente para medir intenção e origem.
- Roteiro-base da aula e estratégia-base do lançamento existem como materiais de apoio.

## Pendências técnicas prioritárias

1. Criar automação no ManyChat para conteúdo orgânico: pessoa comenta `COMANDO` em publicação relacionada à aula → recebe o link oficial da landing da Super Aula.
2. Ajustes finais de frente/layout na landing, se necessários.
3. Finalizar validação operacional das mensagens/reminders do ManyChat sem desperdiçar créditos de Make.
4. Preservar a regra de eficiência: não executar operações em massa no Make quando a mesma tarefa puder ser feita diretamente em Airtable/ManyChat/GitHub sem consumo desnecessário de créditos.

## Tráfego pago — regra oficial

O documento vigente e prevalente é:
`01_META_ADS_PLANO_OFICIAL_TRAVADO.md`

Resumo travado:
- Campanha: `COMANDO 0209 — LEADS — FRIO`
- Objetivo: Leads
- Local de conversão: Website
- Evento: `Lead`
- Orçamento inicial: R$200/dia
- Estrutura: ABO
- Broad — Homens 28–55 — Brasil — R$100/dia
- Lookalike de quem concluiu o Diagnóstico — Homens 28–55 — Brasil — R$100/dia
- Advantage+ Placements
- Excluir quem já se inscreveu
- Fase 1: AD01 15s + AD02 + AD04 + AD06
- Fase 2: AD01 longo 25–35s + AD03 + AD05
- CTA: Cadastre-se
- Checkpoint de 72h = leitura, não cirurgia
- Teto de contingência: R$290/dia, não ponto de partida

## Criativos

O arquivo `02_CRIATIVOS_EM_ANALISE.md` contém os vídeos recebidos até 19/08/2026. Eles ainda não devem ser tratados como AD01/AD02/AD04/AD06 oficiais até avaliação e aprovação expressa.

A produção atual está na fase de definição/aprovação dos criativos da campanha. O usuário está quase finalizando os vídeos e quer combinar vídeos + artes estáticas de alto impacto, sem peças genéricas ou visual barato.

## Estrutura de aquisição do lançamento

Motores já definidos:
1. Meta Ads frio
2. Remarketing Meta
3. Orgânico Instagram — tratado em conversa separada
4. Base Diagnóstico — reativação quente
5. Opcional: compradores do eBook que ainda não compraram o curso

## Guardrails

- Não usar interesses como eixo principal da prospecção fria; prevalece Broad + Lookalike.
- Não pagar para reimpactar inscritos na campanha fria.
- Não começar com 6 criativos; largada oficial usa 4.
- Não alegar que excesso de texto gera penalização automática de entrega.
- CTA oficial da campanha fria: `Cadastre-se`.
- Não reconstruir infraestrutura pronta sem necessidade.
- Não consumir créditos de Make por conveniência quando houver rota direta equivalente.
- Não salvar dados pessoais de leads no GitHub.

## Ordem de continuidade recomendada

1. Confirmar/fechar automação de comentário `COMANDO` no ManyChat.
2. Finalizar e aprovar criativos.
3. Montar campanha fria no Meta conforme plano travado.
4. Estruturar remarketing.
5. Revisar aula/pitch/conversão.
6. Validar rastreamento e operação antes da abertura do tráfego.

## Regra para a nova conversa

A nova conversa deve se chamar **TRAFEGO PAGO 2_RESETMASCULINO** e deve começar deste estado, sem voltar para fases já concluídas. Sempre consultar os arquivos de `RESET_MASCULINO/COMANDO_0209/` antes de alterar uma decisão oficial.