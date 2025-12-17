# Guia do Maintainer (site estático LINKE)

## O que é este repositório
- Este é um **site estático** servido a partir da pasta `linke/`.
- O HTML é um export de **WordPress/Elementor** (por isso vai ver muitas classes `elementor-*` e blocos `<style>` grandes inline).
- A configuração de deploy (Vercel) trata `linke/` como **diretório de output**.

## Pastas principais
- `linke/` — raiz do site em produção (páginas HTML + assets)
- `linke/shared/` — JS/CSS transversal ao site, adicionado por cima do export do Elementor
  - `styles.css` — overrides de estilo (navbar a negrito, estilo do banner de cookies, etc.)
  - `burger-menu.js` / `burger-menu.css` — comportamento/estilo do menu burger
  - `linke-consent.js` — lógica do banner de cookies + armazenamento/evento de consentimento
  - `google-tag.js` — carregador GA4 dependente de consentimento
- `scripts/` — utilitários + servidor local de desenvolvimento
  - `start_server.py` — servidor local para `linke/`

## Desenvolvimento local
- Para servir o site localmente:
  - `npm run dev` (ou `npm run start`)
  - Isto executa `scripts/start_server.py` e serve `linke/` em `http://localhost:8000` (ou 8001 se 8000 estiver ocupado).

## Deploy (Vercel)
- A config está em `vercel.json`:
  - `outputDirectory`: `linke`
  - Rewrite `/` → `/index.html`

## SEO + indexação
### O que foi adicionado/atualizado
- Cada página tem SEO por página no `<head>` (title/description/canonical/robots + OG/Twitter).
- Ficheiros de crawl na raiz do site:
  - `linke/robots.txt`
  - `linke/sitemap.xml`
- Snapshot para revisão:
  - `SEO_REPORT.md` (raiz do repo)

### Suposição de domínio (importante)
- Os canonicals e URLs do sitemap estão hardcoded para `https://linke.pt`.
- Se o domínio de produção mudar, atualize **todas as ocorrências** de `https://linke.pt` em:
  - `linke/*.html` (canonicals + URLs OG)
  - `linke/sitemap.xml`
  - `linke/robots.txt`

### Páginas intencionalmente NÃO indexadas
- `linke/area-cliente.html` e `linke/tracking.html` estão com `noindex, nofollow` no HTML e também estão disallowed no `robots.txt`.

## Consentimento de cookies + analytics (GA4)
### Armazenamento do consentimento + evento
- O consentimento é guardado em `localStorage` na key `linke_cookie_consent_v1` com o valor `accepted`.
- Quando o utilizador clica em “Aceitar”, `linke/shared/linke-consent.js` dispara:
  - `window.dispatchEvent(new Event('linke:cookie-consent-accepted'))`

### Comportamento de carregamento do GA4
- O Measurement ID do GA4 está definido em `linke/shared/google-tag.js`:
  - `G-8CLD3DJBFM`
- O GA só carrega **após consentimento** (se já tiver sido aceite numa visita anterior, ou imediatamente após o clique no botão de aceitar).
- Para alterar o ID do GA4, mude `MEASUREMENT_ID` em `linke/shared/google-tag.js`.

### Onde o banner aparece
- `linke/shared/linke-consent.js` só mostra o banner em:
  - `index`, `contato`, `solucoes`, `sobre-nos`
- Para adicionar uma página, inclua o respetivo nome do ficheiro (sem `.html`) em `ALLOWED_PAGES`.

## Widget de webchat (Botpress)
- A bolha de chat vem de um widget de webchat **Botpress**, injetado através de scripts externos.
- Está incluído em:
  - `linke/index.html`
  - `linke/solucoes.html`
  - `linke/sobre-nos.html`
  - `linke/contato.html`
- Se precisar de mudar o bot/widget, atualize os URLs dos scripts perto do fim dessas páginas (procure o comentário `Botpress Webchat inject`).

### Interação conhecida: offset do dropdown do menu burger
- Quando o Botpress está presente, algumas páginas podem ter o dropdown mobile deslocado (“abre muito em baixo”) devido a ancestrais com `transform`/`position`.
- Foi adicionada uma mitigação como **CSS ao nível da página junto ao bloco de inject do Botpress**, com a etiqueta:
  - `Protect dropdown menu from Botpress CSS interference`
- Se o dropdown voltar a partir depois de mexer no header, revalide:
  - Que IDs do wrapper do nav do Elementor existem nessa página (comum: `elementor-element-5dde0be` e/ou `elementor-element-f33cef5`)
  - Que o CSS de proteção está a apontar para o wrapper correto.

## Tipografia da navbar (negrito)
- Os itens da navbar são forçados a negrito através de overrides em:
  - `linke/shared/styles.css`
- Isto usa maior especificidade + `!important` para ganhar ao CSS gerado pelo Elementor.

## Tailwind (opcional)
- O Tailwind está configurado para gerar um output CSS para a pasta de uploads do Elementor:
  - Input: `tailwind.css`
  - Output: `linke/wp-content/uploads/elementor/css/tailwind-output.css`
- Script de watch:
  - `./tailwind-build.sh`

## Utilitários
- `npm run format:index` / `npm run fix:index` executam scripts Python em `scripts/` para reparar/prettify um ficheiro index (usado na manutenção do HTML exportado).

## Checklist rápido antes de publicar
- Abra estas páginas e valide:
  - O menu burger abre na posição correta (mobile)
  - A bolha de chat do Botpress aparece nas páginas pretendidas
  - O banner de cookies aparece apenas nas páginas pretendidas e o consentimento fica guardado
- Sanidade de SEO:
  - Confirmar que os canonicals correspondem ao domínio de produção
  - Submeter `https://<domain>/sitemap.xml` no Google Search Console
- Sanidade de analytics:
  - Em DevTools → Network, confirmar que `gtag/js?id=G-8CLD3DJBFM` só carrega após consentimento
