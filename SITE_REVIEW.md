# Site Review – LINKE (Product Owner View)

## Snapshot
* Pages reviewed: primary home experience (`linke/index.html`) with navigation to Soluções, Sobre Nós, and Contato.
* Overall impression: strong brand visuals and Portuguese messaging, but the conversion path is unclear above the fold and the case studies lack measurable outcomes.

## Top opportunities (do first)
1. **Add a hero call-to-action that matches the promise.** The hero asks “Pronto para transformar o seu negócio?” but there is no immediate primary action near the question—only a “Scroll Down” cue and navigation links, so visitors must hunt for the next step. Add a prominent CTA (e.g., “Fale com um especialista” linking to Contato) visible on desktop and mobile within the hero container.
2. **Package the value prop and proof in the first viewport.** The “soluções integradas” message and CTAs to Sobre Nós/Contato appear below the hero (after the scroll prompt), meaning users see brand visuals before understanding what LINKE offers. Move or duplicate the value statement and contact CTA into the hero block so the offer and action are paired immediately.
3. **Turn project cards into quantified proof.** The “Os nossos Projectos” section describes clients like MADPiXEL but lacks metrics (conversion lift, cost/time saved). Add 2–3 bullet KPIs per card to show outcomes and link to detailed cases or solutions to build trust faster.
4. **Create a clear “choose your path” panel.** Navigation relies on top menu only. Add a mid-page card/CTA strip that routes prospects by intent (ex: “Lançar ecommerce”, “Otimizar operações”, “Escalar marketing”) to the relevant Soluções anchors.
5. **Trim heavy media on first paint.** The hero uses a background video container without an evident poster or fallback, which can delay first paint on slower connections. Provide a lightweight poster image for mobile and defer video loading until interaction.

## Secondary improvements
- **Social proof rhythm:** Introduce a concise client logo bar before the project grid to reassure new visitors earlier.
- **Form friction:** Ensure the Contato CTA jumps to a short, mobile-friendly form with 3–4 fields maximum; avoid sending users to a generic email link.
- **Content accessibility:** Maintain text shadow usage but verify color contrast on white-over-video elements; add aria-labels to burger toggles and ensure focus styles remain visible.
- **SEO clarity:** Set consistent `<h1>` hierarchy (currently multiple `<h2>`s carry primary messaging) and ensure meta description highlights “tecnologia + operações + atendimento” keywords present in the copy.

## Suggested next steps (2-week sprint)
1. Ship hero CTA + duplicated value statement (desktop & mobile) and measure click-through to Contato.
2. Add KPI bullets and outbound links for top 3 project cards; draft case study one-pagers.
3. Implement hero poster image and lazy-load the background video; record baseline vs. improved LCP.
4. Design and A/B test the “choose your path” CTA strip linking to Soluções anchors.

