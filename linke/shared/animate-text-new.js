(function(){
  document.addEventListener('DOMContentLoaded', function () {
    const ensure = selector => {
      document.querySelectorAll(selector).forEach(node => node.classList.add('js-animate'));
    };

    // Known widget ids fallback
    ensure('[data-id="289b4c4"] .elementor-widget-container');
    ensure('[data-id="91b4ab0"] .elementor-widget-container');
    ensure('[data-id="b9190e4"] .elementor-widget-container');

    // Auto-target by text content across pages
    const phrases = [
      "Vamos construir o seu sonho",
      'Está na altura de levar',
      'Vamos elevar o seu projeto'
    ];
    const textSelectors = ['.elementor-heading-title', '.elementor-widget-container', 'h1', 'h2', 'h3', 'p'];
    phrases.forEach(phrase => {
      document.querySelectorAll(textSelectors.join(',')).forEach(el => {
        try {
          if (!el || !el.textContent) return;
          if (el.textContent.trim().includes(phrase)) {
            const container = el.closest('.elementor-widget-container') || el;
            container.classList.add('js-animate');
          }
        } catch (e) { /* ignore malformed nodes */ }
      });
    });

    const els = Array.from(document.querySelectorAll('.js-animate'));
    if (!els.length) return;

    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const index = els.indexOf(el);
        el.style.setProperty('--animate-delay', (index * 120) + 'ms');
        el.classList.add('in');
        obs.unobserve(el);
      });
    }, { threshold: 0.18 });

    els.forEach((el, i) => {
      el.style.setProperty('--animate-delay', (i * 120) + 'ms');
      observer.observe(el);
    });

    setTimeout(() => {
      els.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom >= 0) {
          if (!el.classList.contains('in')) el.classList.add('in');
        }
      });
    }, 80);
  });
})();
