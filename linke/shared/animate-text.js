document.addEventListener('DOMContentLoaded', function () {
  // Ensure target containers exist. If some widget HTML couldn't be edited, we add class here.
  const ensure = selector => {
    document.querySelectorAll(selector).forEach(node => node.classList.add('js-animate'));
  };

  // Fallback: add js-animate to known widget containers (by their data-id)
  ensure('[data-id="289b4c4"] .elementor-widget-container');
  ensure('[data-id="91b4ab0"] .elementor-widget-container');
  ensure('[data-id="b9190e4"] .elementor-widget-container');

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
    // set a default delay so elements stagger nicely
    el.style.setProperty('--animate-delay', (i * 120) + 'ms');
    observer.observe(el);
  });

  // In case some elements are already visible (e.g., large screens), trigger immediately
  setTimeout(() => {
    els.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom >= 0) {
        if (!el.classList.contains('in')) el.classList.add('in');
      }
    });
  }, 80);
});
