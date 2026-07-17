# Auditoria — Página do Curso Reset Masculino (17/07/2026)

URL: `https://leandrocunhaofc.com.br/curso-reset-masculino/`
Checkout: `https://pay.hotmart.com/V105952284O?checkoutMode=10`

Avaliação feita nos mesmos moldes da auditoria das páginas do ebook
(que resultou no template `build/template.html` e nas 4 páginas `reset-1..4`).
Papel da página no funil: **oferta do curso Reset Online** — destino do upsell
pós-ebook e possível destino direto de tráfego/bio.

---

## Nota geral

A página tem uma promessa central forte e a dor certa ("vivendo no automático"),
mas hoje ela é essencialmente **uma pilha de ~10 imagens PNG** com pouquíssimo
texto real. Tudo o que fez a página do ebook converter melhor — oferta clara com
preço, garantia, autoridade, FAQ, prova social, pixel com eventos, CTA fixo no
mobile, identidade visual preto+dourado — **não existe aqui**. É a página mais
importante do funil em ticket e a mais frágil em construção.

---

## O que está bom (manter na nova versão)

- **Headline de dor certeira**: "Você não está cansado. Está vivendo no
  automático." É o mesmo eixo do diagnóstico e do ebook — coerência de mensagem.
- **Cenas de identificação** (trânsito, banho, antes de dormir) — ótimo recurso,
  vale manter e ampliar.
- **3 CTAs ao longo da página**, o primeiro acima da dobra.
- **Microcompromissos sob o botão** ("Aplicável na vida real / Sem rotinas
  impossíveis / Acesso imediato") — bom padrão, igual ao do ebook.
- Checkout com `checkoutMode=10` (mesmo padrão das outras páginas).

---

## 🔴 Problemas críticos (afetam venda diretamente)

1. **A página inteira vive dentro de imagens.** São ~10 PNGs de 1500px
   carregando o conteúdo de venda (módulos? mecanismo? depoimentos?).
   Consequências:
   - **Peso/velocidade**: PNGs fotográficos grandes arrastam o carregamento no
     4G — e velocidade de página influencia o custo do anúncio no Meta.
   - **Ilegível no celular**: texto desenhado para 1536px espremido em ~390px.
   - **Invisível para Google e acessibilidade**: todos os `alt=""` vazios.
   - Na página do ebook fizemos o oposto: todo o conteúdo é texto real, e
     imagem só onde é imagem (foto, mockup).

2. **Não existe seção de oferta.** Nenhum preço em texto, nenhuma âncora
   ("de R$X por R$Y"), nenhum empilhamento de valor. O visitante clica no botão
   sem saber quanto custa e descobre no checkout — quebra de expectativa que
   gera abandono. No ebook: bloco de oferta com R$37 (de R$121) + o que está
   incluso, antes do botão.

3. **Não existe garantia.** A garantia de 7 dias (obrigatória na Hotmart e
   grande redutor de risco) não é mencionada em lugar nenhum do texto.

4. **Não existe FAQ, autoridade nem prova social em texto.** Sem "quem é
   Leandro Cunha", sem depoimentos legíveis, sem resposta às objeções
   (quanto tempo por dia? é aula em vídeo? por onde acesso? e se não funcionar
   pra mim?). Se algo disso está nas imagens, está inacessível na prática.

5. **Sem Meta Pixel na página** (no bloco colado não há script de pixel; se
   depende do tema, não dispara `InitiateCheckout`). As páginas do ebook
   disparam `PageView` + `InitiateCheckout` com valor no clique — sem isso a
   campanha do curso fica cega para otimização.

6. **Link do checkout sem rastreio.** `V105952284O?checkoutMode=10` sem `sck`
   nem UTM. Padrão do funil: `&sck=<origem>` (ex.: `sck=pagina-curso`) para
   saber o que converte — hoje é impossível separar venda vinda desta página
   da venda vinda do upsell/WhatsApp.

7. **Entregáveis vagos.** "Protocolo prático", "Clareza mental", "Direção
   prática" são promessas, não entregáveis. Falta o concreto: quantos módulos,
   quantas aulas, formato (vídeo? áudio? PDF?), duração, onde acessa
   (Hotmart Club?), o que é a "comunidade masculina" (é o Reset on Fire?).

---

## 🟡 Problemas de acabamento (corroem confiança)

8. **Erro de português no meio da promessa**: "SE VOCÊ ESTÁ PRONTO PARA PARAR
   DE SOBREVIVER E **VOLTA** A LIDERAR SUA VIDA;" → "…e **voltar** a liderar
   sua vida:". A frase ainda termina em ponto e vírgula e não conecta com nada.

9. **Headline com emenda estranha**: "…ESTÁ VIVENDO NO AUTOMÁTICO **E EXISTE
   SAÍDA**" — a terceira ideia entra colada. Melhor em três tempos:
   "Você não está cansado. Você está no automático. **E existe saída.**"

10. **Identidade visual fora do padrão do funil.** Amarelo puro `#ffff00` e
    cinzas genéricos, enquanto todo o resto do funil usa a paleta
    preto + dourado (`#d4a13a` / gradiente `#f7cf5e→#a9781f`) com tipografia
    condensada em caixa alta. A página do curso — o produto mais caro — parece
    de outra marca, e mais barata que a página do ebook de R$37.

11. **HTML sujo de copy/paste.** Os parágrafos vieram colados de outra
    ferramenta com dezenas de variáveis Tailwind inline (`--tw-*`,
    `caret-color`, `scrollbar-width`…). Além do peso, qualquer ajuste futuro
    vira caça ao tesouro. O padrão do funil é CSS com tokens no topo.

12. **Rodapé com links mortos**: "Política de Privacidade" e "Termos de Uso"
    apontam para `#`. Risco de reprovação/nota baixa no Meta Ads e quebra de
    confiança exatamente na hora da decisão.

13. **Emojis nativos como ícones** (📋⚡🎯…) renderizam diferente em cada
    aparelho. No ebook substituímos por SVG embutido (`build/iconizar.py`).

14. **Último CTA é uma imagem clicável**, não um botão real — não escala texto,
    não tem estado de toque, e some se a imagem falhar.

15. **Sem barra de CTA fixa no mobile** — padrão que adotamos nas páginas do
    ebook (`rm__sticky`) e que responde por boa parte dos cliques.

---

## Estrutura recomendada para a nova página

Espelhar o esqueleto validado do ebook (`build/template.html`), adaptado a
ticket maior (curso exige mais prova e mais concretude):

1. **Topbar** + **Hero**: eyebrow "RESET MASCULINO", headline em 3 tempos,
   subheadline, CTA, microcompromissos.
2. **Identificação/dor**: as 3 cenas (trânsito, banho, dormir) em texto real.
3. **Virada/mecanismo**: o que é o Reset (por que funciona onde "força de
   vontade" falha).
4. **O que você recebe**: módulos/aulas concretos + os 8 benefícios atuais
   como apoio, com ícones SVG.
5. **Prova social**: depoimentos em texto (com prints como apoio, não como
   conteúdo único).
6. **Oferta**: empilhamento de valor + âncora + preço em texto + CTA.
7. **Garantia de 7 dias** (selo + texto).
8. **Autoridade**: quem é Leandro Cunha.
9. **FAQ**: 5–7 objeções reais.
10. **CTA final** + rodapé com links reais + **barra fixa mobile**.
11. **Técnica**: pixel `PageView` + `InitiateCheckout` (com valor do curso),
    `&sck=pagina-curso` no checkout, tudo autossuficiente num bloco HTML
    (mesmo esquema de publicação das outras páginas).

## Informações necessárias para construir a nova página

- [ ] **Preço do curso** (valor cheio + valor promocional, se houver).
- [ ] **Conteúdo real**: módulos/aulas (nomes e o que entregam), formato e
      duração, onde o aluno acessa.
- [ ] **O texto que está nas ~10 imagens da página atual** (ou as imagens em
      si) — para não perder nada que já funciona.
- [ ] **Depoimentos** disponíveis (texto ou prints).
- [ ] A "comunidade masculina" prometida é o grupo **Reset on Fire**? Entra
      como bônus?
- [ ] URLs reais de Política de Privacidade e Termos de Uso.


---

## ✅ RESOLVIDO (17/07/2026)

Auditoria concluída e página reconstruída em `curso-reset-masculino.html`
(mesmo design system do ebook, blindada contra o wpautop). Publicada em
`/curso-reset-masculino/` e validada pelo Leandro no ar.

- Oferta: de R$297 por R$97 (preço atualizado na Hotmart pelo Leandro).
- Pixel: PageView + InitiateCheckout (R$97) no clique dos CTAs.
- Checkout: `V105952284O?checkoutMode=10&sck=pagina-curso`.
- Acesso informado: 1 ano na área de membros da Hotmart (FAQ).
- Comunidade: Reset on Fire (grupo exclusivo de alunos).
- Páginas legais criadas e publicadas: `/politica-de-privacidade/` e
  `/termos-de-uso/` (arquivos `politica-de-privacidade.html` e
  `termos-de-uso.html`, com estilo próprio independente do tema).
- Lição operacional: TODA página colada no WordPress precisa passar pela
  blindagem (CSS/JS em linha única, zero quebras de linha — ver
  `build/blindar.py`), senão o editor injeta parágrafos e quebra o layout.

### Pendência de acompanhamento
- [ ] Conferir no Gerenciador de Eventos da Meta se `InitiateCheckout`
      dispara na página do curso (clicar num CTA e observar o evento).
