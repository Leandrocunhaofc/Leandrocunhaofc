# Comunidade Reset on Fire — Plano de Operação (18/07/2026)

Grupo de WhatsApp exclusivo para alunos do curso Reset Masculino (Reset Online).
Porta de entrada oficial: `leandrocunhaofc.com.br/comunidade` (página que
redireciona para o convite do grupo).

## Papel da comunidade no negócio

1. **Retenção**: aluno acompanhado conclui mais e pede menos reembolso
   (garantia de 7 dias — a primeira semana é crítica).
2. **Prova social**: os depoimentos reais que alimentam páginas e anúncios
   nascem aqui.
3. **Próximas ofertas**: público quente para mentorias/turmas futuras.

## Quem entra

- ✅ Comprou o **curso** (produto Hotmart `V105952284O`) — por qualquer porta:
  upsell pós-ebook OU compra direta na página `/curso-reset-masculino/`.
- ❌ Comprou só o ebook/áudio: ainda NÃO entra (o grupo é o benefício do
  curso; é também argumento do upsell).

## ⚠️ Buraco identificado no fluxo (fechar antes de divulgar)

O roteador pós-compra planejado (RM06B) dispara a partir da tag
`comprou_ebook`. **Quem compra o curso DIRETO pela página nova nunca recebe
essa tag** — logo não recebe boas-vindas nem convite do grupo.

**Correção:** criar gatilho próprio pela tag `comprou_curso`:

```
Hotmart (compra V105952284O aprovada)
   → Make RM05C aplica tag "comprou_curso"        (já existe — conferir)
   → ManyChat: NOVO fluxo "RM11 Boas-vindas Curso"
        Gatilho: tag "comprou_curso" aplicada
        Delay: 15 min
        Ação: enviar MSG-1 (abaixo) com link /comunidade
```

Quem veio do upsell também recebe `comprou_curso` → o mesmo fluxo cobre as
duas portas. (No RM06B, a Msg 3 pode então só parabenizar, sem duplicar o
convite — ou verificar se RM11 já enviou.)

## Textos prontos (copiar e colar)

### MSG-1 — Boas-vindas pós-compra do curso (WhatsApp, via ManyChat)

> Parabéns pela decisão, {{nome}}. 👊
>
> Você acaba de entrar no Reset Masculino — e a partir de agora você não
> caminha mais sozinho.
>
> ✅ Seu acesso ao curso já está no seu e-mail (área de membros da Hotmart).
> Se não achou, olhe o spam ou me responda aqui.
>
> 🔥 E o seu lugar na comunidade Reset on Fire está reservado. Entra por
> aqui: https://leandrocunhaofc.com.br/comunidade
>
> Chega lá, leia a mensagem fixada e se apresente. O Reset começa hoje.

### Descrição do grupo (WhatsApp → Dados do grupo → Descrição)

> 🔥 RESET ON FIRE — comunidade oficial dos alunos do Reset Masculino.
> Homens que decidiram sair do automático e voltar ao controle da própria
> vida. Respeito, apoio, propósito, disciplina e crescimento.
> Leia a mensagem fixada antes de postar.

### Mensagem fixada (regras + ritual de entrada)

> **BEM-VINDO AO RESET ON FIRE** 🔥
>
> Aqui dentro:
> 1. Respeito total. Sem ofensa, sem política, sem piada que diminui.
> 2. O que é dito aqui, fica aqui. Histórias dos irmãos não saem do grupo.
> 3. Sem divulgação de produto ou serviço sem autorização do Leandro.
> 4. O conteúdo do curso não sai do grupo (é o combinado dos Termos de Uso).
> 5. Dúvida de acesso/pagamento: chame o suporte no privado, não no grupo.
>
> **Chegou agora? Apresente-se:**
> — Nome, cidade e uma frase: "qual foi o dia em que você percebeu que
> estava no automático?"
>
> Pequenas ações. Grande reconstrução. 👊

### Ritual semanal sugerido (constância sem sobrecarga)

| Dia | Post do admin |
|---|---|
| Segunda | 🎯 **Missão da semana** — 1 ação prática ligada a um módulo |
| Quarta | 🧠 Provocação/reflexão curta (pode ser áudio do Leandro) |
| Sexta | ✅ **Check-in**: "quem cumpriu a missão? o que travou?" |

Domingo o grupo respira. Melhor 3 posts consistentes que 10 aleatórios.

## Proteção do link do grupo

- O link real do convite (`chat.whatsapp.com/...`) fica APENAS na página
  `/comunidade` — nunca em post público, bio ou anúncio.
- Se o link vazar (gente estranha entrando): WhatsApp → Dados do grupo →
  Link de convite → **Redefinir link**, e atualizar SÓ o arquivo
  `comunidade/index.html`. Todo o resto do funil continua apontando para
  `/comunidade` e nada mais precisa mudar.

## Checklist de implantação

- [ ] Conferir no Make: RM05C aplica tag `comprou_curso` para compra direta
      do produto (não só quando é upsell).
- [ ] Criar no ManyChat o fluxo **RM11 Boas-vindas Curso** (gatilho: tag
      `comprou_curso`; delay 15 min; envia MSG-1).
- [ ] Colar descrição e mensagem fixada no grupo (e fixar).
- [ ] Compra de teste de R$97 → validar: e-mail Hotmart chega → MSG-1 chega
      → link /comunidade abre o grupo → apresentação funciona.
- [ ] Definir quem modera além do Leandro (mínimo 1 pessoa da equipe).
- [ ] Agendar o ritual semanal (segunda/quarta/sexta).
