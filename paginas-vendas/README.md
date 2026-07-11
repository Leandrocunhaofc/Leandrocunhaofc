# Reset Masculino — Páginas de Vendas (7 Verdades)

Funil de diagnóstico do e-book **7 Verdades Que Todo Homem Precisa Ouvir**.
São 4 páginas de resultado, uma para cada perfil do quiz.

## As 4 páginas

| Arquivo | Perfil (resultado do quiz) | Gravidade | Rastreio Hotmart (sck) |
|---|---|:---:|---|
| `reset-1-distraido.html` | Homem Distraído | ●○○○ | `sck=distraido` |
| `reset-2-apagado.html` | Homem Apagado | ●●○○ | `sck=apagado` |
| `reset-3-guerra-interna.html` | Homem em Guerra Interna | ●●●○ | `sck=guerra` |
| `reset-4-limite.html` | Homem no Limite do Automático | ●●●● | `sck=limite` |

Cada arquivo é **autossuficiente**: logo, foto e mockup do e-book já estão embutidos
(base64). É só colar o conteúdo num bloco **HTML personalizado** do WordPress.

## Como publicar no WordPress

1. Crie 4 páginas, ex.: `/resultado-distraido`, `/resultado-apagado`,
   `/resultado-guerra`, `/resultado-limite`.
2. Em cada página, adicione um bloco **HTML personalizado** e cole o conteúdo do
   arquivo correspondente.

## Ligar o quiz (Tally) nas páginas

No Tally, configure o redirecionamento de cada resultado para a URL correspondente:

- Homem Distraído → `/resultado-distraido`
- Homem Apagado → `/resultado-apagado`
- Homem em Guerra Interna → `/resultado-guerra`
- Homem no Limite → `/resultado-limite`

## Configurações embutidas

- **Checkout Hotmart:** `https://pay.hotmart.com/C106036012S?checkoutMode=10`
  com `&sck=<perfil>` para rastrear qual perfil converte mais.
- **Meta Pixel:** ID `1307273057695610` — dispara `PageView` ao abrir e
  `InitiateCheckout` (valor R$37) no clique do botão de compra.
- **Preço:** R$37 (de R$121). Garantia de 7 dias. Pagamento pela Hotmart.

## Como alterar (build)

O conteúdo compartilhado (oferta, 7 verdades, FAQ, rodapé) vive em
`build/template.html`, com tokens que o script `build/gerar-paginas.py`
preenche por perfil. Para mudar algo em TODAS as páginas de uma vez, edite o
template e rode o gerador — ele estampa os 4 arquivos novamente.

> Observação: o gerador usa caminhos absolutos do ambiente onde foi criado
> (imagens de origem). É mantido aqui como referência/histórico do build.
