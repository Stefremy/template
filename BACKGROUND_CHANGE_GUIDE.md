# Guia para Alterar os Fundos dos Projectos

Este guia explica como alterar os fundos (backgrounds) das secções de projectos na página inicial do site LINKE. Estes fundos são imagens que são carregadas de forma lazy (preguiçosa) para melhorar o desempenho.

## Importante: Onde Estão os Fundos

Os fundos dos projectos **não estão em posts separados**. Eles estão incorporados diretamente dentro da estrutura HTML do arquivo `linke/index.html`, numa secção de containers Elementor chamada "Os nossos Projectos" (em torno da linha 1850).

## Estrutura dos Fundos

Os fundos são definidos em elementos HTML com a classe `lazy-bg` e um atributo `data-bg` que aponta para o caminho da imagem. Estes elementos são containers Elementor que envolvem todo o conteúdo de cada projecto.

### Exemplo de Elemento HTML

```html
<div class="elementor-element elementor-element-aba69b1 e-con-full e-flex e-con e-child lazy-bg" 
     data-id="aba69b1" 
     data-element_type="container" 
     data-bg="PUBLIC/projects/madpixelhome.png" 
     style="padding:24px; border-radius:12px;">
    <!-- Conteúdo do projecto: título, buttons, descrição, KPIs -->
</div>
```

## Como Alterar um Fundo

1. **Abrir o Arquivo**: Abra o arquivo `linke/index.html` no editor de código.

2. **Procurar pela Secção**: Use Ctrl+F (ou Cmd+F) para procurar por "Os nossos Projectos" ou pelo atributo `data-bg` do projecto que deseja alterar.

3. **Encontrar o data-bg**: Dentro do elemento `lazy-bg`, verá algo como:
   ```
   data-bg="PUBLIC/projects/madpixelhome.png"
   ```

4. **Substituir a Imagem**:
   - Coloque a nova imagem na pasta `linke/PUBLIC/projects/` (ou subpasta apropriada).
   - Atualize o valor do `data-bg` para o novo caminho da imagem, por exemplo: 
     ```
     data-bg="PUBLIC/projects/nova-imagem.png"
     ```

5. **Verificar o Caminho**: Certifique-se de que o caminho é relativo à raiz do site (linke/). As imagens devem estar acessíveis via URL como `https://linke.pt/PUBLIC/projects/nova-imagem.png`.

## Scripts Relacionados

- **lazy-bg.js**: Este script (localizado em `linke/shared/lazy-bg.js`) é responsável por carregar as imagens de fundo de forma assíncrona quando o elemento entra na viewport. Não altere este script a menos que seja necessário para funcionalidades avançadas.

## Dicas

- **Formatos de Imagem**: Use formatos otimizados como PNG, JPG ou WebP para melhor desempenho.
- **Tamanho e Resolução**: As imagens devem ser de alta qualidade mas otimizadas para web. Considere usar ferramentas como ImageOptim ou TinyPNG.
- **Responsividade**: As imagens são exibidas em containers responsivos, então certifique-se de que a imagem se adapta bem a diferentes tamanhos de ecrã.
- **Conteúdo da Imagem**: O fundo fica por trás do conteúdo do projecto (título, buttons, descrição, KPIs), portanto escolha imagens com contraste apropriado para garantir que o texto seja legível.

## Projectos Atuais e Seus Fundos

- **MADPiXEL**: `PUBLIC/projects/madpixelhome.png` (elemento-aba69b1)
- **Aurora**: `PUBLIC/projects/aurora-home.png` (procure por "Aurora" no index.html)
- **Outros**: Verifique o `index.html` para projectos adicionais.

Se adicionar novos projectos, siga o mesmo padrão dentro da secção "Os nossos Projectos":
- Use `class="lazy-bg"` no elemento container
- Adicione o `data-bg` com o caminho da imagem

## Estrutura de um Projecto Completo

Cada projecto tem esta estrutura dentro de um container `lazy-bg`:
- Título/Nome do projecto
- Categoria (tags/botões com categorias)
- Descrição do projecto
- KPIs (Key Performance Indicators) com métricas

Tudo isto está envolvido pelo `lazy-bg` container que carrega a imagem de fundo.

## CSS para Editar

Se o maintainer quiser customizar o estilo dos projectos (além de mudar as imagens), aqui estão os CSS inline que pode editar:

### 1. **Imagem de Fundo** (Container Principal)
```html
<div class="lazy-bg" data-bg="PUBLIC/projects/madpixelhome.png" 
     style="padding:24px; border-radius:12px;">
```
- `padding`: Espaço interno do container (24px)
- `border-radius`: Cantos arredondados (12px)

### 2. **KPIs (Métricas)**
```html
<ul class="project-kpis" style="list-style:none; padding:0; margin:12px 0 0; display:flex; flex-wrap:wrap; gap:8px 16px; font-size:12px; color:rgba(255,255,255,0.9);">
```
- `margin`: Espaço acima da lista (12px 0 0)
- `gap`: Espaço entre items (8px 16px)
- `font-size`: Tamanho do texto (12px)
- `color`: Cor do texto (branco semi-transparente)

### 3. **Números das Métricas** (em destaque)
```html
<span style="color:#C4FE61; font-weight:700;">+40%</span>
```
- `color`: Cor verde limão (#C4FE61) — a cor principal do design
- `font-weight`: 700 (bold)

### 4. **Container de Buttons**
```html
<div style="display: flex; align-items: center; gap: 10px; background: rgba(255,255,255,0.06); border: 1px solid rgba(196,254,97,0.2); padding: 16px 24px; border-radius: 12px;">
```
- `gap`: Espaço entre items (10px)
- `background`: Fundo semi-transparente branco (6% opacidade)
- `border`: Borda com verde limão (20% opacidade)
- `padding`: Espaço interno (16px 24px)
- `border-radius`: Cantos arredondados (12px)

## Localização Exata do CSS no index.html

Todo o CSS dos projectos está **inline** no próprio HTML, não em arquivos CSS separados. Procure na secção "Os nossos Projectos" por:

1. **Elemento container lazy-bg**: linha ~1868 para MADPiXEL, linha ~1928 para AutoGo, linha ~1985 para Aurora
2. **KPIs**: procure por `class="project-kpis"` (~linhas 1915, 1970, 2027)
3. **Buttons**: procure por `elementor-button` dentro dos containers de cada projecto

## Cor Principal

A cor principal do site é **#C4FE61** (verde limão). Se quiser mudar a cor dos destaques (números KPI, ícones, etc.), altere todas as instâncias de `color:#C4FE61` nos styles inline.

</content>
<parameter name="filePath">/workspaces/template/BACKGROUND_CHANGE_GUIDE.md