# Guia à prova de erro — Publicar no WordPress

> Regra de ouro: **NÃO use "Editar com Elementor"** nessas páginas.
> Use o **editor normal** do WordPress com o bloco **"HTML personalizado"**.
> O Elementor trava com código grande e apaga tudo — o bloco HTML não.

## Mapa dos arquivos (qual arquivo → qual página → qual slug)

| Arquivo | Título da página | Slug (final do endereço) |
|---|---|---|
| `diagnostico.html` | Diagnóstico | `diagnostico` |
| `reset-1-distraido.html` | Resultado - Homem Distraído | `resultado-distraido` |
| `reset-2-apagado.html` | Resultado - Homem Apagado | `resultado-apagado` |
| `reset-3-guerra-interna.html` | Resultado - Homem em Guerra Interna | `resultado-guerra` |
| `reset-4-limite.html` | Resultado - Homem no Limite | `resultado-limite` |

⚠️ Os slugs precisam ser **exatamente** esses — o quiz procura por eles.

---

## Passo a passo (repita para as 5 páginas)

### 1. Criar a página
- WordPress → **Páginas → Adicionar nova**.
- **NÃO** clique em "Editar com Elementor". Fique no editor de blocos.
- Escreva o **Título** (ex.: *Resultado - Homem Distraído*).

### 2. Colar o código
- Clique no **"+"** → busque **"HTML personalizado"** → adicione o bloco.
- Cole **todo** o código do arquivo correspondente.
  - Para copiar: abra o arquivo (ou no GitHub, botão 📋 "copy raw"), **Ctrl+A**, **Ctrl+C**.

### 3. Publicar
- Clique em **Publicar**.

### 4. Deixar em tela cheia (tirar o menu do tema)
- Vá em **Páginas** (a lista) → passe o mouse na página → **Edição rápida**.
- Campo **Modelo** (à direita) → escolha **"Tela do Elementor"**.
- Campo **Slug** (à esquerda) → confirme que está o slug correto da tabela.
- **Atualizar**.

### 5. Testar
- Abra o endereço no navegador **e no celular**.
- Confira: página em tela cheia, sem menu roxo, acentos certos.
- Clique em **"Quero iniciar meu Reset"** → tem que abrir o **checkout da Hotmart**.

Repita para as 5. Faça as 4 de resultado primeiro; o `diagnostico` por último.

---

## Já vem embutido em cada arquivo (não precisa configurar)
- ✅ Link do **Hotmart** fixo no botão (`C106036012S`), com `sck` por perfil.
- ✅ **Meta Pixel** `1307273057695610` (PageView; InitiateCheckout no clique).
- ✅ **Acentuação** correta (UTF-8) e **layout responsivo** (mobile).
- ✅ Conteúdo **visível mesmo sem JavaScript** (fim da "tela escura").
- ✅ Logo, foto e mockup **embutidos** (não precisa subir imagem).

## Depois de publicar tudo
1. Teste o `diagnostico`: responda → deve **redirecionar** para a página do perfil certo.
2. Confira no **Airtable** se o lead de teste caiu (via Make).
3. Aponte seu **anúncio** para `/diagnostico` e **desligue o Tally**.

## Se algo der errado
- **Código aparece como texto / botão não abre:** você colou no bloco errado. Tem que ser **"HTML personalizado"**.
- **Aparece o menu roxo:** faltou o Modelo **"Tela do Elementor"** (passo 4).
- **Acentos quebrados (Ã³, Â€):** o arquivo usado está sem o `<meta charset>` — use os arquivos desta pasta (já corrigidos).
- **Não salva / apaga:** provável limite do servidor com imagem pesada. Nesse caso, avise para hospedar as imagens à parte (plano B).
