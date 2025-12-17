# LINKE — Website Estático

Site corporativo da **LINKE**, uma empresa de operações e tecnologia para ecommerce em Portugal. Este repositório contém o site estático exportado do WordPress/Elementor com melhorias de SEO, analytics e consentimento de cookies.

---

## 📁 Estrutura do Projeto

```
template/
├── linke/                    # Site em produção (output folder)
│   ├── index.html           # Página inicial
│   ├── solucoes.html        # Página de soluções
│   ├── sobre-nos.html       # Sobre a empresa
│   ├── contato.html         # Contacto
│   ├── robots.txt           # Configuração de crawlers
│   ├── sitemap.xml          # Mapa do site
│   ├── PUBLIC/              # Assets públicos (imagens, fonts, etc)
│   ├── shared/              # JS e CSS compartilhado
│   │   ├── styles.css       # Estilos globais e overrides
│   │   ├── burger-menu.js   # Menu hamburger
│   │   ├── linke-consent.js # Banner de cookies
│   │   ├── google-tag.js    # GA4 loader (consent-aware)
│   │   └── lazy-bg.js       # Lazy loading de backgrounds
│   └── wp-content/          # Assets do WordPress/Elementor
├── scripts/                 # Utilitários e scripts de desenvolvimento
│   └── start_server.py      # Servidor local
├── MAINTAINER_GUIDE.md      # Guia técnico detalhado (português)
├── SEO_REPORT.md           # Relatório de SEO (títulos/descrições)
├── BACKGROUND_CHANGE_GUIDE.md # Como alterar fundos de projectos
└── vercel.json             # Configuração de deploy
```

---

## 🚀 Quick Start

### Desenvolvimento Local

```bash
# Instalar dependências (opcional, para scripts)
npm install

# Iniciar servidor local
npm run dev
# ou
npm start
```

O site estará disponível em `http://localhost:8000` (ou porta 8001 se 8000 estiver ocupada).

### Build

```bash
npm run build
```

O site é estático, então não há processo de build real. O comando apenas confirma que o site está pronto.

---

## 🌐 Deploy

### Vercel (Recomendado)

O projeto está configurado para deploy na Vercel. A configuração em `vercel.json`:

```json
{
  "outputDirectory": "linke",
  "rewrites": [
    { "source": "/", "destination": "/index.html" }
  ]
}
```

**Domínio de Produção**: `https://linke.pt`

---

## 🔍 SEO e Indexação

### O que está implementado:
- ✅ Meta tags por página (title, description, canonical, robots)
- ✅ Open Graph e Twitter Cards
- ✅ JSON-LD (Schema.org) para dados estruturados
- ✅ `robots.txt` e `sitemap.xml`
- ✅ Páginas internas com `noindex` (`area-cliente.html`, `tracking.html`)

### Importante:
Se o **domínio de produção mudar**, atualize todas as ocorrências de `https://linke.pt` em:
- Todos os arquivos `.html` (canonical URLs e Open Graph)
- `linke/sitemap.xml`
- `linke/robots.txt`

Consulte `SEO_REPORT.md` para ver os títulos e descrições de todas as páginas.

---

## 📊 Analytics e Cookies

### Google Analytics 4
- **Measurement ID**: `G-8CLD3DJBFM`
- **Loader**: `linke/shared/google-tag.js`
- **Comportamento**: Só carrega **após consentimento** do utilizador

### Consentimento de Cookies
- **Script**: `linke/shared/linke-consent.js`
- **Storage**: `localStorage['linke_cookie_consent_v1'] = 'accepted'`
- **Evento**: Dispara `linke:cookie-consent-accepted` quando aceite
- **Banner**: Aparece apenas em páginas principais (não em páginas legais)

### Privacidade
- GA4 configurado com `anonymize_ip: true`
- Analytics não executa até o utilizador aceitar cookies

---

## 🤖 Chatbot (Botpress)

O site integra um chatbot Botpress nas seguintes páginas:
- `index.html`
- `solucoes.html`
- `sobre-nos.html`
- `contato.html`

**Scripts externos**:
```html
<script src="https://cdn.botpress.cloud/webchat/v3.4/inject.js"></script>
<script src="https://files.bpcontent.cloud/.../20250225174247-YDOR8OY4.js"></script>
```

**Nota**: O Botpress pode causar offset no menu dropdown. CSS de mitigação está implementado inline.

---

## 🎨 Customização

### Alterar Fundos de Projectos
Consulte `BACKGROUND_CHANGE_GUIDE.md` para instruções detalhadas sobre como alterar as imagens de fundo da secção "Os nossos Projectos".

**Resumo rápido**:
1. Adicione a imagem em `linke/PUBLIC/projects/`
2. Edite `linke/index.html` e procure por `lazy-bg`
3. Atualize o atributo `data-bg="PUBLIC/projects/sua-imagem.png"`

### Cores e Estilos
- **Cor principal**: `#C4FE61` (verde limão)
- **CSS global**: `linke/shared/styles.css`
- **Overrides Elementor**: A maioria dos estilos está inline no HTML

---

## 📝 Scripts Disponíveis

```bash
npm run dev          # Servidor de desenvolvimento local
npm run start        # Alias para dev
npm run build        # Confirma build (site estático)
npm run format:index # Formata/repara index.html (Python)
npm run fix:index    # Fix de index.html (Python)
```

---

## 🛠️ Tecnologias

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Framework**: WordPress/Elementor (exportado como estático)
- **Analytics**: Google Analytics 4
- **Chatbot**: Botpress
- **Deploy**: Vercel
- **Servidor Local**: Python 3 (SimpleHTTPServer)

---

## 📚 Documentação Adicional

- **`MAINTAINER_GUIDE.md`**: Guia técnico completo (em português) para maintainers
- **`SEO_REPORT.md`**: Lista de títulos e descrições SEO de todas as páginas
- **`BACKGROUND_CHANGE_GUIDE.md`**: Como alterar fundos dos projectos
- **`BURGER_MENU_REFERENCE.md`**: Referência do menu hamburger

---

## 🤝 Contribuir

Este é um projeto interno da LINKE. Para alterações:
1. Faça as modificações locais
2. Teste com `npm run dev`
3. Commit e push para o repositório
4. O deploy na Vercel é automático

---

## 📧 Suporte

Para questões técnicas sobre o site, consulte primeiro:
1. `MAINTAINER_GUIDE.md` — guia técnico detalhado
2. `BACKGROUND_CHANGE_GUIDE.md` — customização de projectos
3. `SEO_REPORT.md` — informações de SEO

---

## 📄 Licença

© 2025 LINKE. Todos os direitos reservados.