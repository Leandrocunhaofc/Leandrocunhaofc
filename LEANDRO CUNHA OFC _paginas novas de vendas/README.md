# LEANDRO CUNHA OFC — Páginas novas de vendas

Este diretório reúne páginas de vendas revisadas e os arquivos necessários para publicação no WordPress.

## Página disponível

### Homem Distraído

Arquivos:

- `HOMEM DISTRAIDO/wordpress-bloco-html.html`: arquivo correto para colar no bloco **HTML personalizado** do WordPress.
- `HOMEM DISTRAIDO/pagina-completa.html`: página HTML completa para backup e testes fora do WordPress.
- `HOMEM DISTRAIDO/politica-de-privacidade.html`: conteúdo da página de Política de Privacidade.
- `HOMEM DISTRAIDO/termos-de-uso.html`: conteúdo da página de Termos de Uso.

## Configurações confirmadas

- Produto: **7 Verdades Que Todo Homem Precisa Ouvir Antes de Ser Tarde**.
- Preço exibido: **R$ 37**.
- Checkout Hotmart: `https://pay.hotmart.com/C106036012S?checkoutMode=10&sck=distraido`.
- Quatro botões de compra configurados com o checkout.
- Parâmetro Hotmart `sck=distraido` preservado.
- UTMs recebidas pela página são encaminhadas ao checkout.
- Pixel da Meta: `1307273057695610`.
- O Pixel é carregado somente no domínio `leandrocunhaofc.com.br`, depois da autorização dos cookies de publicidade.
- O evento `InitiateCheckout` não é disparado manualmente na página, evitando duplicidade com o evento enviado pela Hotmart quando o checkout abre.
- Checklist e Protocolo Inicial de 7 Dias incluídos na compra principal.
- Audiobook e Workbook permanecem como complemento opcional no checkout da Hotmart.

## Instalação no WordPress

### 1. Criar as páginas legais

Antes da página de vendas, crie estas duas páginas no WordPress:

1. **Política de Privacidade**
   - Slug: `privacidade`
   - Cole o conteúdo de `politica-de-privacidade.html` em um bloco **HTML personalizado**.
2. **Termos de Uso**
   - Slug: `termos`
   - Cole o conteúdo de `termos-de-uso.html` em um bloco **HTML personalizado**.

Os links do rodapé da página de vendas apontam para `/privacidade` e `/termos`.

### 2. Criar a página Homem Distraído

1. No WordPress, acesse **Páginas → Adicionar nova**.
2. Nomeie a página como **Homem Distraído**.
3. Defina o endereço como `homem-distraido`.
4. Selecione um modelo de página **em branco**, **sem cabeçalho** ou **largura total**. O nome exato depende do tema instalado.
5. Adicione apenas um bloco **HTML personalizado**.
6. Abra `wordpress-bloco-html.html`, copie todo o conteúdo e cole no bloco.
7. Não cole em bloco de parágrafo, editor visual ou bloco de código.
8. Publique a página.

### 3. Limpar interferências do tema

Na configuração da página, quando disponível:

- ocultar o título automático da página;
- ocultar cabeçalho e rodapé do tema;
- remover barra lateral;
- usar largura total;
- remover margens e preenchimentos do container principal.

### 4. Limpar cache

Depois de publicar:

1. limpe o cache do WordPress;
2. limpe o cache do plugin de desempenho, se existir;
3. limpe o cache da hospedagem ou CDN, se existir;
4. abra a página em janela anônima.

### 5. Teste obrigatório

Teste nesta ordem:

1. abrir a página no celular;
2. aceitar ou rejeitar os cookies;
3. testar os quatro botões de compra;
4. confirmar que todos abrem o checkout `C106036012S`;
5. confirmar que o order bump do Audiobook + Workbook aparece na Hotmart;
6. abrir Política de Privacidade e Termos de Uso;
7. abrir as perguntas frequentes;
8. verificar a barra de compra fixa no celular;
9. no Gerenciador de Eventos da Meta, usar **Testar eventos** e confirmar o `PageView` depois de aceitar os cookies;
10. confirmar na Hotmart que a visita ao checkout gera o evento de início de checkout.

## Observações importantes

- No endereço de demonstração fora do domínio oficial, o Pixel permanece desativado para não contaminar as campanhas.
- No WordPress oficial, o domínio ativa o Pixel somente após o aceite dos cookies.
- Se o WordPress remover as tags `<script>` ao salvar, não publique a página incompleta. Isso normalmente indica restrição de permissão ou segurança do editor. Nesse caso, use uma conta administradora e configure o código por um recurso de inserção de HTML/JavaScript permitido pelo tema ou pela hospedagem.
- Se o site já possuir outro banner de cookies, não mantenha dois banners ativos. A versão incluída pode ser integrada ou substituída pelo gerenciador já existente.
- O arquivo `pagina-completa.html` é backup; para o WordPress, use `wordpress-bloco-html.html`.

